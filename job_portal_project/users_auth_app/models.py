from django.contrib.auth.models import AbstractUser
from django.db import models

class customUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Employer','Employer'),
        ('Candidate','Candidate')
    ]
    phone = models.CharField(max_length = 100, null = True)
    userTypes = models.CharField(choices = USERTYPE, max_length = 100, null = True)

class pendingAccountModel(models.Model):
    username = models.CharField(max_length = 100, null = True)
    email = models.EmailField(null = True)
    phone = models.CharField(max_length = 100, null = True)
    USERTYPE = [
        ('Employer','Employer'),
        ('Candidate','Candidate')
    ]
    userTypes = models.CharField(choices = USERTYPE, max_length = 100, null = True)
    STATUS = [
        ('Pending','Pending'),
        ('Accept','Accept'),
        ('Rejected','Rejected')
    ]
    pendingStatus = models.CharField(choices = STATUS, max_length = 100, null = True)