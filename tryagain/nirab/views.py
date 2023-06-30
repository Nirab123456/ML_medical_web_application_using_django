from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , addrecord
from . models import Record
import datetime
import calendar
from calendar import HTMLCalendar
import time
from datetime import datetime, timedelta
# Create your views here.



def home(request):
    current_year = datetime.now().year
    current_month = datetime.now().strftime('%B')
    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month})

def real(request):
    return render(request,'real.html')

def event(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    return render(request,'event.html',{'month':month,
                                        'year':year,
                                        'cal':cal,
                                        'now':now})




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



def view_records(request):
    records = Record.objects.all()
    return render(request,'records.html',{'records':records})



def view_record(request,pk):
    record = Record.objects.get(id=pk)
    return render(request,'record.html',{'record':record})



def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record Deleted Successfully')
    return redirect('real')




def add_record(request):
    if request.method == 'POST':
        form = addrecord(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Added Successfully')
            return redirect('records')
    else:
        form = addrecord()
    return render(request,'add_record.html',{'form':form})




def update_record(request,pk):
    record = Record.objects.get(id=pk)
    if request.method == 'POST':
        form = addrecord(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully')
            return redirect('records')
    else:
        form = addrecord(instance=record)
    return render(request,'update_record.html',{'form':form})