from flask import Flask
import os

base_path = os.getcwd()
file_path = os.path.normpath('/uploads')
abs_path = os.path.join(base_path+file_path)
if os.path.exists(abs_path):
    print(abs_path)
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = abs_path
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024