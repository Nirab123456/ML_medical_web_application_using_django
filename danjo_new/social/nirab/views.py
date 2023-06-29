
from PIL import Image

import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
from django.shortcuts import render,redirect

from django.conf import settings



def home(request):


    return render(request, 'home.html',{})

def ocr(request):
    if request.method == 'POST':
        image = request.FILES['img']
        image_path = os.path.join(settings.MEDIA_ROOT, image.name)

        with open(image_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        img = cv2.imread(image_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
        os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
        text = pytesseract.image_to_string(img_gray, lang='Bengali')
        return render(request, 'ocr.html', {'text': text})

    return render(request, 'ocr.html', {})