from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , addrecord , VenueForm , EventForm , OCRImageForm
from . models import Record , Event , EventVenue , EventAttendee , RecordImage
import datetime
import calendar
from calendar import HTMLCalendar
import time
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from PIL import Image
from .bangla_ocr import BanglaOCR
import os
from django.http import FileResponse,HttpResponse


def index(request):
    return render(request, 'index.html')



def home(request):
    current_year = datetime.now().year
    current_month = datetime.now().strftime('%B')
    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month})

def real(request):
    return render(request,'real.html')

def event(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    
    # Fetch all events for the given year and month
    events = Event.objects.filter(date__year=year, date__month=month_number)

    return render(request, 'event.html', {'month': month, 'year': year, 'cal': cal, 'now': now, 'month_events': events})

def all_events(request):
    all_events = Event.objects.all()
    return render(request, 'event.html', {'all_events_list': all_events})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('real')
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
			messages.success(request, "You Have Registered Successfully!")
			return redirect('real')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})


def user_profile(request):
    return render(request, 'user_profile.html')

def view_record(request):
    record = Record.objects.filter(user=request.user).first()
    print(record)

    return render(request, 'record.html', {'record': record})


def delete_record(request):
    record = Record.objects.filter(user=request.user).first()
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('real')



def add_record(request):

    existing_record = Record.objects.filter(user=request.user).exists()

    if existing_record:
        return redirect('real')  # Redirect to the record list page or show an error message
    else:
        if request.method == 'POST':
            form = addrecord(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user  # Set the current logged-in user as the user
                record.save()
                messages.success(request, 'Record Added Successfully')
                return redirect('real')  # Redirect to the record list page
        else:
            form = addrecord()
        
        return render(request, 'add_record.html', {'form': form})

def bangla_ocr(request):
    return render(request, 'bangla_ocr.html')


BANGLA_OCR = BanglaOCR()
def add_image(request):
    return BANGLA_OCR.add_image(request)


def download_text(request, text_path):
    with open(text_path, 'r', encoding='utf-8') as file:
        text = file.read()

    response = HttpResponse(text, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={os.path.basename(text_path)}'
    return response


def get_ocr(request):
    if request.method == 'POST':
        form = OCRImageForm(request.POST, request.FILES)
        if form.is_valid():
            existing_record = RecordImage.objects.filter(user=request.user).first()
            if existing_record:
                messages.success(request, 'Image found to extract text from')
                return render(request, 'bangla_ocr_result.html', {'form': form, 'image_url': existing_record.image.url})

    form = OCRImageForm()
    messages.success(request, 'No Image Found')
    return render(request, 'bangla_ocr.html', {'form': form})

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




def update_record(request):
    record = record = Record.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = addrecord(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully')
            return redirect('real')
    else:
        form = addrecord(instance=record)
    return render(request,'update_record.html',{'form':form})