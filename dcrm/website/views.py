from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
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
		return render(request, 'home.html', {})



def login_user(request):
    pass





def logout_user(request):
    pass