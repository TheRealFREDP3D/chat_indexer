"""
LLM Chat Indexer - Web Interface

Flask web application for the LLM Chat Indexer.
"""

import os
import sys
from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
from werkzeug.utils import secure_filename

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.config import Config
from src.web import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
