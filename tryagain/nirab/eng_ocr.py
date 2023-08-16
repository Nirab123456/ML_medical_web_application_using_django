from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OCRImageForm
from .models import RecordImage
from .ENG_HANDWRITTEN import HandwrittenImageGenerator
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
import subprocess
import sys
import uuid
from django.conf import settings


PATH = settings.ENG_HANDWRITTEN_ROOT
BG_PATH = os.path.join(PATH, 'bg.png')

generator = HandwrittenImageGenerator(BG_PATH, PATH)

class ENGOCR:
    def __init__(self):
        pass

    def add_image(self, request):
        if request.method == 'POST':
            form = OCRImageForm(request.POST, request.FILES)
            if form.is_valid():
                existing_record = RecordImage.objects.filter(user=request.user).first()
                if existing_record:
                    existing_record.image.delete()  # Delete the old image
                    existing_record.image = form.cleaned_data['image']  # Update the image
                    existing_record.save()
                    messages.success(request, 'Image Updated Successfully')
                    image_url = existing_record.image.url
                    text,file_path = self.get_ocr(image_url)
                    if file_path:
                        return render(request, 'base_ocr.html', {'ENG_OCR_form': form, 'ENG_OCR_image_url': existing_record.image.url, 'ENG_OCR_text': text, 'ENG_OCR_file_path': file_path})
                else:
                    record_image = form.save(commit=False)
                    record_image.user = request.user
                    record_image.save()
                    messages.success(request, 'Image Added Successfully')
                    image_url = record_image.image.url
                    text,file_path = self.get_ocr(image_url)
                    if file_path:
                        return render(request, 'base_ocr.html', {'ENG_OCR_form': form, 'ENG_OCR_image_url': record_image.image.url, 'ENG_OCR_text': text, 'ENG_OCR_file_path': file_path})
        else:
            form = OCRImageForm()
        return render(request, 'base_ocr.html', {'ENG_OCR_form': form})

    def get_ocr(self, image_url):
        image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/').replace('media/', ''))
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            if img is not None:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
                os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
                text = pytesseract.image_to_string(gray, lang='eng')

                # Generate a unique file name
                file_name = f'{uuid.uuid4()}.txt'
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)

                return text,file_path
        return None
    
    def eng_ocr_handwritten(self, request):
        if request.method == 'POST':
            form = OCRImageForm(request.POST, request.FILES)
            if form.is_valid():
                existing_record = RecordImage.objects.filter(user=request.user).first()
                if existing_record:
                    existing_record.image.delete()  # Delete the old image
                    existing_record.image = form.cleaned_data['image']  # Update the image
                    existing_record.save()
                    messages.success(request, 'Image Updated Successfully')
                    image_url = existing_record.image.url
                    text,file_path = self.get_ocr(image_url)
                    # MAIN_TXT_FILE ='boom.txt'
                    # MAIN_FILE_NAME=  MAIN_TXT_FILE.split('.')[0]

                    MAIN_TXT_FILE = file_path
                    MAIN_FILE_PATH, MAIN_FILE_NAME = os.path.split(MAIN_TXT_FILE)# split the path and filename
                    MAIN_FILE_NAME_WITHOUT_EXT = os.path.splitext(MAIN_FILE_NAME)[0]# split the filename and extension
                    output_dir = MAIN_FILE_PATH# output directory
                    output_file = os.path.join(output_dir, f"{MAIN_FILE_NAME_WITHOUT_EXT}.pdf")# output file name
                    with open(MAIN_TXT_FILE, 'r') as file:
                        data = file.read().replace('\n', '')

                    l = len(data)
                    nn = len(data) // 500
                    FILE_NAMES = []

                    for i in range(nn):
                        unique_id = uuid.uuid4().hex  # Generate a unique ID
                        file_name = f'{unique_id}.txt'  # Create a unique file name
                        FILE_NAMES.append(file_name)  # Add the file name to the list
                        
                        with open(file_name, 'w') as file:
                            file.write(data[i * 600:(i + 1) * 600])
                            
####################################################################################

                    PHOTO_FILENAME = []
                    for file_name in FILE_NAMES:
                        with open(file_name, 'r') as file:
                            data = file.read().replace('\n', '')
                            generator.generate_handwritten_image(data, f"{file_name}_outt.png")
                            PHOTO_FILENAME.append(f"{file_name}_outt.png")

                    pdf = generator.convert_photos_to_pdf(PHOTO_FILENAME, output_file)

                    # detete file_names and 
                    for file_name in FILE_NAMES:
                        os.remove(file_name)
                    for file_name in PHOTO_FILENAME:
                        os.remove(file_name)

                    pdf_output_file = output_file


                    if file_path:
                        return render(request, 'base_ocr.html', {'ENG_OCR_form': form, 'ENG_OCR_image_url': existing_record.image.url, 'ENG_OCR_text': text, 'ENG_OCR_file_path': file_path , 'ENG_OCR_pdf_output_file':pdf_output_file})
                
                
                
                
                else:




                    record_image = form.save(commit=False)
                    record_image.user = request.user
                    record_image.save()
                    messages.success(request, 'Image Added Successfully')
                    image_url = record_image.image.url
                    text,file_path = self.get_ocr(image_url)


                    MAIN_TXT_FILE = file_path
                    MAIN_FILE_PATH, MAIN_FILE_NAME = os.path.split(MAIN_TXT_FILE)# split the path and filename
                    MAIN_FILE_NAME_WITHOUT_EXT = os.path.splitext(MAIN_FILE_NAME)[0]# split the filename and extension
                    output_dir = MAIN_FILE_PATH# output directory
                    output_file = os.path.join(output_dir, f"{MAIN_FILE_NAME_WITHOUT_EXT}.pdf")# output file name
                    with open(MAIN_TXT_FILE, 'r') as file:
                        data = file.read().replace('\n', '')

                    l = len(data)
                    nn = len(data) // 500
                    FILE_NAMES = []

                    for i in range(nn):
                        unique_id = uuid.uuid4().hex  # Generate a unique ID
                        file_name = f'{unique_id}.txt'  # Create a unique file name
                        FILE_NAMES.append(file_name)  # Add the file name to the list
                        
                        with open(file_name, 'w') as file:
                            file.write(data[i * 600:(i + 1) * 600])


####################################################################################
                    PHOTO_FILENAME = []
                    for file_name in FILE_NAMES:
                        with open(file_name, 'r') as file:
                            data = file.read().replace('\n', '')
                            generator.generate_handwritten_image(data, f"{file_name}_outt.png")
                            PHOTO_FILENAME.append(f"{file_name}_outt.png")

                    pdf = generator.convert_photos_to_pdf(PHOTO_FILENAME, output_file)

                    # detete file_names and 
                    for file_name in FILE_NAMES:
                        os.remove(file_name)
                    for file_name in PHOTO_FILENAME:
                        os.remove(file_name)

                    pdf_output_file = output_file
                    print('text path',file_path)
                    print('pdf path',pdf_output_file)


                    if file_path:
                        return render(request, 'base_ocr.html', {'ENG_OCR_form': form, 'ENG_OCR_image_url': record_image.image.url, 'ENG_OCR_text': text, 'ENG_OCR_file_path': file_path, 'ENG_OCR_pdf_output_file':pdf_output_file})
        else:
            form = OCRImageForm()
        return render(request, 'base_ocr.html', {'ENG_OCR_form': form})
