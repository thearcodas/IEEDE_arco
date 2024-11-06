from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.home , name="home"),
    path('search-job/',views.search_job , name="search_job"),
    path('citizen-login/',views.citizen_login , name="citizen-login"),
    path('citizen-skillset/',views.citizen_skillset , name="citizen_skillset"),
    path('personal-profile/',views.personal_profile , name="personal_profile"),
    path('citizen-education-profile/',views.citizen_education_profile , name="citizen_education_profile"),
]
