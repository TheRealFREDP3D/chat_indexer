# LLM Chat Indexer Configuration

## Module Structure

- Uses Python's built-in `os` module for environment variables
- Leverages `python-dotenv` for .env file support
- Implements a `Config` class with class-level attributes

## Key Features

- Loads environment variables at import time using `load_dotenv()`
- Provides default values for all settings
- Includes validation for critical configurations

## Main Configuration Settings

| Setting | Description |
|---------|-------------|
| `BASE_DIR` | Root directory for file operations |
| `OUTPUT_DIR` | Directory for generated files |
| `SUMMARY_FILENAME` | Output file name for summaries |
| `INDEX_FILENAME` | Output file name for indexes |
| `LLM_PROVIDER` | Default: `gemini/gemini-2.5-pro-exp-03-25` |
| `LLM_API_KEY` | API key for LLM service (via LiteLLM) |
| `SUPPORTED_FILE_EXTENSIONS` | List of processable file types |
| `MAX_TOPIC_KEYWORDS` | Maximum number of topics per file |
| `LOG_LEVEL` | Logging level configuration |
| `LOG_FILE` | Log file location |

## Validation Method

- `validate_config()`: Class method that checks for required settings
- Currently validates `LLM_API_KEY`
- Exits with error message if critical configs are missing

> **Note**: Configuration can be modified through environment variables or `.env` file without code changes.
