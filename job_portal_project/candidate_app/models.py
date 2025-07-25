from django.db import models
from users_auth_app.models import customUserModel
from employer_app.models import jobModel

class candidateProfileModel(models.Model):
    candidateUser = models.OneToOneField(customUserModel, on_delete = models.CASCADE, null = True)
    fullName = models.CharField(max_length = 100, null = True)
    adress = models.TextField(null = True)
    dateOfBirth = models.DateField(null = True)

class jobApplicationModel(models.Model):
    job = models.ForeignKey(jobModel, on_delete = models.CASCADE, null = True)
    candidate = models.ForeignKey(candidateProfileModel, on_delete = models.CASCADE, null = True)
    STATUS = [
        ('Applied','Applied'),
        ('Interview','Interview'),
        ('Offered','Offered'),
        ('Rejected','Rejected')
    ]
    status = models.CharField(choices = STATUS, max_length = 100, null = True)
    appliedAt = models.DateTimeField(auto_now_add = True, null = True)
    lastEducation = models.CharField(max_length = 20, null = True)
    workExprience = models.TextField(null = True)