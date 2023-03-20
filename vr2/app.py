from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS
import numpy as np
from io import BytesIO
from PIL import Image
from utils import apply_makeup, apply_feature
import cv2
import enum
import uuid
import time
from typing import Tuple

app = Flask(__name__)
CORS(app)

class FeatureChoice(str, enum.Enum):
    lips = 'lips'
    blush = 'blush'
    foundation = 'foundation'


@app.route('/apply-makeup/', methods=['POST'])
def try_makeup():
    choice = request.form['choice']
    filePath = request.form['filePath']
    color = request.form['color']
    
    if color=='red': color=(0,0,255)
    elif color=='orange': color=(0,127,255)
    elif color=='purple': color=(255,0,255)
    elif color=='pink': color=(234,5,250)
    
    # 파일경로 불러오기
    image = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
    
    # 메이크업 방식 선택
    output = apply_makeup(image, False, choice, color, False)
    
    # output 저장 -> 뒤에 시간에 따른 uuid 붙음
    output_filename = f"output_{int(time.time())}_{uuid.uuid4()}.jpg"
    output_filepath = f"C:/dev64/thehyundai/color/img/{output_filename}"
    cv2.imwrite(output_filepath, output)
    
    # jpg로 return
    return output_filename

if __name__ == '__main__':
    app.run()