"""
Configuration module for LLM Chat Indexer.

This module loads environment variables from a .env file and provides
configuration settings for the LLM Chat Indexer application. Environment
variables are loaded at import time, before the Config class is instantiated.

Environment variables can be set in a .env file in the project root or
directly in the system environment. Values in the .env file will override
system environment variables.
"""

import os
import sys
from dotenv import load_dotenv
from litellm import fallbacks

# Load environment variables from .env file at import time
# This happens before any Config instances are created
load_dotenv()


class Config:
    """Configuration class for LLM Chat Indexer.

    Default values are provided for all settings, but critical settings
    like LLM_API_KEY should be set in the environment or .env file.

    Attributes:
        BASE_DIR (str): Base directory for file operations, defaults to current working directory
        OUTPUT_DIR (str): Directory for generated files, relative to BASE_DIR unless absolute
        SUMMARY_FILENAME (str): Filename for generated summary file, defaults to "summary.md"
        INDEX_FILENAME (str): Filename for generated index file, defaults to "index.json"
        LLM_PROVIDER (str): LLM provider identifier, defaults to "gemini/gemini-2.5-pro-exp-03-25"
        LLM_API_KEY (str): API key for LLM provider, must be set in environment
        SUPPORTED_FILE_EXTENSIONS (list): List of supported file extensions for processing
        MAX_TOPIC_KEYWORDS (int): Maximum number of topic keywords to extract, defaults to 5
        LOG_LEVEL (str): Logging level, defaults to "INFO"
        LOG_FILE (str): Path to log file, defaults to "logs/chat_indexer.log"
    """

    # Base directory for file operations
    BASE_DIR = os.getenv("BASE_DIR", os.getcwd())

    # Output directory for generated files (relative to BASE_DIR unless absolute path)
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")

    # Filenames for generated output
    SUMMARY_FILENAME = os.getenv("SUMMARY_FILENAME", "summary.md")
    INDEX_FILENAME = os.getenv("INDEX_FILENAME", "index.json")

    # LLM service configuration
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini/gemini-2.5-pro-exp-03-25")
    # API key can be from any supported provider (see .env.template examples)
    LLM_API_KEY = os.getenv("LLM_API_KEY")  # Supports GOOGLE_API_KEY/OPENAI_API_KEY etc via LiteLLM

    # File types that can be processed
    SUPPORTED_FILE_EXTENSIONS = os.getenv("SUPPORTED_FILE_EXTENSIONS", ".txt,.md,.json,.html,.csv,").split(",")

    # Processing parameters
    MAX_TOPIC_KEYWORDS = int(os.getenv("MAX_TOPIC_KEYWORDS", 5))

    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/chat_indexer.log")

    @classmethod
    def validate_config(cls):
        """Validate critical configuration settings.

        Checks for required settings and exits with an error message if any are missing.
        This should be called at application startup to prevent runtime errors.

        Raises:
            SystemExit: If any critical configurations are missing
        """
        missing_configs = []

        # Check for critical configurations
        if not cls.LLM_API_KEY:
            missing_configs.append("LLM_API_KEY")

        # Add validation for other critical configs as needed

        if missing_configs:
            print(f"ERROR: Missing critical configuration(s): {', '.join(missing_configs)}")
            print("Please set these values in your environment or .env file.")
            sys.exit(1)
