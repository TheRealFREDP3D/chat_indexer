"""
Forms for the LLM Chat Indexer web interface.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from src.config import Config

# Get allowed extensions
ALLOWED_EXTENSIONS = [ext.strip('.') for ext in Config.SUPPORTED_FILE_EXTENSIONS if ext.strip('.')]

class UploadForm(FlaskForm):
    """Form for uploading files."""
    file = FileField('Select File', 
                    validators=[
                        FileRequired(),
                        FileAllowed(ALLOWED_EXTENSIONS, f'Only {", ".join(ALLOWED_EXTENSIONS)} files allowed')
                    ])
    submit = SubmitField('Upload and Process')

class SettingsForm(FlaskForm):
    """Form for configuring settings."""
    llm_provider = StringField('LLM Provider', 
                              validators=[DataRequired()],
                              description='Provider identifier (e.g., gemini/gemini-2.0-flash)')
    max_topic_keywords = IntegerField('Max Topic Keywords',
                                    validators=[NumberRange(min=1, max=20)],
                                    description='Maximum number of topics to extract per file')
    output_dir = StringField('Output Directory',
                            validators=[DataRequired()],
                            description='Directory for output files')
    submit = SubmitField('Save Settings')
