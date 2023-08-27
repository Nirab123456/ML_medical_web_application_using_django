from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
import os

model = nn.Sequential(
    nn.Linear(17, 64),
    nn.ReLU(),
    nn.Linear(64, 64),
    nn.ReLU(),
    nn.Linear(64, 1),
    nn.Sigmoid()
)


class C_V_D_PREDICTION():
    def __init__(self, request):
        self.request = request


    def get_C_V_D_prediction(self):
        request = self.request
        gender = request.GET.get('gender')
        bmi = request.GET.get('bmi')
        ethnic_group = request.GET.get('ethnic_group')
        age = request.GET.get('age')
        alcohol = request.GET.get('alcohole')
        smoke = request.GET.get('smoke')
        exercise = request.GET.get('exersise')
        psychology = request.GET.get('psychologogy')
        sleeping_time = request.GET.get('sleeping_time')
        stroke = request.GET.get('stroke')
        physical_health = request.GET.get('physical_health')
        general_health = request.GET.get('general_health')
        diff_walking = request.GET.get('diff_walking')
        diabetic = request.GET.get('diabetic')
        asthma = request.GET.get('asthma')
        kidney = request.GET.get('kidney')
        skin_cancer = request.GET.get('skin_cancer')
        age = int(age)
        users_age=age
        if age >= 18 and age <= 24:
            age = 0
        elif age >= 25 and age <= 29:
            age = 1
        elif age >= 30 and age <= 34:
            age = 2
        elif age >= 35 and age <= 39:
            age = 3
        elif age >= 40 and age <= 44:
            age = 4
        elif age >= 45 and age <= 49:
            age = 5
        elif age >= 50 and age <= 54:
            age = 6
        elif age >= 55 and age <= 59:
            age = 7
        elif age >= 60 and age <= 64:
            age = 8
        elif age >= 65 and age <= 69:
            age = 9
        elif age >= 70 and age <= 74:
            age = 10
        elif age >= 75 and age <= 79:
            age = 11
        elif age >= 80:
            age = 12

        print('age:', age)
        print('users_age:', users_age)

        physical_health = float(physical_health)
        general_health = float(general_health)
        psychology = float(psychology)
        sleeping_time = float(sleeping_time)
        physical_health = (physical_health) / 10
        general_health = (general_health) / 4
        psychology = (psychology) / 10
        sleeping_time = (sleeping_time) / 24

        self.pred_list = [float(bmi),float(smoke),float(alcohol),float(stroke),
                     float(physical_health),float(psychology),
                    float(diff_walking),float(gender),float(age),float(ethnic_group),
                    float(diabetic),float(exercise),float(general_health),float(sleeping_time),
                    float(asthma),float(kidney),float(skin_cancer)]
        print('pred_list:', self.pred_list)

        result = self.calculate_prediction()
        result = result * 100
        print('result:', result)

        return JsonResponse(result, safe=False)


    def calculate_prediction(self):
        pred = self.pred_list
        pred = torch.FloatTensor(pred)
        model = nn.Sequential(
        nn.Linear(17, 64),
        nn.ReLU(),
        nn.Linear(64, 64),
        nn.ReLU(),
        nn.Linear(64, 1),
        nn.Sigmoid()
        )
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        pred = pred.to(device)
        model.load_state_dict(torch.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles', 'C_V_D_model_1.pt')))
        model.eval()
        with torch.no_grad():
            output = model(pred)
            print('output_1:', output)
            output = output.cpu()

            output = output.numpy()
            output = output.tolist()
            print('output_2:', output)
            output = output[0]
            print('output_results:', output)
            return output