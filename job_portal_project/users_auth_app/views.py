from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from users_auth_app.models import *
from employer_app.models import *
from candidate_app.models import *
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

@login_required(login_url='logIn')
def index(req):
    all_jobs = jobModel.objects.all()
    if req.user.is_authenticated:
        if req.user.userTypes == 'Candidate':
            if candidateProfileModel.objects.filter(candidateUser=req.user):
                candidate = candidateProfileModel.objects.get(candidateUser=req.user)

                jobs_with_status = []
                for job in all_jobs:
                    applied = jobApplicationModel.objects.filter(candidate=candidate, job=job).exists()
                    jobs_with_status.append({
                        'job': job,
                        'applied': applied
                    })

                context = {
                    'jobs_with_status': jobs_with_status
                }
            else:
                context = None
        else:
            context = None
    else:
        context = None
    return render(req, 'index.html', context)

def signUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        userTypes = req.POST.get('userTypes')
        
        usernameis = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        if usernameis:
            messages.error(req, 'Username already exists')
            return render(req, 'user_auth/signUp.html')
        else:
            if userTypes == 'Admin':
                user = customUserModel.objects.create_user(
                    username = username,
                    email = email,
                    phone = phone,
                    password = phone,
                    userTypes = userTypes,
                    )
                return redirect('logIn')
            else:
                user = pendingAccountModel(
                    username = username,
                    email = email,
                    phone = phone,
                    userTypes = userTypes,
                    pendingStatus = 'Pending'
                    )
                user.save()
                return redirect('logIn')
    return render(req, 'user_auth/signUp.html')

def logIn(req):
    if req.method=='POST':
        customUser = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        pendingAccount = pendingAccountModel.objects.filter(username=req.POST.get('username')).exists()
        if customUser:
            Username = req.POST.get('username')
            Password = req.POST.get('password')
            
            user = authenticate(req, username=Username, password=Password)
            
            if user is not None:
                login(req, user)
                return redirect('index')
        elif pendingAccount:
            messages.error(req, 'Do not approved admin yeat!')
            return render(req, 'user_auth/logIn.html')
        else:
            messages.error(req, 'Username do not exists or Password incurrect')
            return render(req, 'user_auth/logIn.html')
        
    return render(req, 'user_auth/logIn.html')

@login_required(login_url='logIn')
def logOut(req):
    logout(req)
    return redirect('logIn')

@login_required(login_url='logIn')
def changePassword(req):
    if req.method=='POST':
        oldPassword = req.POST.get('oldPassword')
        newPassword = req.POST.get('newPassword')
        confirmPassword = req.POST.get('confirmPassword')
        if newPassword == confirmPassword:
            if req.user.check_password(oldPassword):
                req.user.set_password(newPassword)
                req.user.save()
                logout(req)
                return redirect('logIn')
    return render(req, 'user_auth/changePassword.html')

@login_required(login_url='logIn')
def pendingAccount(req):
    data = pendingAccountModel.objects.all()
    context={
        'data':data
    }
    return render(req, 'pendingAccount.html', context)

@login_required(login_url='logIn')
def accept(req, id):
    data = pendingAccountModel.objects.get(id=id)

    user = customUserModel.objects.create_user(
        username = data.username,
        email = data.email,
        phone = data.phone,
        password = str(data.phone),
        userTypes = data.userTypes
        )
    if data.userTypes == 'Employer':
        data = employerProfileModel(
            employerUser = user
        )
    else:
        data = candidateProfileModel(
            candidateUser = user
        )
    user.save()
    
    data = pendingAccountModel.objects.get(id=id).delete()
    return redirect("pendingAccount")

@login_required(login_url='logIn')
def deny(req, id):
    data = pendingAccountModel.objects.get(id=id).delete()
    return redirect("pendingAccount")