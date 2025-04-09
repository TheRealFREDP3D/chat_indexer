"""
Web interface package for LLM Chat Indexer.
"""

import os
import secrets
from flask import Flask
from src.config import Config

def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'templates'),
                static_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static'))
    
    # Set secret key for session management
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    
    # Set upload folder
    app.config['UPLOAD_FOLDER'] = os.path.abspath(Config.BASE_DIR)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size
    
    # Register blueprints
    from src.web.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Ensure the upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    return app
