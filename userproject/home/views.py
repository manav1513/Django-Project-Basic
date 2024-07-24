from django.contrib.auth import authenticate, logout as auth_logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user, '++++++++++++++++++++++')
        if user is  None:
            return redirect('/')  # Redirect to home or dashboard
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'index.html')

def logout(request):
    auth_logout(request)
    return redirect('index')  # Redirect to index page after logout
