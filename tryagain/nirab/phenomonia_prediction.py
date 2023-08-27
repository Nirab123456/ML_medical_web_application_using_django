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

# Import Libraries
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch 
import torch.nn as nn 
from PIL import Image





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
                image_path = image.image
                self.image_path = image_path
                image_url = image_path.url
                prediction = self.get_phenomonia_prediction()
                return render(request, 'C_V_D_prediction.html', {'form': form,'image_path':image_url,'phenomonia_prediction':prediction})
        else:
            form = phenomonia_prediction_form()
        return render(request, 'C_V_D_prediction.html', {'form': form})
    

    def get_phenomonia_prediction(self):
        image_path = self.image_path
        transformations = transforms.Compose([
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        test_single_image_path = image_path
        test_single_image = Image.open(test_single_image_path).convert("RGB")
        test_single_image = transformations(test_single_image)

        # Load the pretrained model
        model = models.resnet18(pretrained=True)
        # Freeze model parameters
        for param in model.parameters():
            param.requires_grad = False
        # Change the final layer of densenet model
        classifier_input = model.fc.in_features
        num_labels = 2
        classifier = nn.Sequential(nn.Linear(classifier_input, 100),
                                    nn.ReLU(),
                                    nn.Linear(100, 512),
                                    nn.ReLU(),
                                    nn.Dropout(p=0.5),
                                    nn.Linear(512, 128),
                                    nn.ReLU(),
                                    nn.Dropout(p=0.5),
                                    nn.Linear(128, 64),
                                    nn.ReLU(),
                                    nn.Dropout(p=0.5),
                                    nn.Linear(64, num_labels),
                                    nn.LogSoftmax(dim=1))
        model.fc = classifier
        #load the model
        model.load_state_dict(torch.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles', 'phenomonia_main.pt')))
        model.eval()
        # Test out your network!
        with torch.no_grad():
            output = model(test_single_image.unsqueeze(0))
            ps = torch.exp(output)
            top_p, top_class = ps.topk(1, dim=1)
            if top_class == 0:
                prediction = 'NORMAL'
            else:
                prediction = 'PNEUMONIA'
        return prediction

