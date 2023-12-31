from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , addrecord , VenueForm , EventForm , OCRImageForm,Mail_me_Form,profilepicForm,SocialMediaForm,ChangePasswordForm,MedicineForm,PERSONAL_DIARY_FORM
from . models import Record , Event , EventVenue , EventAttendee , RecordImage,Record_mail_me,SocialMedia,Medication,MedicationDetails,PERSONAL_DIARY
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
from .madication_chat import MEDICINE_CHAT
from .presciption_classification_beta import PRESCIPTION_CLASSIFICATION_BETA
from .C_V_D_prediction import C_V_D_PREDICTION
from .mental_health_prediction import MENTAL_HEALTH
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .phenomonia_prediction import PHENOMONIA_PREDICTION_CLASS


def trial(request):
    return render(request, 'trial.html')


def about(request):
    about_me = 'KNOW ABOUT ME'
    return render(request, 'about.html',{'about_me': about_me})


def logout_user(request):
    logout(request)
    return redirect('index_new')



def login_register(request):
    if request.method == 'GET':
        return render(request, 'new_login_reg.html')  # Display the form for GET requests

    elif request.method == 'POST':
        if 'name' in request.POST:
            username = request.POST['name']
            print('username',username)
            password = request.POST['password']
            
            # Check if user has entered correct credentials
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('index_new')
            else:
                messages.error(request, 'Error logging in, please try again')
                return redirect('login_register')
        
        elif 'username' in request.POST:  # Assuming the username field is in your RegisterForm
            register_form = RegisterForm(request.POST)
            
            if register_form.is_valid():
                user = register_form.save()  # Save the user object
                username = register_form.cleaned_data.get('username')
                password = register_form.cleaned_data.get('password1')
                # Authenticate
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You have registered successfully! Complete your profile by updating details and profile picture.")
                return redirect('add_or_update_profile_picture')
            else:
                messages.error(request, "Registration error, please try again")
                return render(request, 'new_login_reg.html', {'register_form': register_form})
        else:
            messages.error(request, "Invalid form submission")
            return render(request, 'new_login_reg.html')  # Handle other cases
        
    return render(request, 'new_login_reg.html')  # Handle other HTTP methods









def index_new(request):
    return render(request, 'index_new.html')


def C_V_D_prediction(request):
    return render(request, 'C_V_D_prediction.html')


def main_bmi_calculator(request):
    return render(request, 'main_bmi_calculator.html')

def get_C_V_D_prediction(request):
    C_V_D_PREDICTION_ = C_V_D_PREDICTION(request=request)
    return C_V_D_PREDICTION_.get_C_V_D_prediction()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def phenomonia_prediction(request): 
    PHENOMONIA_PREDICTION=PHENOMONIA_PREDICTION_CLASS(request=request)
    return PHENOMONIA_PREDICTION.phenomonia_prediction()


def med_search(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.med_search()

def med_search_generic(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.med_search_generic()

def get_generic_medication_details(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.get_generic_medication_details()


def get_medication_details(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.get_medication_details()


def med_search_results(request):
    return render(request, 'search_results.html')

def med_details_search_results(request):
    return render(request, 'search_med_details_results.html')


def get_medicine_details(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.get_medicine_details()

   

def medicine_details(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.medicine_details()

def medicine_details_generic(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.medicine_details_generic()

def get_medicine_details_generic(request):
    T_M_S = TOTAL_MEDICINE_SEARCH(request=request)
    return T_M_S.get_medicine_details_generic()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def personal_diary_input(request):
    MENTAL_HEALTH_ = MENTAL_HEALTH(request=request)
    return MENTAL_HEALTH_.personal_diary_input()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def predict_mental_health(request):
    MENTAL_HEALTH_ = MENTAL_HEALTH(request=request)
    return MENTAL_HEALTH_.predict_mental_health()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def get_diery_objects(request):
    MENTAL_HEALTH_ = MENTAL_HEALTH(request=request)
    return MENTAL_HEALTH_.get_diery_objects()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def edit_diery_objects(request):
    MENTAL_HEALTH_ = MENTAL_HEALTH(request=request)
    return MENTAL_HEALTH_.edit_diery_objects()

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def update_diery_objects(request):
    MENTAL_HEALTH_ = MENTAL_HEALTH(request=request)
    return MENTAL_HEALTH_.update_diery_objects()


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

def get_generic_name_recommendations(request):
    if request.method == 'GET':
        input_query = request.GET.get('input', '').strip()
        unique_generic_names_txt = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'staticfiles', 'unique_generic_name_list.txt')

        with open(unique_generic_names_txt, 'r') as f:
            unique_generic_names = f.readlines()
        unique_generic_names = [x.replace('\n', '') for x in unique_generic_names]
        # Filter word_list based on the input_query
        generic_name_recommendations = [word for word in unique_generic_names if word.lower().startswith(input_query.lower())]

        return JsonResponse(generic_name_recommendations, safe=False)




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



def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Password Has Been Changed Successfully!")
            return redirect('index_new')
        else:
            messages.error(request, "Please Correct The Error Below")
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_password.html', {'change_password_form': form})




@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def base_handwritten(request):
    return render(request, 'base_handwritten.html')

@login_required(login_url='/login_register/')  # Redirect to LOGIN_URL if user is not logged in
def base_ocr(request):
    return render(request, 'base_ocr.html')


def projects(request):
    return render(request, 'projects.html')


def hire_me(request):
    return render(request, 'hire_me.html')



def ENG_OCR_HANDWRITTEN(request):
    ENGLISH_OCR = ENGOCR()
    return ENGLISH_OCR.eng_ocr_handwritten(request)


def ENG_TEXT_HANDWRITTEN(request):
    ENGLISH_OCR = ENGOCR()
    return ENGLISH_OCR.eng_text_to_handwritten(request)



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
            return redirect('index_new')  # Change 'real' to 'index'
        else:
            # print(form.errors)
            messages.error(request, "There was an error in your form submission.")
    else:
        form = Mail_me_Form()
    
    return render(request, 'trial.html', {'send_message_form': form})


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











def delete_record(request):
    record = Record.objects.filter(user=request.user).first()
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('real')






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