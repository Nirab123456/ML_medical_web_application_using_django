from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OCRImageForm
from .models import RecordImage
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

class BanglaOCR:
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
                        print(file_path)
                    return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url, 'text': text, 'file_path': file_path})
                else:
                    record_image = form.save(commit=False)
                    record_image.user = request.user
                    record_image.save()
                    messages.success(request, 'Image Added Successfully')
                    image_url = record_image.image.url
                    text,file_path = self.get_ocr(image_url)
                    if file_path:
                        print(file_path)
                    return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url, 'text': text, 'file_path': file_path})
        else:
            form = OCRImageForm()
        return render(request, 'add_image.html', {'form': form})

    def get_ocr(self, image_url):
        image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/').replace('media/', ''))
        print(image_path)  # Add this line to print the image path
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

















































# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import OCRImageForm
# from .models import RecordImage
# from PIL import Image
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import pytesseract
# import subprocess
# import sys
# import uuid
# from django.conf import settings

# class BanglaOCR:
#     def __init__(self):
#         pass

#     def add_image(self, request):
#         if request.method == 'POST':
#             form = OCRImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 existing_record = RecordImage.objects.filter(user=request.user).first()
#                 if existing_record:
#                     existing_record.image.delete()  # Delete the old image
#                     existing_record.image = form.cleaned_data['image']  # Update the image
#                     existing_record.save()
#                     messages.success(request, 'Image Updated Successfully')
#                     image_url = existing_record.image.url
#                     file_path=self.get_ocr(image_url)
#                     print(file_path)
#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url})
#                 else:
#                     record_image = form.save(commit=False)
#                     record_image.user = request.user
#                     record_image.save()
#                     messages.success(request, 'Image Added Successfully')
#                     image_url = record_image.image.url
#                     file_path=self.get_ocr(image_url)
#                     print(file_path)
#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url})
#         else:
#             form = OCRImageForm()
#         return render(request, 'add_image.html', {'form': form})

#     def get_ocr(self, image_url):
#         image_path = os.path.join(settings.MEDIA_ROOT, image_url.lstrip('/'))
#         if os.path.exists(image_path):
#             img = cv2.imread(image_path)
#             if img is not None:
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
#                 os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
#                 text = pytesseract.image_to_string(gray, lang='Bengali')
#                 return text

                # # Generate a unique file name
                # file_name = f'{uuid.uuid4()}.txt'
                # file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                # with open(file_path, 'w', encoding='utf-8') as file:
                #     file.write(text)

                # # Optionally, you can return the file path to the view or perform any additional operations
                # return file_path






















































# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import  OCRImageForm
# from . models import  RecordImage
# from django.shortcuts import get_object_or_404
# from PIL import Image
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import pytesseract
# import subprocess
# import sys
# import uuid





# class BanglaOCR:
#     def __init__(self) -> None:
#         pass

#     def add_image(self,request):
#         if request.method == 'POST':
#             form = OCRImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 existing_record = RecordImage.objects.filter(user=request.user).first()
#                 if existing_record:
#                     existing_record.image.delete()  # Delete the old image
#                     existing_record.image = form.cleaned_data['image']  # Update the image
#                     existing_record.save()
#                     messages.success(request, 'Image Updated Successfully')
#                     image_url  = existing_record.image.url
#                     ############################################
#                     self.get_ocr(image_url)

#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url})
#                 else:
#                     record_image = form.save(commit=False)
#                     record_image.user = request.user
#                     record_image.save()
#                     messages.success(request, 'Image Added Successfully')
#                     image_url  = record_image.image.url
#                     ############################################
#                     self.get_ocr(image_url)
#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url})
                
#         else:
#             form = OCRImageForm()
        
#         return render(request, 'add_image.html', {'form': form})
    

#     def get_ocr(self, image_url):
#         image_path = image_url
#         if image_path:            
#             img = cv2.imread(image_path)
#             if img is not None and not img.empty():
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
#                 os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
#                 text = pytesseract.image_to_string(gray, lang='Bengali')

#                 with open(f'{uuid.uuid4()}.txt', 'w', encoding='utf-8') as file:
#                     file.write(text)

    
























# class BanglaOCR:
#     def __init__(self) -> None:
#         pass

#     def add_image(self,request):
#         if request.method == 'POST':
#             form = OCRImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 existing_record = RecordImage.objects.filter(user=request.user).first()
#                 if existing_record:
#                     existing_record.image.delete()  # Delete the old image
#                     existing_record.image = form.cleaned_data['image']  # Update the image
#                     existing_record.save()
#                     messages.success(request, 'Image Updated Successfully')
#                     image_url  = existing_record.image.url

#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url})
#                 else:
#                     record_image = form.save(commit=False)
#                     record_image.user = request.user
#                     record_image.save()
#                     messages.success(request, 'Image Added Successfully')
#                     image_url  = record_image.image.url
#                     return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url})
                
#         else:
#             form = OCRImageForm()
        
#         return render(request, 'add_image.html', {'form': form})













# def add_image(request):
#     if request.method == 'POST':
#         form = OCRImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             existing_record = RecordImage.objects.filter(user=request.user).first()
#             if existing_record:
#                 existing_record.image.delete()  # Delete the old image
#                 existing_record.image = form.cleaned_data['image']  # Update the image
#                 existing_record.save()
#                 messages.success(request, 'Image Updated Successfully')
#                 # Load the image
#                 image = Image.open(existing_record.image.path)
#                 return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url})
#             else:
#                 record_image = form.save(commit=False)
#                 record_image.user = request.user
#                 record_image.save()
#                 image = Image.open(record_image.image.path)
#                 messages.success(request, 'Image Added Successfully')
#                 return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url})
               
#     else:
#         form = OCRImageForm()
    
#     return render(request, 'add_image.html', {'form': form})


# def get_ocr(request):
#     if request.method == 'POST':
#         form = OCRImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             existing_record = RecordImage.objects.filter(user=request.user).first()
#             if existing_record:
#                 messages.success(request, 'Image found to extract text from')
#                 return render(request, 'bangla_ocr_result.html', {'form': form, 'image_url': existing_record.image.url})

#     form = OCRImageForm()
#     messages.success(request, 'No Image Found')
#     return render(request, 'bangla_ocr.html', {'form': form})
