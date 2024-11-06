from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.home , name="home"),
    path('search-job/',views.search_job , name="search_job"),
    path('personal-profile/',views.personal_profile , name="personal_profile"),
    path('citizen_login/',views.citizen_login , name="citizen-login"),
]
