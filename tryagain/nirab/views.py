from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , addrecord , VenueForm , EventForm , OCRImageForm,Mail_me_Form,profilepicForm,BlogForm,SocialMediaForm,ChangePasswordForm,MedicineForm
from . models import Record , Event , EventVenue , EventAttendee , RecordImage,Record_mail_me,Post,SocialMedia,Medication,MedicationDetails,Classify_Drug_Class
import datetime
import calendar
from calendar import HTMLCalendar
import time
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from PIL import Image
from .bangla_ocr import BanglaOCR
from .eng_ocr import ENGOCR
from .med_search import TOTAL_MEDICINE_SEARCH
import os
from django.http import FileResponse,HttpResponse
from .templatetags.custom_filters import add_or_update_social_media
from .ADD_OR_UPDATE_RECORD import ADD_OR_UPDATE_record
from django.http import JsonResponse
from .presciption_classification import PRESCIPTION_CLASSIFICATION
from .madication_chat import MEDICINE_CHAT
from .presciption_classification_beta import PRESCIPTION_CLASSIFICATION_BETA



def med_search(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.med_search()




def get_medication_details(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.get_medication_details()


def med_search_results(request):
    return render(request, 'search_results.html')

def med_details_search_results(request):
    return render(request, 'search_med_details_results.html')


def get_medicine_details(request):
    name = request.GET.get('name')
    name = name.lower()
    generic_name = Medication.objects.filter(name=name).first()
    if generic_name:
        details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name.generic_name)
        if details_of_medicine.exists():
            details_list = []
            for detail in details_of_medicine:
                details = {
                    'generic_name': detail.generic_name,
                    'drug_class': detail.drug_class,
                    'indication': detail.indication,
                    'indication_description': detail.indication_description,
                    'therapeutic_class_description': detail.therapeutic_class_description,
                    'pharmacology_description': detail.pharmacology_description,
                    'dosage_description': detail.dosage_description,
                    'interaction_description': detail.interaction_description,
                    'contraindications_description': detail.contraindications_description,
                    'side_effects_description': detail.side_effects_description,
                }
                details_list.append(details)
            return JsonResponse(details_list, safe=False)
        else:
            return JsonResponse({'error': 'Medication details not found'}, status=404)
    else:
        return JsonResponse({'error': 'Medication not found'}, status=404)
    

def medicine_details(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.lower()
            return render(request, 'search_med_details.html', {'medication_form': form, 'name_of_medication': name})
    else:
        form = MedicineForm()
    return render(request, 'search_med_details.html', {'medication_form': form})









def medicine_chatbot(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.lower()
            return render(request, 'medicine_chatbot.html', {'medicine_chatbot_form': form, 'name_of_medication': name})
    else:
        form = MedicineForm()
    return render(request, 'medicine_chatbot.html', {'medicine_chatbot_form': form})


def get_medicine_chat(request):
    MEDICINE_CHATBOT = MEDICINE_CHAT(request=request)
    return MEDICINE_CHATBOT.get_medicine_details()




def get_word_recommendations(request):
    if request.method == 'GET':
        input_query = request.GET.get('input', '').strip()
        unique_names_txt = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles', 'unique_names.txt')

        with open(unique_names_txt, 'r') as f:
            unique_names = f.readlines()
        unique_names = [x.replace('\n', '') for x in unique_names]
        # Filter word_list based on the input_query
        word_recommendations = [word for word in unique_names if word.lower().startswith(input_query.lower())]

        return JsonResponse(word_recommendations, safe=False)








def get_presciption_classification(request):
    PRESCIPTION_classification = PRESCIPTION_CLASSIFICATION(request=request)
    return PRESCIPTION_classification.get_presciption_classification()



def presciption_classification(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.lower()
            return render(request, 'presciption_classification.html', {'medication_form': form, 'name_of_medication': name})
    else:
        form = MedicineForm()
    return render(request, 'presciption_classification.html', {'medication_form': form})


def presciption_classification_beta(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            name = name.lower()
            return render(request, 'presciption_classification_beta.html', {'medication_form': form, 'name_of_medication': name})
    else:
        form = MedicineForm()
    return render(request, 'presciption_classification_beta.html', {'medication_form': form})





def get_presciption_classification_beta(request):
    PRESCIPTION_classification = PRESCIPTION_CLASSIFICATION_BETA(request=request)
    return PRESCIPTION_classification.get_presciption_classification()

def presciption_classification_beta_results(request):
    return render(request, 'presciption_classification_beta_results.html')

def search_medication_chatbot_results(request):
    return render(request, 'search_medication_chatbot_results.html')


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Password Has Been Changed Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please Correct The Error Below")
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'add_or_update_record.html', {'change_password_form': form})





def base_handwritten(request):
    return render(request, 'base_handwritten.html')

def base_ocr(request):
    return render(request, 'base_ocr.html')


def projects(request):
    return render(request, 'projects.html')


def hire_me(request):
    return render(request, 'hire_me.html')


def about(request):
    return render(request, 'about.html')




def apps(request):
    i_c_record = RecordImage.objects.filter(user=request.user).first()
    if i_c_record:
        return render(request, 'apps.html', {'i_c_record': i_c_record})
    else:
        return render(request, 'apps.html')






def ENG_OCR_HANDWRITTEN(request):
    ENGLISH_OCR = ENGOCR()
    return ENGLISH_OCR.eng_ocr_handwritten(request)





def download_pdf(request, pdf_path):
    with open(pdf_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(pdf_path)}'
        return response



def download_text(request, text_path):
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    response = HttpResponse(text, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={os.path.basename(text_path)}'
    return response



def dashboard(request):
    return render(request, 'dashboard.html')
    


def view_record(request):
    record = Record.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'record': record})



def index(request):
    return render(request, 'index.html')



def save_mail_form(request):
    if request.method == 'POST':
        form = Mail_me_Form(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Record Has Been Saved Successfully!")
            return redirect('index')  # Change 'real' to 'index'
        else:
            print(form.errors)
            messages.error(request, "There was an error in your form submission.")
    else:
        form = Mail_me_Form()
    
    return render(request, 'index.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def real(request):
    current_year = datetime.now().year
    current_month = datetime.now().strftime('%B')
    return render(request, 'real.html', {'current_year': current_year, 'current_month': current_month})



def event(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    
    # Fetch all events for the given year and month
    events = Event.objects.filter(date__year=year, date__month=month_number)

    return render(request, 'event.html', {'month': month, 'year': year, 'cal': cal, 'now': now, 'month_events': events})




def login_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('profile')
        else:
            messages.success(request, 'Error logging in, please try again')
            return redirect('login_user')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')



def register_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			# Authenticate
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Registered Successfully! compleate by updating details and profile picture PLEASE")
			return redirect('add_or_update_profile_picture')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})




def delete_record(request):
    record = Record.objects.filter(user=request.user).first()
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('real')




def bangla_ocr(request):
    return render(request, 'bangla_ocr.html')



def BN_OCR(request):
    BANGLA_OCR = BanglaOCR()
    return BANGLA_OCR.add_image(request)

def ENG_OCR(request):
    ENGLISH_OCR = ENGOCR()
    return ENGLISH_OCR.add_image(request)




def add_event(request):
    if request.method == 'POST':
        venue_form = VenueForm(request.POST, prefix='venue')
        event_form = EventForm(request.POST, prefix='event')

        if event_form.is_valid() and venue_form.is_valid():
            venue = venue_form.save()
            event = event_form.save(commit=False)
            event.venue = venue
            event.save()
            messages.success(request, 'Event and Venue Successfully Added')
            return redirect('real')

        elif event_form.is_valid():
            event = event_form.save(commit=False)
            event.save()
            messages.success(request, 'Event Added Successfully')
            return redirect('real')

        elif venue_form.is_valid():
            venue = venue_form.save()
            messages.success(request, 'Venue Added Successfully')
            return redirect('real')

        else:
            messages.error(request, 'Invalid Data. Please try again.')
    else:
        venue_form = VenueForm(prefix='venue')
        event_form = EventForm(prefix='event', initial={'date': datetime.now().date(), 'time': datetime.now().time()})

    return render(request, 'event_catalogue.html', {'venue_form': venue_form, 'event_form': event_form})




def join_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    record, created = Record.objects.get_or_create(user=request.user)
    attendee, attendee_created = EventAttendee.objects.get_or_create(record=record)
    attendee.event.add(event)
    if created:
        messages.success(request, 'You have joined the event')
    else:
        messages.warning(request, 'You are already registered for this event')
    return redirect('real')


def leave_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    record = Record.objects.filter(user=request.user).first()
    attendee = EventAttendee.objects.filter(record=record).first()
    attendee.event.remove(event)
    messages.success(request, 'You have left the event')
    return redirect('real')







def profile(request):
    return render(request, 'profile.html')






def profile_picture(request):
    record = Record.objects.filter(user=request.user).first()
    form = profilepicForm(request.POST, request.FILES, instance=record)    
    if record:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Your Record Has Been Saved Successfully!")
                return redirect('profile')
    else:
        form = profilepicForm(instance=record)
    
    return render(request, 'dashboard.html', {'profile_picture_form': form})


def add_or_update_profile_picture(request):
    record = Record.objects.filter(user=request.user).first()
    form = profilepicForm(request.POST, request.FILES, instance=record)

    if record and record.photo:  # Check if record exists and if photo is not None
        photo_url = record.photo.url if record.photo else None

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Your Record Has Been Saved Successfully!")
                return redirect('profile')
        else:
            form = profilepicForm(instance=record)

        return render(request, 'add_or_update_record.html', {'add_or_update_profile_picture_form': form, 'photo_url': photo_url})
    else:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Your Record Has Been Saved Successfully!")
                return redirect('profile')
        else:
            form = profilepicForm(instance=record)

        return render(request, 'add_or_update_record.html', {'add_or_update_profile_picture_form': form})


def add_or_update_record(request):
    ADD_OR_update_record = ADD_OR_UPDATE_record(request=request)
    return ADD_OR_update_record.add_or_update_record()