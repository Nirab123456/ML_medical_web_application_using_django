from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  OCRImageForm
from . models import  RecordImage
from django.shortcuts import get_object_or_404
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract






class BanglaOCR:
    def __init__(self) -> None:
        pass

    def add_image(self,request):
        if request.method == 'POST':
            form = OCRImageForm(request.POST, request.FILES)
            if form.is_valid():
                existing_record = RecordImage.objects.filter(user=request.user).first()
                if existing_record:
                    existing_record.image.delete()  # Delete the old image
                    existing_record.image = form.cleaned_data['image']  # Update the image
                    existing_record.save()
                    messages.success(request, 'Image Updated Successfully')
                    # Load the image
                    image = Image.open(existing_record.image.path)
                    return render(request, 'bangla_ocr.html', {'form': form, 'image_url': existing_record.image.url})
                else:
                    record_image = form.save(commit=False)
                    record_image.user = request.user
                    record_image.save()
                    image = Image.open(record_image.image.path)
                    messages.success(request, 'Image Added Successfully')
                    return render(request, 'bangla_ocr.html', {'form': form, 'image_url': record_image.image.url})
                
        else:
            form = OCRImageForm()
        
        return render(request, 'add_image.html', {'form': form})













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
