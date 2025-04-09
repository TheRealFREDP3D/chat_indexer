"""
File parsing module for LLM Chat Indexer.
Handles various file formats to extract chat messages.

This module uses an object-oriented approach with:
1. An abstract base class (FileParser) that defines the parser interface
2. Concrete parser implementations for each supported file type
3. A factory class (ParserFactory) to create the appropriate parser

Classes:
    FileParser: Abstract base class for all file parsers
    TxtParser: Parser for plain text files
    MarkdownParser: Parser for markdown files
    JsonParser: Parser for JSON files
    HtmlParser: Parser for HTML files
    CsvParser: Parser for CSV files
    ParserFactory: Factory class to create appropriate parser instances

Functions:
    parse_file(file_path, content): Main function that routes file parsing based on extension

Supported File Formats:
    - .txt: Plain text files, split by lines
    - .md: Markdown files, extracts paragraphs, headings, lists and quotes
    - .json: JSON files with either list of messages or messages object
    - .html: HTML files, extracts paragraph content
    - .csv: CSV files with 'message' or 'content' columns

Error Handling:
    - Logs warnings for unsupported file types
    - Logs errors for parsing failures
    - Returns empty list on any error
"""

import os
import json
import logging
from abc import ABC, abstractmethod
import pandas as pd
from bs4 import BeautifulSoup
from markdown import markdown

logger = logging.getLogger("LLMChatIndexer")


class FileParser(ABC):
    """Abstract base class for file parsers."""

    def __init__(self, file_path):
        """
        Initialize the parser with file path.

        Args:
            file_path (str): Path to the file being parsed
        """
        self.file_path = file_path

    @abstractmethod
    def parse(self, content):
        """
        Parse the file content and extract messages.

        Args:
            content (str): File content as string

        Returns:
            list: Extracted messages from the file
        """
        pass


class TxtParser(FileParser):
    """Parser for plain text files."""

    def parse(self, content):
        """
        Parse plain text content by splitting into lines.

        Args:
            content (str): Text file content

        Returns:
            list: Lines from the text file
        """
        return content.splitlines()


class MarkdownParser(FileParser):
    """Parser for markdown files."""

    def parse(self, content):
        """
        Parse markdown content by converting to HTML and extracting structured content.

        Args:
            content (str): Markdown content

        Returns:
            list: Extracted messages from markdown
        """
        try:
            html = markdown(content, extensions=["extra"])
            soup = BeautifulSoup(html, "html.parser")
            messages = []

            for p in soup.find_all("p"):
                if p.get_text().strip():
                    messages.append(p.get_text().strip())

            for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
                level = int(heading.name[1])
                messages.append(f"{'#' * level} {heading.get_text().strip()}")

            for list_elem in soup.find_all(["ul", "ol"]):
                for item in list_elem.find_all("li"):
                    messages.append(f"- {item.get_text().strip()}")

            for quote in soup.find_all("blockquote"):
                messages.append(f"> {quote.get_text().strip()}")

            if not messages:
                logger.warning(f"No content extracted from markdown file {self.file_path}")

            return messages
        except ImportError as e:
            logger.error(f"Missing dependencies for markdown parsing: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error parsing markdown file {self.file_path}: {str(e)}")
            return []


class JsonParser(FileParser):
    """Parser for JSON files."""

    def parse(self, content):
        """
        Parse JSON content to extract messages.

        Args:
            content (str): JSON content

        Returns:
            list: Extracted messages from JSON
        """
        try:
            data = json.loads(content)
            if isinstance(data, list):
                return [entry.get("message", "") for entry in data if "message" in entry]
            elif isinstance(data, dict) and "messages" in data:
                return [entry.get("content", "") for entry in data["messages"] if "content" in entry]
            logger.warning(f"Unsupported JSON structure in {self.file_path}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {self.file_path}: {str(e)}")
        except Exception as e:
            logger.error(f"Error parsing JSON file {self.file_path}: {str(e)}")
        return []


class HtmlParser(FileParser):
    """Parser for HTML files."""

    def parse(self, content):
        """
        Parse HTML content to extract paragraph text.

        Args:
            content (str): HTML content

        Returns:
            list: Extracted paragraph text from HTML
        """
        try:
            soup = BeautifulSoup(content, "html.parser")
            return [p.get_text() for p in soup.find_all("p")]
        except Exception as e:
            logger.error(f"Error parsing HTML file {self.file_path}: {str(e)}")
            return []


class CsvParser(FileParser):
    """Parser for CSV files."""

    def parse(self, content):
        """
        Parse CSV content to extract messages.
        Note: The content parameter is not used as CSV files are read directly.

        Args:
            content (str): Not used for CSV parsing, file is read directly

        Returns:
            list: Extracted messages from CSV
        """
        try:
            df = pd.read_csv(self.file_path)
            if "message" in df.columns:
                return df["message"].dropna().tolist()
            elif "content" in df.columns:
                return df["content"].dropna().tolist()
            logger.warning(f"No message or content column found in CSV file {self.file_path}")
        except Exception as e:
            logger.error(f"Error parsing CSV file {self.file_path}: {str(e)}")
        return []


class ParserFactory:
    """Factory class to create appropriate parser instances."""

    @staticmethod
    def get_parser(file_path):
        """
        Create and return the appropriate parser for the given file.

        Args:
            file_path (str): Path to the file

        Returns:
            FileParser: An instance of the appropriate parser or None if unsupported
        """
        ext = os.path.splitext(file_path)[1].lower()
        parsers = {
            ".txt": TxtParser,
            ".md": MarkdownParser,
            ".json": JsonParser,
            ".html": HtmlParser,
            ".csv": CsvParser,
        }

        parser_class = parsers.get(ext)
        if parser_class:
            return parser_class(file_path)
        else:
            logger.warning(f"Unsupported file extension: {ext} for file {file_path}")
            logger.info(f"Supported extensions are: {', '.join(parsers.keys())}")
            return None


def parse_file(file_path, content):
    """
    Parse file content based on its extension to extract chat messages.

    Args:
        file_path (str): Path to the file
        content (str): File content as string

    Returns:
        list: Extracted messages from the file
    """
    try:
        parser = ParserFactory.get_parser(file_path)
        if parser:
            return parser.parse(content)
        return []
    except Exception as e:
        logger.error(f"Unexpected error processing file {file_path}: {str(e)}")
        return []
