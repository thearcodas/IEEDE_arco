from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.home , name="home"),
    ## citizens
    path('citizen-login/',views.citizen_login , name="citizen_login"),
    path('citizen-registration/',views.citizen_registration , name="citizen_registration"),
    path('citizen-logout/',views.citizen_logout , name="citizen_logout"),
    path('citizen-login/send-otp/',views.send_otp , name="send_otp"),
    path('citizen-login/verify-otp/',views.verify_otp , name="verify_otp"),
    path('forgot-password/',views.forgot_password , name="forgot_password"),
    path('citizen-skillset/',views.citizen_skillset , name="citizen_skillset"),
    path('personal-profile/',views.personal_profile , name="personal_profile"),
    path('citizen-education-profile/',views.citizen_education_profile , name="citizen_education_profile"),
    ## institutions
    path('institution-login/',views.institution_login , name="institution_login"),
    path('institution-registration/',views.institution_registration , name="institution_registration"),
    path('institution-logout/',views.institution_logout , name="institution_logout"),
    path('institution/',views.institution , name="institution"),
    path('institution-student/',views.institution_student , name="institution_student"),
    path('institution-student/student-update/',views.student_update , name="student_update"),
    path('institution-student/rejectStudent',views.reject_Student , name="reject_Student"),
    path('institution-course/course-update/',views.course_update , name="course_update"),
    path('institution-course/course-delete/',views.course_delete , name="course_delete"),
    path('institution-course/',views.institution_course , name="institution_course"),
    path('institution-result/',views.institution_result , name="institution_result"),
    # ## employes
    # path('search-job/',views.search_job , name="search_job"),
    # path('employer-login/',views.employer_login , name="employer_login"),
]
