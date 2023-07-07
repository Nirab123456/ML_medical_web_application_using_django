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

# class HandwrittenImageGenerator:
#     def __init__(self):
#         pass
#     def get_text(self,request):
#         if request.method == 'POST':
