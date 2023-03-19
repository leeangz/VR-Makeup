from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS
import numpy as np
from io import BytesIO
from PIL import Image
from utils import apply_makeup, apply_feature
import cv2
import enum
from typing import List

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Do something with the file
    return 'File uploaded successfully'

class FeatureChoice(str, enum.Enum):
    lips = 'lips'
    blush = 'blush'
    foundation = 'foundation'


@app.route('/apply-makeup/', methods=['POST'])
def try_makeup():
    choice = request.form['choice']
    filePath = request.form['filePath']
    
    # Read the image file from the specified file path
    image = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
    
    # Apply the chosen makeup feature to the image
    output = apply_makeup(image, False, choice, False)
    
    # Save the output image to a file
    output_filepath = 'output.jpg'
    cv2.imwrite(output_filepath, output)
    
    # Return the output image as a JPEG file
    return send_file(output_filepath, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()