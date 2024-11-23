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
    if request.method == "POST":
        email = request.POST['ph']
        if User.objects.filter(email=email).exists():
            otp_gen = otp_generate() # Generate and send the OTP 
            user = User.objects.get(email=email)
            otp = OTP(user=user,otp=otp_gen,otp_created_at=timezone.now())
            otp.save()
            OTP_mail(otp_gen,user.email) ## send otp to the user mail
            print(email)
    return render(request, 'forgot_pass.html')

## citizens
def citizen_login(request): ## citizen login
    return render(request, 'citizen_login.html') #ok

def citizen_registration(request):
    # if request.method =="POST":
    #     mec = request.POST['mec']
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     address = request.POST['address']
    #     if not User.objects.filter(username=mec).exists():
    #         first_name, last_name = name.split()
    #         user = User(username=mec,email=email,first_name=first_name,last_name=last_name)
    #         user.save()
    #         citizen =Citizen(user=user.username,name=name,phone=phone,address=address)
    #         citizen.save()
    #         otp_gen = otp_generate() # Generate and send the OTP 
    #         otp = OTP.objects.create(user=user,otp=otp_gen,otp_created_at=timezone.now())
    #         otp.save()
    #         OTP_mail(otp_gen,user.email) ## send otp to the user mail
            
    return render(request,"citizen_reg.html")

@login_required
def citizen_logout(request): ## citizen logout
    logout(request)
    return redirect("/citizen-login") #ok

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
                return JsonResponse({"mec_id": mec})
            else:
                return JsonResponse({"error": "MEC ID is required."},status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405) #ok

@csrf_exempt
@require_POST
def verify_otp(request):
    if request.method =="POST":
        try:
            data = json.loads(request.body)
            otp = data.get("otp")
            mec_id = data.get("mec")
            user = User.objects.get(username=mec_id)
            otp_ver = OTP.objects.get(user_id=user)
            if otp == otp_ver.otp:
                login(request,user)
                return JsonResponse({"message": "OTP sent successfully!"})
            else:
                return JsonResponse({"error": "MEC ID is required."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    #Handle non-POST requests
    return JsonResponse({"error": "Invalid request method."}, status=405) #ok

def home(request): ## citizen dashboard page
    if not request.user.is_authenticated:
        return redirect("/citizen-login")
    else:
        user = request.user
        citizen = Citizen.objects.get(MEC_no=user.id)
        return render(request, 'citizen_landing.html',{"user": user,"citizen":citizen}) #ok

@login_required
def citizen_skillset(request):
    return render(request, 'citizen_skillset.html')

@login_required
def citizen_education_profile(request):
    user = request.user
    citizen = Citizen.objects.get(MEC_no=user.id)
    return render(request, 'citizen_education_profile.html',{"user": user,"citizen":citizen})

@login_required
def personal_profile(request):
    user = request.user
    citizen = Citizen.objects.get(MEC_no=user.id)
    return render(request, 'citizen_personal_profile.html',{"user": user,"citizen":citizen})

## institutions
def institution_login(request): 
    if request.method == "POST":
        lic = request.POST["lic"]
        psw = request.POST["psw"]
        if User.objects.filter(username=lic).exists():
            institute = authenticate(request,username=lic,password=psw)
            if institute is not None:
                    login(request,institute)  ## institution login
            return redirect("/institution")
        else:
            return redirect("/institution-login")
    return render(request, 'institution_login.html') #ok

@login_required
def institution_logout(request):
    logout(request) ## institution logout
    return redirect("/institution-login") #ok

def institution_registration(request):
    return render(request,"institution_reg.html") 

def institution(request):
    if not request.user.is_authenticated:
        return redirect("/institution-login")
    else: 
        institution = request.user.id
        user = User.objects.get(id=institution)
        institute = Institution.objects.get(IIC_no=institution)
        students = EducationProfile.objects.filter(Inst=institute)
        course = Course.objects.filter(institution=institution)
        courses = course.count()
        student = students.count()
        return render(request, 'institution_landing.html',{"user":user ,"institute":institute,"courses":courses,"student":student}) #ok

@login_required
def institution_student(request):
    request_user = request.user.id
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
        if  User.objects.filter(id=request_user).exists() and not EducationProfile.objects.filter(edp_id=edp_id).exists():
            users = User.objects.get(username=addmecid)
            citizen = Citizen.objects.get(MEC_no=users.id)
            courses = Course.objects.get(course_name=course,institution=request_user)
            print(citizen)
            print(citizen.MEC_no)
            institute = Institution.objects.get(IIC_no=request_user)
            edp_id = edp_id_generator()  ## auto genetated Educational Profile ID
            education_profile = EducationProfile(
                edp_id=edp_id,
                Inst=institute,
                roll=addrollstu,
                student=citizen,
                course=courses,
                registration_no=addregstu,
                registration_year=syear,
                passing_year=eyear,
                status=status)
            education_profile.save()
    institute = Institution.objects.get(IIC_no=request_user)
    students = EducationProfile.objects.filter(Inst=institute)
    print(students)
    return render(request, 'institution_student_manage.html',{"students":students})

@login_required
def institution_course(request):
    request_user = request.user
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
            course.institution.set(request_user)
            course.save()

    institute = Institution.objects.get(IIC_no=request_user.id)
    courses = Course.objects.filter(institution=institute)
    return render(request, 'institution_course_manage.html' , {'courses':courses}) #ok

def institution_result(request):
    return render(request, 'institution_result_manage.html')

# ## employes
# def employer_login(request):
#     return render(request, 'employer_login.html')


# def search_job(request):
#     return render(request, 'search_jobs.html')
