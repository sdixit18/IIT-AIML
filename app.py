from flask import Flask, render_template, request, redirect, url_for
from controllers.file_controller import upload_file, download_template
from controllers.report_controller import reports

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    return upload_file()

@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/download-template', methods=['GET'])
def download():
    return download_template()

@app.route('/reports', methods=['GET', 'POST'])
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
