from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OCRImageForm
from .models import RecordImage
import cv2
import os
import pytesseract
import uuid
from django.conf import settings

class BanglaOCR:
    def __init__(self):
        pass

    def add_image(self, request):
        if request.method == 'POST':
            print('i am here')
            form = OCRImageForm(request.POST, request.FILES)
            if form.is_valid():
                print('i am here 2')
                existing_record = RecordImage.objects.filter(user=request.user).first()
                if existing_record:
                    existing_record.image.delete()  # Delete the old image
                    existing_record.image = form.cleaned_data['image']  # Update the image
                    existing_record.save()
                    messages.success(request, 'Image Updated Successfully')
                    image_url = existing_record.image.url
                    text,file_path = self.get_ocr(image_url)
                    print('text:',text)
                    if file_path:
                        return render(request, 'base_ocr.html', {'BN_OCR_form': form, 'BN_OCR_image_url': existing_record.image.url, 'BN_OCR_text': text, 'BN_OCR_file_path': file_path})
                else:
                    record_image = form.save(commit=False)
                    record_image.user = request.user
                    record_image.save()
                    messages.success(request, 'Image Added Successfully')
                    image_url = record_image.image.url
                    text,file_path = self.get_ocr(image_url)
                    print('text:',text)
                    if file_path:
                        return render(request, 'base_ocr.html', {'BN_OCR_form': form, 'BN_OCR_image_url': record_image.image.url, 'BN_OCR_text': text, 'BN_OCR_file_path': file_path})
        else:
            form = OCRImageForm()
        return render(request, 'base_ocr.html', {'BN_OCR_form': form})

    def get_ocr(self, image_url):
        image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/').replace('media/', ''))
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            if img is not None:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
                os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
                text = pytesseract.image_to_string(gray, lang='Bengali')

                # Generate a unique file name
                file_name = f'{uuid.uuid4()}.txt'
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)

                return text,file_path
        return None
