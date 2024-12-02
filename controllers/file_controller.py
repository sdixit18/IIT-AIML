from flask import request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from config import Config
from models.excel_processor import ExcelProcessor

def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    if file and file.filename.endswith('.xlsx'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Process Excel file
        processor = ExcelProcessor(file_path)
        data = processor.data

        return render_template('display.html', data=data)
    return "Invalid file format"

def download_template():
    template_path = os.path.join('data', 'oil.xlsx')
    return send_file(template_path, as_attachment=True, download_name='oil.xlsx')
