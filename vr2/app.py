import numpy as np
from flask import Flask
from fastapi import File, UploadFile
from io import BytesIO
from PIL import Image
from utils import apply_makeup, apply_feature
from starlette.responses import StreamingResponse
import cv2
import enum
from typing import List

app = Flask(__name__)

class FeatureChoice(str, enum.Enum):

    lips = 'lips'
    blush = 'blush'
    foundation = 'foundation'

@app.route('/tospring')
def spring():
    return '스프링으로 보내'

if __name__ == '__main__':
    app.run()