from decimal import Decimal
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, "home.html")

def dashboard(request):
    return render (request, 'dashboard.html')

def schedule(request):
    if request.method == 'POST':
        fan_start = request.POST['fan_start']
        fan_stop = request.POST['fan_stop']
        start_at = request.POST['start_at']
        end_at = request.POST['end_at']
        data = {
            'fan_start': Decimal(fan_start),
            'fan_stop': Decimal(fan_stop),
            'start_at': start_at,
            'end_at': end_at
        }
        models.Schedule.objects.create(**data)
        
        return render(request, 'schedule.html')
    else:
        return render(request, 'schedule.html')

def login(request):
    return render (request, 'login.html')
    
def register(request):
    return render (request, 'register.html')


def login(request):
    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_ip = request.META.get('REMOTE_ADDR') 

        if username == 'your_username' and password == 'your_password' and user_ip == 'your_allowed_ip':
            
            return redirect('home')  
        else:

            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:

        return render(request, 'login.html')
