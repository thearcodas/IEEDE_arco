from django.shortcuts import render

# Create your views here.

def citizen_login(request):
    return render(request, 'citizen_login.html')

def home(request):
    return render(request, 'citizen_landing.html')

def search_job(request):
    return render(request, 'search_jobs.html')

def citizen_skillset(request):
    return render(request, 'citizen_skillset.html')

def citizen_education_profile(request):
    return render(request, 'citizen_education_profile.html')

def personal_profile(request):
    return render(request, 'citizen_personal_profile.html')