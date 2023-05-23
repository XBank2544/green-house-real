import requests
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

        # Save the data to Supabase
        supabase_url = 'https://plmhcpnlnhgfeydcgijk.supabase.co/database/tables/webapp_schedule'
        supabase_key = 'sbp_d93e1cd9e760d209e58103bdfd6b1c0689343aa8'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {supabase_key}'
        }

        data = {
            'fan_start': fan_start,
            'fan_stop': fan_stop,
            'start_at': start_at,
            'end_at': end_at
        }

        response = requests.POST(supabase_url, headers=headers, json=data)

        if response.status_code == 201:
            # Data saved successfully
            return redirect('/dashboard')
        else:
            # Error occurred while saving data
            return HttpResponse('Error occurred while saving data')
    else:
        return render(request, 'schedule.html')

def login(request):
    return render (request, 'login.html')
    
def register(request):
    return render (request, 'register.html')
