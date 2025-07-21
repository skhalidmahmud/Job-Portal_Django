from django.db import models
from users_auth_app.models import *

class employerProfileModel(models.Model):
    employerUser = models.OneToOneField(customUserModel, on_delete = models.CASCADE, null = True)
    companyName = models.CharField(max_length = 100, null = True)
    aboutConpany = models.TextField(null = True)
    conpanyLogo = models.ImageField(upload_to='static/img/logo', null = True)
    location = models.TextField(null = True)

class jobModel(models.Model):
    employer = models.ForeignKey(employerProfileModel, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)
    requirements = models.TextField(null = True)
    salary = models.IntegerField(null = True)
    TYPE = [
        ('FullTime','Full Time'),
        ('Remote','Remote'),
        ('Internship','Internship')
    ]
    jobType = models.CharField(choices = TYPE, max_length = 100, null = True)
    deadline = models.DateField(null = True)
    postedDate = models.DateTimeField(auto_now_add = True, null = True)