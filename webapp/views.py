from decimal import Decimal
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import HttpResponse, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import Group

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

    
def register(request):
    return render (request, 'register.html')


def userLogin(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('user'),
            password=request.POST.get('password')
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, 'This account has been disabled!')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Error wrong username/password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def Logout(request):
    messages.error(request, 'User has been loged out')
    logout(request)
    return redirect('/login')

def registerCustomer(request):
    if request.method == 'POST':
        # name = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        pass1 = request.POST.get('password1')

        if checkUserExist(email):
            user = User.objects.create_user(
                username=email,
                first_name=firstname,
                last_name=lastname,
                password=pass1,
            )

            my_group = Group.objects.get(name='customer')
            my_group.user_set.add(user)

            if user is not None:
                messages.error(request, 'User has been created.')
                return redirect('/login')
        else:
            messages.error(request, 'Username or Email is Already Exist')
            return render(request, 'login.html')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
