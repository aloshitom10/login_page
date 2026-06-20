from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'login.html', {'error_message': 'Please fill in all fields.'})
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    
    return render(request, 'login.html')

def register(request):
    """Handle user registration"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        
        # Validation
        if not username or not email or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'register.html', {'error_message': 'Please fill in all fields.'})
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'register.html', {'error_message': 'Password must be at least 6 characters.'})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html', {'error_message': 'Username already exists.'})
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'register.html', {'error_message': 'Email already registered.'})
        
        # Create user
        try:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('home')
        except Exception as e:
            messages.error(request, 'An error occurred during registration.')
            return render(request, 'register.html', {'error_message': 'Registration failed. Please try again.'})
    
    return render(request, 'register.html')

@login_required(login_url='home')
def dashboard(request):
    """Display user dashboard"""
    return render(request, 'dashboard.html')

def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


