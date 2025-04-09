"""
Routes for the LLM Chat Indexer web interface.
"""

import os
import json
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, send_from_directory
from werkzeug.utils import secure_filename

from src.config import Config
from src.file_parser import parse_file
from src.llm_client import LLMClient
from src.index_builder import build_index, get_timestamp
from src.web.forms import UploadForm, SettingsForm

# Create blueprint
main_bp = Blueprint('main', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = set([ext.strip('.') for ext in Config.SUPPORTED_FILE_EXTENSIONS if ext.strip('.')])

def allowed_file(filename):
    """Check if a file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/')
def index():
    """Render the home page."""
    upload_form = UploadForm()
    return render_template('index.html', form=upload_form, title='LLM Chat Indexer')

@main_bp.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    form = UploadForm()
    
    if form.validate_on_submit():
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
            
        file = request.files['file']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Process the file
            try:
                # Read file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Initialize LLM client
                llm_client = LLMClient(Config.LLM_PROVIDER)
                
                # Parse file
                messages = parse_file(file_path, content)
                timestamp = get_timestamp(file_path)
                
                if not messages:
                    flash('No messages extracted from file', 'warning')
                    return redirect(url_for('main.index'))
                
                # Extract topics
                topics = llm_client.extract_topics(messages, Config.MAX_TOPIC_KEYWORDS)
                
                # Generate summary
                summary = llm_client.summarize(messages)
                
                # Create file data
                file_data = {
                    "filename": filename,
                    "path": file_path,
                    "timestamp": timestamp,
                    "topics": topics,
                    "summary": summary,
                    "message_count": len(messages)
                }
                
                # Build index
                os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
                build_index({"files": [file_data]}, Config.OUTPUT_DIR, Config.INDEX_FILENAME, Config.SUMMARY_FILENAME)
                
                flash('File processed successfully', 'success')
                return redirect(url_for('main.results'))
                
            except Exception as e:
                flash(f'Error processing file: {str(e)}', 'error')
                return redirect(url_for('main.index'))
        else:
            flash(f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
            return redirect(url_for('main.index'))
    
    flash('Form validation failed', 'error')
    return redirect(url_for('main.index'))

@main_bp.route('/results')
def results():
    """Show processing results."""
    # Check if index file exists
    index_path = os.path.join(Config.OUTPUT_DIR, Config.INDEX_FILENAME)
    if not os.path.exists(index_path):
        flash('No processed files found', 'warning')
        return redirect(url_for('main.index'))
    
    # Read index file
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    return render_template('results.html', 
                          title='Processing Results',
                          files=index_data.get('files', []))

@main_bp.route('/view/<filename>')
def view_file(filename):
    """View a specific file's summary."""
    # Check if index file exists
    index_path = os.path.join(Config.OUTPUT_DIR, Config.INDEX_FILENAME)
    if not os.path.exists(index_path):
        flash('No processed files found', 'warning')
        return redirect(url_for('main.index'))
    
    # Read index file
    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)
    
    # Find the file
    file_data = None
    for file in index_data.get('files', []):
        if file.get('filename') == filename:
            file_data = file
            break
    
    if not file_data:
        flash(f'File {filename} not found', 'error')
        return redirect(url_for('main.results'))
    
    return render_template('view.html', 
                          title=f'View {filename}',
                          file=file_data)

@main_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    """Settings page."""
    form = SettingsForm()
    
    if form.validate_on_submit():
        # Update settings
        # Note: This is a simplified version that doesn't actually update the .env file
        flash('Settings updated', 'success')
        return redirect(url_for('main.index'))
    
    # Pre-populate form with current settings
    form.llm_provider.data = Config.LLM_PROVIDER
    form.max_topic_keywords.data = Config.MAX_TOPIC_KEYWORDS
    form.output_dir.data = Config.OUTPUT_DIR
    
    return render_template('settings.html', 
                          title='Settings',
                          form=form)

@main_bp.route('/download/<filename>')
def download_file(filename):
    """Download a file from the output directory."""
    return send_from_directory(directory=Config.OUTPUT_DIR, path=filename, as_attachment=True)
