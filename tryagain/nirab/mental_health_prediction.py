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
from django.core.serializers.json import DjangoJSONEncoder

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
        all_mental_prediction_objects = MENTAL_HEALTH_PREDICTION_MODEL.objects.filter(user=user) 
        all_mental_prediction_objects_list = []
        for object in all_mental_prediction_objects:
            all_mental_prediction_objects_list.append(object.id)
        all_diery_objects = PERSONAL_DIARY.objects.filter(user=user)
        all_diery_objects_id_list = []
        for object in all_diery_objects:
            all_diery_objects_id_list.append(object.id)
        print('all_diery_objects_id_list',all_diery_objects_id_list)
        print('all_mental_prediction_objects_list',all_mental_prediction_objects_list)
        # Convert elements in all_diery_objects_id_list to strings
        all_diery_objects_id_list_str = list(map(str, all_diery_objects_id_list))

        # Find the common elements
        common_elements = list(set(all_diery_objects_id_list_str).intersection(all_mental_prediction_objects_list))
        print('common_elements', common_elements)

        # Convert common_elements back to integers
        common_elements_int = list(map(int, common_elements))

        # Find elements not available in all_mental_prediction_objects_list
        not_available_in_mental_prediction_objects_list = list(set(all_diery_objects_id_list) - set(common_elements_int))
        print('not_available_in_mental_prediction_objects_list', not_available_in_mental_prediction_objects_list)
        if len(not_available_in_mental_prediction_objects_list) >=1:
            device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
            tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
            model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
            for id in not_available_in_mental_prediction_objects_list:
                object = get_object_or_404(PERSONAL_DIARY, id=id)
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
                        prediction_value = label_id.item()     
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

                        title_prediction_dict[label] = prediction_value

                combined_prediction_dict={}
                WEIGHT_OF_TITLE = 0.3
                WEIGHT_OF_CONTENT = 0.7
                if len(title_prediction_dict) > 0 and len(content_prediction_dict) > 0:
                    for key in title_prediction_dict.keys():
                        combined_prediction_dict[key] = (title_prediction_dict[key]*WEIGHT_OF_TITLE) + (content_prediction_dict[key]*WEIGHT_OF_CONTENT)
                elif len(title_prediction_dict) > 0 and len(content_prediction_dict) <= 0:
                    combined_prediction_dict = title_prediction_dict

                MENTAL_HEALTH_PREDICTION_MODEL.objects.create(user=user,admiration=combined_prediction_dict['admiration'],id=id,
                                                                  amusement = combined_prediction_dict['amusement'],anger = combined_prediction_dict['anger'],
                                                                    annoyance = combined_prediction_dict['annoyance'],approval = combined_prediction_dict['approval'],
                                                                    caring = combined_prediction_dict['caring'],confusion = combined_prediction_dict['confusion'],
                                                                    curiosity = combined_prediction_dict['curiosity'],desire = combined_prediction_dict['desire'],
                                                                    disappointment = combined_prediction_dict['disappointment'],disapproval = combined_prediction_dict['disapproval'],
                                                                    disgust = combined_prediction_dict['disgust'],embarrassment = combined_prediction_dict['embarrassment'],
                                                                    excitement = combined_prediction_dict['excitement'],fear = combined_prediction_dict['fear'],
                                                                    gratitude = combined_prediction_dict['gratitude'],grief = combined_prediction_dict['grief'],
                                                                    joy = combined_prediction_dict['joy'],love = combined_prediction_dict['love'],
                                                                    nervousness = combined_prediction_dict['nervousness'],optimism = combined_prediction_dict['optimism'],
                                                                    pride = combined_prediction_dict['pride'],realization = combined_prediction_dict['realization'],
                                                                    relief = combined_prediction_dict['relief'],remorse = combined_prediction_dict['remorse'],
                                                                    sadness = combined_prediction_dict['sadness'],surprise = combined_prediction_dict['surprise'],
                                                                    neutral = combined_prediction_dict['neutral'])
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
        all_prediction_objects_list = dumps(all_prediction_objects_list)

        return render(request, 'mental_health_prediction.html', {'all_prediction_objects_list':all_prediction_objects_list})
    



    def get_diery_objects(self):
        request = self.request
        user = self.user
        all_diery_objects = PERSONAL_DIARY.objects.filter(user=user)
        all_diery_objects_list = []
        
        for obj in all_diery_objects:
            object_dict = {
                'id': obj.id,
                'title': obj.title,
                'content': obj.content,
                'created_at': obj.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Convert datetime to string
            }
            all_diery_objects_list.append(object_dict)

        print('all_diery_objects_list', all_diery_objects_list)
        
        # Serialize the list of dictionaries to JSON
        all_diery_objects_list_json = dumps(all_diery_objects_list, cls=DjangoJSONEncoder)
        
        return render(request, 'mental_health_prediction.html', {'all_diery_objects_list': all_diery_objects_list_json})
    
    def edit_diery_objects(self):
        request = self.request
        user = self.user
        if request.method == 'GET':
            id = request.GET.get('id')
            print('id',id)
            if id:
                object = get_object_or_404(PERSONAL_DIARY, id=id)
                editable_title = object.title
                editable_content = object.content
                print('editable_title',editable_title)
                print('editable_content',editable_content)
                return render(request, 'mental_health_prediction.html', {'editable_title':editable_title,'editable_content':editable_content,'noneditable_id':id})
            else:
                return render(request, 'mental_health_prediction.html')
        else:
            return render(request, 'mental_health_prediction.html')
        

    def update_diery_objects(self):
        request = self.request
        user = self.user
        if request.method == 'POST':
            id = request.POST.get('id')
            title = request.POST.get('title')
            content = request.POST.get('content')
            print('id',id)
            print('title',title)
            print('content',content)
            if id:
                object = get_object_or_404(PERSONAL_DIARY, id=id)
                object.title = title
                object.content = content
                object.save()
                return redirect('get_diery_objects')
            else:
                return render(request, 'mental_health_prediction.html')
        else:
            return render(request, 'mental_health_prediction.html')