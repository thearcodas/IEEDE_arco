from django.shortcuts import render

# Create your views here.

def citizen_login(request):
    return render(request, 'citizen_login.html')

def home(request):
    return render(request, 'citizen_landing.html')

def search_job(request):
    return render(request, 'search_jobs.html')

def personal_profile(request):
    return render(request, 'citizen_personal_profile.html')