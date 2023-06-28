from .forms import signupForm,updaterecordform
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import record


def home(request):
	record_list = record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['name']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'record_list': record_list})



def login_user(request):
    pass





def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out!")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = signupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			# Authenticate
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Registered Successfully!")
			return redirect('home')
	else:
		form = signupForm()
	return render(request, 'register.html', {'form': form})


def castomer_record(request, pk):
	if request.user.is_authenticated:
		record_list = record.objects.get(id=pk)

	else:
		messages.success(request, "You Have To Login First!")

	return render(request, 'record.html', {'record_list': record_list})



def delete_record(request, pk):
	if request.user.is_authenticated:
		record_list = record.objects.get(id=pk)
		record_list.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "You Have To Login First!")
		return redirect('home')
	

def update_record(request):
    if request.user.is_authenticated:
        form = updaterecordform()  # Define a default value for the form
        if request.method == 'POST':
            form = updaterecordform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated Successfully!")
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Have To Login First!")
        return redirect('home')
