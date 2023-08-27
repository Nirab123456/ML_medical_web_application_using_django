from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
import os
from .forms import phenomonia_prediction_form
from .models import PHENOMONIA_PREDICTION
from PIL import Image
import cv2
from django.conf import settings






class PHENOMONIA_PREDICTION_CLASS():
    def __init__(self, request):
        self.request = request

        
    def phenomonia_prediction(self):
        request = self.request
        if request.method == 'POST':
            form = phenomonia_prediction_form(request.POST, request.FILES)
            if form.is_valid():
                #get image from form
                image = form.cleaned_data['image']
                print(image)
                #open image
                img = Image.open(image)
            return render(request, 'C_V_D_prediction.html', {'X_P_prediction_form': form, 'X_P_prediction_img': img})
        else:
            form = phenomonia_prediction_form()
            return render(request, 'C_V_D_prediction.html', {'X_P_prediction_form': form})


