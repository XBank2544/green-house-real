import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(requests):
  return render(requests, "home.html")

def dashboard(requests):
    return render (requests, 'dashboard.html')

def schedule(requests):
    if requests.method == 'POST':
        fan_start = requests.POST['fan_start']
        fan_stop = requests.POST['fan_stop']
        start_at = requests.POST['start_at']
        end_at = requests.POST['end_at']

        # Save the data to Supabase
        supabase_url = 'https://plmhcpnlnhgfeydcgijk.supabase.co'
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsbWhjcG5sbmhnZmV5ZGNnaWprIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODM3MDg2MjQsImV4cCI6MTk5OTI4NDYyNH0.TSa1If5ES9C-Pr8Ikmeae8yU64IlW0xs5R9KzOcv-kA'

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

        response = requests.post(supabase_url, headers=headers, json=data)

        if response.status_code == 201:
            # Data saved successfully
            return redirect('/dashboard')
        else:
            # Error occurred while saving data
            return HttpResponse('Error occurred while saving data')
    else:
        return render(requests, 'schedule.html')

def login(request):
    return render (requests, 'login.html')
    
def register(request):
    return render (requests, 'register.html')
