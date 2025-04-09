# File Parser Module

## Main Function

- **parse_file(file_path, content)**
  - Input: file path and content
  - Output: list of extracted messages
  - Routes parsing to appropriate handler based on extension

## Supported File Formats

### TXT Files

- `parse_txt()`
  - Simply splits text by lines

### Markdown Files

- `parse_md()`
  - Converts markdown to HTML and extracts:
    - Paragraphs
    - Headings (with proper heading levels)
    - List items
    - Blockquotes

### JSON Files

- `parse_json()`
  - Handles two JSON structures:
    - List of objects with "message" field
    - Object with "messages" array containing "content" field

### HTML Files

- `parse_html()`
  - Extracts text from paragraph tags

### CSV Files

- `parse_csv()`
  - Reads CSV files looking for:
    - "message" column
    - "content" column

## Error Handling

- Uses logging throughout the code
- Catches and logs specific exceptions for each format
- Returns empty list on any error
- Warns about unsupported file types
- Logs missing dependencies

## Dependencies

| Library | Purpose |
|---------|----------|
| BeautifulSoup | HTML parsing |
| markdown | Markdown processing |
| pandas | CSV handling |
| json | JSON processing (built-in) |

> **Note**: The code follows a modular structure with separate handlers for each file type, making it easy to maintain and extend for new formats.
