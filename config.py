import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data')  # Change to the 'data' folder
    ALLOWED_EXTENSIONS = {'xlsx'}
