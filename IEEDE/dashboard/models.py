from django.db import models
from django.contrib.auth.models import User

class SkillSet(models.Model):
    skill_id = models.CharField(max_length=10, primary_key=True)
    skill_name = models.CharField(max_length=20)
    CHOICES = (("beg", "Beginner"), ("int", "Intermediate"), ("adv", "Advanced"))
    Level = models.CharField(max_length=3, choices=CHOICES, default="beg")
    Feature = models.BooleanField(default=True)

class Institution(models.Model):
    IIC_no = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    TYPE_CHOICES = (
        ("school", "School"),
        ("college", "College"),
        ("university", "University"),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="school")
    location = models.CharField(max_length=15)
    Acc_status = models.CharField(max_length=5)

class Citizen(models.Model):
    MEC_no = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    Guardian = models.ManyToManyField('self', related_name='guardians', blank=True)
    Address = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillSet, related_name='skillset', blank=True)
    
    def __str__(self):
        return self.name

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
    TYPE_CHOICES = (("deg", "Degree"), ("cert", "Certificates"))
    MEDIUM_CHOICES = (("online", "Online"), ("offline", "Offline"))
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default="cert")
    medium = models.CharField(max_length=7, choices=MEDIUM_CHOICES, default="online")

class EducationProfile(models.Model):
    edp_id = models.CharField(max_length=10, primary_key=True)
    Inst = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(Citizen, on_delete=models.CASCADE)
    qualifications = models.CharField(max_length=20)
    passing_year = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (("ongoing", "Ongoing"), ("completed", "Completed"))
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="ongoing")
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True)

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
