from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('password')
        c=authenticate(username=a,password=b)
        if c :
            login(request,c)
            return redirect('dashboard')
        else:
            return redirect('home')    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('password')
        User.objects.create_user(username=a,email=b,password=c)
        return redirect('home')
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')