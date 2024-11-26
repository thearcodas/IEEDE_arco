from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class SkillSet(models.Model):
    skill_id = models.CharField(max_length=10, primary_key=True)
    skill_name = models.CharField(max_length=20)
    CHOICES = (("beg", "Beginner"), ("int", "Intermediate"), ("adv", "Advanced"))
    Level = models.CharField(max_length=3, choices=CHOICES, default="beg")
    Feature = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.skill_name} ({self.Level})"

class Institution(models.Model):
    IIC_no = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    TYPE_CHOICES = (
        ("school", "School"),
        ("college", "College"),
        ("university", "University"),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="school")
    location = models.CharField(max_length=120)
    Acc_status = models.CharField(max_length=5)
    logo = models.ImageField(upload_to="institute/logo")

    def __str__(self):
        return self.name


class Citizen(models.Model):
    MEC_no = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    # Guardian = models.ManyToManyField('self', related_name='guardians', blank=True)
    Address = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillSet, related_name='skillset', blank=True)
    profile_img = models.ImageField(upload_to="citizen/profile")
    

    
    def __str__(self):
        return self.name

class OTP(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def is_otp_valid(self, otp):
        time_diff = timezone.now() - self.otp_created_at
        return self.otp == otp and time_diff.total_seconds() < 300  # 5 minutes validity
    
    def __str__(self):
        return self.user.username

    

class Employer(models.Model):
    EIC_no = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    TYPE_CHOICES = (
        ("organisation", "Organisation"),
        ("individual", "Individual"),
    )
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default="individual")
    Location = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(blank=True)

class Job(models.Model):
    job_id = models.CharField(max_length=10, primary_key=True)
    job_title = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=20)
    TYPE_CHOICES = (
        ("intern", "Internship"),
        ("ft", "Full-Time"),
        ("pt", "Part-Time"),
        ("fl", "Freelancing"),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="fl")
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    skills_req = models.ManyToManyField(SkillSet, related_name="skills_required")

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=20)
    institution = models.ManyToManyField(Institution, related_name="institutions_available")
    skills = models.ManyToManyField(SkillSet, related_name="skills_offered")
    duration = models.IntegerField(null=True)
    totalsem = models.IntegerField(null=True)
    department = models.CharField(max_length=40)
    MEDIUM_CHOICES = (("online", "Online"), ("offline", "Offline"))
    medium = models.CharField(max_length=7, choices=MEDIUM_CHOICES, default="offline")

    def __str__(self):
        return self.course_name

class EducationProfile(models.Model):
    edp_id = models.CharField(max_length=30, primary_key=True)
    Inst = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(Citizen, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    roll = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=30 , unique=True)
    registration_year = models.DateField(blank=True,null=True)
    passing_year = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (("ongoing", "Ongoing"), ("completed", "Completed"))
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="ongoing")
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    ten_grade = models.FileField(upload_to="citizen/grade")
    twelve_grade = models.FileField(upload_to="citizen/grade")
    sem1 = models.FileField(upload_to="citizen/sem")
    sem2 = models.FileField(upload_to="citizen/sem")
    sem3 = models.FileField(upload_to="citizen/sem")
    sem4 = models.FileField(upload_to="citizen/sem")
    sem5 = models.FileField(upload_to="citizen/sem")
    sem6 = models.FileField(upload_to="citizen/sem")
    sem7 = models.FileField(upload_to="citizen/sem")
    sem8 = models.FileField(upload_to="citizen/sem")

    def __str__(self):
        return f"{self.student.name} ({self.registration_no})"

class EmploymentProfile(models.Model):
    emp_id = models.CharField(max_length=10, primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Employee = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (("ongoing", "Ongoing"), ("resigned", "Resigned"), ("promoted", "Promoted"))
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="ongoing")

class Application(models.Model):
    app_id = models.CharField(max_length=10, primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    STATUS_CHOICES = (("review", "In-Review"), ("accepted", "Accepted"), ("rejected", "Rejected"))
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="review")
    date = models.DateField()
