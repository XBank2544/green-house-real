from decimal import Decimal
from . import models
from django.shortcuts import render

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
        supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsbWhjcG5sbmhnZmV5ZGNnaWprIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODM3MDg2MjQsImV4cCI6MTk5OTI4NDYyNH0.TSa1If5ES9C-Pr8Ikmeae8yU64IlW0xs5R9KzOcv-kA'
        

        

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
