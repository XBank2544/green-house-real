from decimal import Decimal
from . import models
from django.shortcuts import render
import supabase

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
        client = supabase.create_client(supabase_url, supabase_key)

        

        data = {
            'fan_start': Decimal(fan_start),
            'fan_stop': Decimal(fan_stop),
            'start_at': start_at,
            'end_at': end_at
        }
        response = client.table('webapp_schedule').insert(data)
        
        if response['status'] == 201:
            # Data saved successfully
            return render(request, 'schedule.html')
        else:
            # Error occurred while saving data
            return render(request, 'error.html')
    else:
        return render(request, 'schedule.html')

def login(request):
    return render (request, 'login.html')
    
def register(request):
    return render (request, 'register.html')
