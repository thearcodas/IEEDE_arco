from django.contrib import admin
from dashboard.models import *

# Register your models here.
admin.site.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('MEC_no', 'name', 'phone', 'Guardian',  'Address', 'skills')

admin.site.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('IIC_no', 'name', 'TYPE_CHOICES', 'type', 'location', 'Acc_status')

admin.site.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('ETC_no','name', 'TYPE_CHOICES', 'type', 'Locatio', 'phone', 'email')

admin.site.register(SkillSet)
class SkillsetAdmin(admin.ModelAdmin):
    list_display = ('skill_id', 'skill_name','CHOICES', 'Level', 'Feature')

admin.site.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'institution', 'skills', 'duration', 'TYPE_CHOICES', 
                    'MEDIUM_CHOICES','type', 'medium')

admin.site.register(EducationProfile)
class EducationProfileAdmin(admin.ModelAdmin):
    list_display = ('edp_id', 'Inst', 'course', 'student', 'qualifications','passing_year','STATUS_CHOICES','status','cgpa')

admin.site.register(EmploymentProfile)
class EmploymentProfileAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'employer', 'Employee','Job','start','end','STATUS_CHOICES','status')

admin.site.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'job_title', 'designation','description','location','TYPE_CHOICES','type','employer','skills_req')

admin.site.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('app_id', 'job','applicant','STATUS_CHOICES','status','date')