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
            mebtal_care_record_count_today = MENTAL_HEALTH_PREDICTION_MODEL.objects.filter(user=user, created_at__date=today).count()
            if mental_care_record_count_yesterday <=0 :
                #check yesterday diery object count
                yesterday_diery_object = PERSONAL_DIARY.objects.filter(user=user, created_at__date=yesterday)
                yesterday_diery_object_count = yesterday_diery_object.count()
                if yesterday_diery_object_count > 0:
                    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                    tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
                    model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
                    all_prediction_objects_list = []
                    for object in yesterday_diery_object:
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
                        else:
                            continue

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
                        else:
                            continue
                        combined_prediction_dict={}
                        WEIGHT_OF_TITLE = 0.3
                        WEIGHT_OF_CONTENT = 0.7
                        if len(title_prediction_dict) > 0 and len(content_prediction_dict) > 0:
                            for key in title_prediction_dict.keys():
                                combined_prediction_dict[key] = (title_prediction_dict[key]*WEIGHT_OF_TITLE) + (content_prediction_dict[key]*WEIGHT_OF_CONTENT)
                        elif len(title_prediction_dict) > 0 and len(content_prediction_dict) <= 0:
                            combined_prediction_dict = title_prediction_dict
                        
                        all_prediction_objects_list.append(combined_prediction_dict)
                    for object in all_prediction_objects_list:
                        MENTAL_HEALTH_PREDICTION_MODEL.objects.create(user=user,admiration=object['admiration'],
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
            if mebtal_care_record_count_today <= 0:
                print("inside today")
                today = timezone.now().date()
                start_of_day = timezone.make_aware(timezone.datetime.combine(today, timezone.datetime.min.time()))
                end_of_day = start_of_day + timedelta(days=1)
                record_count_today = PERSONAL_DIARY.objects.filter(user=user, created_at__range=(start_of_day, end_of_day)).count()
                if record_count_today >= 10:
                    today_diery_object = PERSONAL_DIARY.objects.filter(user=user, created_at__date=today)
                    
                    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
                    tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
                    model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
                    all_prediction_objects_list = []
                    for object in today_diery_object:
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
                        else:
                            continue

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
                        else:
                            continue
                        combined_prediction_dict={}
                        WEIGHT_OF_TITLE = 0.3
                        WEIGHT_OF_CONTENT = 0.7
                        if len(title_prediction_dict) > 0 and len(content_prediction_dict) > 0:
                            for key in title_prediction_dict.keys():
                                combined_prediction_dict[key] = (title_prediction_dict[key]*WEIGHT_OF_TITLE) + (content_prediction_dict[key]*WEIGHT_OF_CONTENT)
                        elif len(title_prediction_dict) > 0 and len(content_prediction_dict) <= 0:
                            combined_prediction_dict = title_prediction_dict

                        all_prediction_objects_list.append(combined_prediction_dict)
                    for object in all_prediction_objects_list:
                        MENTAL_HEALTH_PREDICTION_MODEL.objects.create(user=user,admiration=object['admiration'],
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
            object_dict['admiration'] = object.admiration
            object_dict['amusement'] = object.amusement
            object_dict['anger'] = object.anger
            object_dict['annoyance'] = object.annoyance
            object_dict['approval'] = object.approval
            object_dict['caring'] = object.caring
            object_dict['confusion'] = object.confusion
            object_dict['curiosity'] = object.curiosity
            object_dict['desire'] = object.desire
            object_dict['disappointment'] = object.disappointment

            object_dict['disapproval'] = object.disapproval
            object_dict['disgust'] = object.disgust
            object_dict['embarrassment'] = object.embarrassment
            object_dict['excitement'] = object.excitement
            object_dict['fear'] = object.fear
            object_dict['gratitude'] = object.gratitude
            object_dict['grief'] = object.grief
            object_dict['joy'] = object.joy
            object_dict['love'] = object.love
            object_dict['nervousness'] = object.nervousness
            object_dict['optimism'] = object.optimism
            object_dict['pride'] = object.pride
            object_dict['realization'] = object.realization
            object_dict['relief'] = object.relief
            object_dict['remorse'] = object.remorse
            object_dict['sadness'] = object.sadness
            object_dict['surprise'] = object.surprise
            object_dict['neutral'] = object.neutral
            all_prediction_objects_list.append(object_dict)

            print(all_prediction_objects_list)

        return render(request, 'mental_health_prediction.html', {'all_prediction_objects_list':all_prediction_objects_list})

                        
                            




