from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .mails import *
from .utility import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.

def forgot_password(request):
    return render(request, 'forgot_pass.html')

## citizens
def citizen_login(request):
    
    return render(request, 'citizen_login.html')

@csrf_exempt
@require_POST
def send_otp(request):  ## mec id validation and otp send 
    if request.method =="POST":
        try:
            data = json.loads(request.body)
            mec = data.get("mec")
            if User.objects.filter(username=mec).exists():
                otp_gen = otp_generate() # Generate and send the OTP 
                user = User.objects.get(username=mec)
                otp = OTP(user=user,otp=otp_gen,otp_created_at=timezone.now())
                otp.save()
                OTP_mail(otp_gen,user.email) ## send otp to the user mail
                request.session['mec_id']=mec
                return JsonResponse({"message": "OTP sent successfully!"})
            else:
                return JsonResponse({"error": "MEC ID is required."},status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
@require_POST
def verify_otp(request):
    if request.method =="POST":
        mec_id = request.session.get["mec_id"]
        print(mec_id)
        try:
            data = json.loads(request.body)
            otp = data.get("otp")
            user = User.objects.get(username=mec_id)
            otp_ver = OTP.objects.get(user_id=user)
            if otp == otp_ver.otp:
                login(request,user)
                # Respond to the client
                return JsonResponse({"message": "OTP sent successfully!"})
            else:
                return JsonResponse({"error": "MEC ID is required."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    # Handle non-POST requests
    return JsonResponse({"error": "Invalid request method."}, status=405)

def home(request): ## citizen dashboard page
    if not request.user.is_authenticated:
        return redirect("/citizen-login")
    else:
        return render(request, 'citizen_landing.html')

def citizen_skillset(request):
    return render(request, 'citizen_skillset.html')

def citizen_education_profile(request):
    return render(request, 'citizen_education_profile.html')

def personal_profile(request):
    return render(request, 'citizen_personal_profile.html')

## institutions
def institution_login(request): 
    if request.method == "POST":
        lic = request.POST["lic"]
        psw = request.POST["psw"]
        if User.objects.filter(username=lic).exists():
            institute = authenticate(request,username=lic,password=psw)
            if institute is not None:
                    login(request,institute)  ## institution login
            return redirect("/institution",{"institute":institute})
        else:
            return redirect("/institution-login")
    return render(request, 'institution_login.html')

@login_required
def institution_logout(request):
    logout(request) ## institution logout
    return redirect("/institution-login")

# @login_required
def institution(request):
    # institute_name = request.session.get['institute_name']
    # institute = EducationProfile.objects.filter(inst=institute_name)
    if not request.user.is_authenticated:
        return redirect("/institution-login")
    else: 

        return render(request, 'institution_landing.html')

# @login_required
def institution_student(request):
    # int_no = request.session.get["institute_name"]
    if request.method == "POST":
        addmecid = request.POST['addmecid']
        addnamestu = request.POST['addnamestu']
        addrollstu = request.POST['addrollstu']
        addregstu = request.POST['addregstu']
        addphonestu = request.POST['addphonestu']
        addemailstu = request.POST['addemailstu']
        dept = request.POST['dept']
        course = request.POST['course']
        syear = request.POST['syear']
        eyear = request.POST['eyear']
        status = request.POST['status']
        edp_id =edp_id_generator()
        if  User.objects.filter(username=addmecid).exists() and not EducationProfile.objects.filter(edp_id=edp_id).exists():
            user = User.objects.get(username=addmecid)
            citizen = Citizen.objects.get(MEC_no=user)
            course_id = course_id_generator()
            edp_id = edp_id_generator()
            course = Course.objects.create()
            education_profile = EducationProfile.objects.create(
                edp_id=edp_id,
                roll=addrollstu,
                Inst=int_no,
                department=dept,
                registration_no=addregstu,
                registration_year=syear,
                passing_year=eyear,
                status=status)

    return render(request, 'institution_student_manage.html')

@login_required
def institution_course(request):
    if request.method == "POST":
        coursecode = request.POST["coursecode"]
        coursename = request.POST["coursename"]
        duration = request.POST["duration"]
        totalsem = request.POST["totalsem"]
        department = request.POST["department"]
        if not Course.objects.filter(course_id=coursecode).exists():
            course = Course.objects.create(
                course_id=coursecode,
                course_name=coursename,
                duration=duration,
                department=department,
                totalsem=totalsem,
                type="deg",
                medium="offline")
            course.save()
    courses = Course.objects.all()
    return render(request, 'institution_course_manage.html' , {'courses':courses})

def institution_result(request):
    return render(request, 'institution_result_manage.html')

# ## employes
# def employer_login(request):
#     return render(request, 'employer_login.html')


# def search_job(request):
#     return render(request, 'search_jobs.html')
