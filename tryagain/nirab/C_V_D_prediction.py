from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse



class C_V_D_PREDICTION():
    def __init__(self, request):
        self.request = request


    def get_C_V_D_prediction(self):
        request = self.request
        gender = request.GET.get('gender')
        print('gender:', gender)

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
        #print all the data
        print('bmi:', bmi)
        print('ethnic_group:', ethnic_group)
        print('age:', age)
        print('alcohol:', alcohol)
        print('smoke:', smoke)
        print('exercise:', exercise)
        print('psychology:', psychology)
        print('sleeping_time:', sleeping_time)
        print('stroke:', stroke)
        print('physical_health:', physical_health)
        print('general_health:', general_health)
        print('diff_walking:', diff_walking)
        print('diabetic:', diabetic)
        print('asthma:', asthma)
        print('kidney:', kidney)
        print('skin_cancer:', skin_cancer)



