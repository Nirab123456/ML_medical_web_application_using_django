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
                #get image from form and pass it to web page
                image = form.cleaned_data['image']
                #save image to database
                PHENOMONIA_PREDICTION.objects.create(user=request.user,image=image)
                #get image from database
                image = PHENOMONIA_PREDICTION.objects.filter(user=request.user).last()
                #get image path
                image_path = image.image.url
                return render(request, 'C_V_D_prediction.html', {'form': form,'image_path':image_path})
        else:
            form = phenomonia_prediction_form()
        return render(request, 'C_V_D_prediction.html', {'form': form})

