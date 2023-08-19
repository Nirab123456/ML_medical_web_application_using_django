from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PERSONAL_DIARY_FORM
from . models import PERSONAL_DIARY,MENTAL_HEALTH_PREDICTION_MODEL
from django.shortcuts import get_object_or_404
import os
from django.http import FileResponse,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import re 
from json import dumps
# Load tokenizer and model


class MENTAL_HEALTH:
    def __init__(self, request):
        self.request = request
        self.user = request.user

    def personal_diary_input(self):
        request = self.request
        user=self.user
        
        # Calculate the date range for the current day
        today = timezone.now().date()
        start_of_day = timezone.make_aware(timezone.datetime.combine(today, timezone.datetime.min.time()))
        end_of_day = start_of_day + timedelta(days=1)
        
        # Count the number of records created by the user today
        record_count_today = PERSONAL_DIARY.objects.filter(user=user, created_at__range=(start_of_day, end_of_day)).count()
        
        if record_count_today <= 10:  # Set your desired daily limit here (e.g., 3 records)
            if request.method == 'POST':
                form = PERSONAL_DIARY_FORM(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    content = form.cleaned_data['content']
                    PERSONAL_DIARY.objects.create(user=user,title=title,content=content)
                    count = PERSONAL_DIARY.objects.filter(user=user).count()
                    count = count + 1
                    messages.success(request, "Your Record Has Been Saved Successfully!")
                    return render(request, 'mental_health_prediction.html', {'personal_diery_form': form,'personal_instance_count':count,'record_count_today':record_count_today})

            else:
                form = PERSONAL_DIARY_FORM()
                user = request.user
                count = PERSONAL_DIARY.objects.filter(user=user).count()
                count = count + 1
            return render(request, 'mental_health_prediction.html', {'personal_diery_form': form,'personal_instance_count':count,'record_count_today':record_count_today})
        else:
            messages.error(request, "You have reached your daily limit of 10 records")
            return render(request, 'mental_health_prediction.html', {'record_count_today':record_count_today})


    def predict_mental_health(self):
        request = self.request
        user=self.user
        if request.method == 'GET':
            yesterday = timezone.now().date() - timedelta(days=1)
            today = timezone.now().date()

            # check if the user has created a record yesterday
            mental_care_record_count_yesterday = MENTAL_HEALTH_PREDICTION_MODEL.objects.filter(user=user, created_at__date=yesterday).count()
            print('mental_care_record_count_yesterday',mental_care_record_count_yesterday)
            mebtal_care_record_count_today = MENTAL_HEALTH_PREDICTION_MODEL.objects.filter(user=user, created_at__date=today).count()
            print('mebtal_care_record_count_today',mebtal_care_record_count_today)
            if mental_care_record_count_yesterday == 0 :
                #check yesterday diery object count
                yesterday_diery_object = PERSONAL_DIARY.objects.filter(user=user, created_at__date=yesterday)
                yesterday_diery_object_count = yesterday_diery_object.count()
                print('yesterday_diery_object_count',yesterday_diery_object_count)
                if yesterday_diery_object_count > 0:
                    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                    tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
                    model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
                    all_prediction_objects_list = []
                    for object in yesterday_diery_object:
                        id = object.id
                        title = object.title
                        content = object.content
                        title_prediction_dict={}
                        content_prediction_dict={}
                        if content :
                            input_text = content
                            input_text = input_text.lower()
                            input_text = input_text.replace('\n', '')
                            input_text = re.sub(r'[^\w\s,.\-?!]', '', input_text)
                            inputs = tokenizer(input_text, return_tensors="pt")
                            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                            model.to(device)
                            inputs.to(device)
                            with torch.no_grad():
                                outputs = model(**inputs)
                            logits = outputs.logits 
                            probabilities = F.softmax(logits, dim=1)

                            for i, label_id in enumerate(probabilities[0]):
                                label = model.config.id2label[i]
                                prediction_value = label_id.item()  # Convert tensor to float
                                # #take upto 2 decimal points
                                # prediction_value = round(prediction_value, 2)
                                content_prediction_dict[label] = prediction_value



                        if title:
                            input_text = title
                            input_text = input_text.lower()
                            input_text = input_text.replace('\n', '')
                            input_text = re.sub(r'[^\w\s,.\-?!]', '', input_text)
                            inputs = tokenizer(input_text, return_tensors="pt")
                            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                            model.to(device)
                            inputs.to(device)
                            with torch.no_grad():
                                outputs = model(**inputs)
                            logits = outputs.logits 
                            probabilities = F.softmax(logits, dim=1)

                            for i, label_id in enumerate(probabilities[0]):
                                label = model.config.id2label[i]
                                prediction_value = label_id.item()

                                # #take upto 2 decimal points
                                # prediction_value = round(prediction_value, 2)
                                title_prediction_dict[label] = prediction_value

                        combined_prediction_dict={}
                        WEIGHT_OF_TITLE = 0.3
                        WEIGHT_OF_CONTENT = 0.7
                        if len(title_prediction_dict) > 0 and len(content_prediction_dict) > 0:
                            for key in title_prediction_dict.keys():
                                combined_prediction_dict[key] = (title_prediction_dict[key]*WEIGHT_OF_TITLE) + (content_prediction_dict[key]*WEIGHT_OF_CONTENT)


                        elif len(title_prediction_dict) > 0 and len(content_prediction_dict) <= 0:
                            combined_prediction_dict = title_prediction_dict

                        combined_prediction_dict['id'] = id

                        all_prediction_objects_list.append(combined_prediction_dict)
                    for object in all_prediction_objects_list:
                        print('yesterday_object_length',len(object))
                        MENTAL_HEALTH_PREDICTION_MODEL.objects.create(user=user,admiration=object['admiration'],id=object['id'],
                                                                    amusement = object['amusement'],anger = object['anger'],
                                                                    annoyance = object['annoyance'],approval = object['approval'],
                                                                    caring = object['caring'],confusion = object['confusion'],
                                                                    curiosity = object['curiosity'],desire = object['desire'],
                                                                    disappointment = object['disappointment'],disapproval = object['disapproval'],
                                                                    disgust = object['disgust'],embarrassment = object['embarrassment'],
                                                                    excitement = object['excitement'],fear = object['fear'],
                                                                    gratitude = object['gratitude'],grief = object['grief'],
                                                                    joy = object['joy'],love = object['love'],
                                                                    nervousness = object['nervousness'],optimism = object['optimism'],
                                                                    pride = object['pride'],realization = object['realization'],
                                                                    relief = object['relief'],remorse = object['remorse'],
                                                                    sadness = object['sadness'],surprise = object['surprise'],
                                                                    neutral = object['neutral'])
            if mebtal_care_record_count_today == 0:
                print('inside today')
                today = timezone.now().date()
                start_of_day = timezone.make_aware(timezone.datetime.combine(today, timezone.datetime.min.time()))
                end_of_day = start_of_day + timedelta(days=1)
                record_count_today = PERSONAL_DIARY.objects.filter(user=user, created_at__range=(start_of_day, end_of_day)).count()
                if record_count_today >= 9:
                    print('inside record count')
                    today_diery_object = PERSONAL_DIARY.objects.filter(user=user, created_at__date=today)
                    print('len(today_diery_object)',len(today_diery_object))
                    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                    tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
                    model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
                    all_prediction_objects_list = []
                    for object in today_diery_object:
                        print('inside today_diery_object')
                        id = object.id
                        title = object.title
                        content = object.content
                        title_prediction_dict={}
                        content_prediction_dict={}
                        if content :
                            input_text = content
                            input_text = input_text.lower()
                            input_text = input_text.replace('\n', '')
                            input_text = re.sub(r'[^\w\s,.\-?!]', '', input_text)
                            inputs = tokenizer(input_text, return_tensors="pt")
                            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                            model.to(device)
                            inputs.to(device)
                            with torch.no_grad():
                                outputs = model(**inputs)
                            logits = outputs.logits 
                            probabilities = F.softmax(logits, dim=1)

                            for i, label_id in enumerate(probabilities[0]):
                                label = model.config.id2label[i]
                                prediction_value = label_id.item()  # Convert tensor to float
                                # #take upto 2 decimal points
                                # prediction_value = round(prediction_value, 2)
                                content_prediction_dict[label] = prediction_value


                        if title:
                            input_text = title
                            input_text = input_text.lower()
                            input_text = input_text.replace('\n', '')
                            input_text = re.sub(r'[^\w\s,.\-?!]', '', input_text)
                            inputs = tokenizer(input_text, return_tensors="pt")
                            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                            model.to(device)
                            inputs.to(device)
                            with torch.no_grad():
                                outputs = model(**inputs)
                            logits = outputs.logits 
                            probabilities = F.softmax(logits, dim=1)

                            for i, label_id in enumerate(probabilities[0]):
                                label = model.config.id2label[i]
                                prediction_value = label_id.item()

                                # #take upto 2 decimal points
                                # prediction_value = round(prediction_value, 2)
                                title_prediction_dict[label] = prediction_value

                        combined_prediction_dict={}
                        WEIGHT_OF_TITLE = 0.3
                        WEIGHT_OF_CONTENT = 0.7
                        if len(title_prediction_dict) > 0 and len(content_prediction_dict) > 0:
                            for key in title_prediction_dict.keys():
                                combined_prediction_dict[key] = (title_prediction_dict[key]*WEIGHT_OF_TITLE) + (content_prediction_dict[key]*WEIGHT_OF_CONTENT)
                        elif len(title_prediction_dict) > 0 and len(content_prediction_dict) <= 0:
                            combined_prediction_dict = title_prediction_dict

                        combined_prediction_dict['id'] = id
                    

                        all_prediction_objects_list.append(combined_prediction_dict)


                    for object in all_prediction_objects_list:
                        print('today_object_length',len(object))
                        MENTAL_HEALTH_PREDICTION_MODEL.objects.create(user=user,admiration=object['admiration'],id=object['id'],
                                                                    amusement = object['amusement'],anger = object['anger'],
                                                                    annoyance = object['annoyance'],approval = object['approval'],
                                                                    caring = object['caring'],confusion = object['confusion'],
                                                                    curiosity = object['curiosity'],desire = object['desire'],
                                                                    disappointment = object['disappointment'],disapproval = object['disapproval'],
                                                                    disgust = object['disgust'],embarrassment = object['embarrassment'],
                                                                    excitement = object['excitement'],fear = object['fear'],
                                                                    gratitude = object['gratitude'],grief = object['grief'],
                                                                    joy = object['joy'],love = object['love'],
                                                                    nervousness = object['nervousness'],optimism = object['optimism'],
                                                                    pride = object['pride'],realization = object['realization'],
                                                                    relief = object['relief'],remorse = object['remorse'],
                                                                    sadness = object['sadness'],surprise = object['surprise'],
                                                                    neutral = object['neutral'])
                        
        #get all prediction objects of a user
        all_prediction_objects = MENTAL_HEALTH_PREDICTION_MODEL.objects.filter(user=user)
        all_prediction_objects_list = []
        for object in all_prediction_objects:
            object_dict = {}
            object_dict['id'] = object.id
            object_dict['admiration'] = round(float(object.admiration), 3)
            object_dict['amusement'] = round(float(object.amusement), 3)
            object_dict['anger'] = round(float(object.anger), 3)
            object_dict['annoyance'] = round(float(object.annoyance), 3)
            object_dict['approval'] = round(float(object.approval), 3)
            object_dict['caring'] = round(float(object.caring), 3)
            object_dict['confusion'] = round(float(object.confusion), 3)
            object_dict['curiosity'] = round(float(object.curiosity), 3)
            object_dict['desire'] = round(float(object.desire), 3)
            object_dict['disappointment'] = round(float(object.disappointment), 3)

            object_dict['disapproval'] = round(float(object.disapproval), 3)
            object_dict['disgust'] = round(float(object.disgust), 3)
            object_dict['embarrassment'] = round(float(object.embarrassment), 3)
            object_dict['excitement'] = round(float(object.excitement), 3)
            object_dict['fear'] = round(float(object.fear), 3)
            object_dict['gratitude'] = round(float(object.gratitude), 3)
            object_dict['grief'] = round(float(object.grief), 3)
            object_dict['joy'] = round(float(object.joy), 3)
            object_dict['love'] = round(float(object.love), 3)
            object_dict['nervousness'] = round(float(object.nervousness), 3)
            object_dict['optimism'] = round(float(object.optimism), 3)
            object_dict['pride'] = round(float(object.pride), 3)
            object_dict['realization'] = round(float(object.realization), 3)
            object_dict['relief'] = round(float(object.relief), 3)
            object_dict['remorse'] = round(float(object.remorse), 3)
            object_dict['sadness'] = round(float(object.sadness), 3)
            object_dict['surprise'] = round(float(object.surprise), 3)
            object_dict['neutral'] = round(float(object.neutral), 3)
            all_prediction_objects_list.append(object_dict)
            
        print('all_objectsssssssssssssss',all_prediction_objects_list)
        all_prediction_objects_list = dumps(all_prediction_objects_list)

        return render(request, 'mental_health_prediction.html', {'all_prediction_objects_list':all_prediction_objects_list})

                        
                            




