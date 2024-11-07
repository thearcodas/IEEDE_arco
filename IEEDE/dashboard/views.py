from django.shortcuts import render

# Create your views here.

def forgot_password(request):
    return render(request, 'forgot_pass.html')

## citizens
def citizen_login(request):
    return render(request, 'citizen_login.html')

def home(request):
    return render(request, 'citizen_landing.html')

def citizen_skillset(request):
    return render(request, 'citizen_skillset.html')

def citizen_education_profile(request):
    return render(request, 'citizen_education_profile.html')

def personal_profile(request):
    return render(request, 'citizen_personal_profile.html')

## institutions
def institution_login(request):
    return render(request, 'institution_login.html')

def institution(request):
    return render(request, 'institution_landing.html')

def institution_staff(request):
    return render(request, 'institution_staff_manage.html')


def employer_login(request):
    return render(request, 'employer_login.html')


def search_job(request):
    return render(request, 'search_jobs.html')
