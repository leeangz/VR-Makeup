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
    lips = request.form['lips']
    blush = request.form['blush']
    foundation = request.form['foundation']
    filePath = request.form['filePath']
    
    # 색상별 BGR값 부여 -> lips
    if lips=='red': color=(0,0,255)
    elif lips=='orange': color=(0,127,255)
    elif lips=='purple': color=(102,000,153)
    elif lips=='lightpurple' : color=(130,0,75)
    elif lips=='pink': color=(255,0,255)
    elif lips=='coral' : color=(0,102,255)
    elif lips=='beige' : color=(0,153,204)
    elif lips=='rose' : color=(0,0,102)
    elif lips=='darkrose' : color=(000,000,102)
    elif lips=='salmon' : color=(000,000,204)
    elif lips=='none' : color=()
    
     # 색상별 BGR값 부여 -> blush
    if blush=='red': color=(0,0,255)
    elif blush=='orange': color=(0,127,255)
    elif blush=='purple': color=(102,000,153)
    elif blush=='lightpurple' : color=(130,0,75)
    elif blush=='pink': color=(255,0,255)
    elif blush=='coral' : color=(0,102,255)
    elif blush=='beige' : color=(0,153,204)
    elif blush=='rose' : color=(0,0,102)
    elif blush=='darkrose' : color=(000,000,102)
    elif blush=='salmon' : color=(000,000,204)
    elif blush=='none' : color=()
    
     # 색상별 BGR값 부여 -> lips
    if foundation=='none': color=(0,0,255)
    elif foundation=='dark': color=(0,127,255)
    elif foundation=='warmbeige': color=(102,000,153)
    elif foundation=='coolpink' : color=(130,0,75)
    elif foundation=='lightbeige': color=(255,0,255)
    
    # 파일경로 불러오기
    image = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
    
    # 각 부위 별 색상 넣기
    output_lip = apply_makeup(image, False, 'lips', color, False)
    output_blush = apply_makeup(image, False, 'blush', color, False)
    output_foundation = apply_makeup(image, False, 'foundation', color, False)
    
    # Blend the three output images together
    alpha1 = 0.5 
    alpha2 = 0.3  
    alpha3 = 0.2  
    beta = 1 - (alpha1 + alpha2 + alpha3)
    blend = cv2.addWeighted(output_lip, alpha1, output_blush, alpha2, 0)
    blend = cv2.addWeighted(blend, 1, output_foundation, alpha3, 0)
    
    # output 저장 -> 뒤에 시간에 따른 uuid 붙음
    output_filename = f"output_{int(time.time())}_{uuid.uuid4()}.jpg"
    output_filepath = f"C:/dev64/thehyundai/color/img/{output_filename}"
    cv2.imwrite(output_filepath, blend)
    
    # jpg로 return
    return output_filename

if __name__ == '__main__':
    app.run()