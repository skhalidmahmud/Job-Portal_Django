from django.shortcuts import render, redirect
from .models import *
from candidate_app.models import *
from django.contrib.auth.decorators import login_required 

@login_required(login_url='logIn')
def updateProfiles(req):
    data = employerProfileModel.objects.filter(employerUser=req.user).first()
    context = {
        'data': data
    }
    if not data:
        data = employerProfileModel.objects.create(employerUser=req.user)

    if req.method=='POST':
        data.companyName=req.POST.get('companyName')
        data.aboutConpany=req.POST.get('aboutConpany')
        if req.FILES.get('conpanyLogo'):
            data.conpanyLogo=req.FILES.get('conpanyLogo')
        data.location=req.POST.get('location')

        data.save()
        return redirect('index')
    
    return render(req, 'employerUpdateProfiles.html', context)

@login_required(login_url='logIn')
def jobPost(req):
    profile = employerProfileModel.objects.filter(employerUser=req.user).first()

    data = jobModel.objects.filter(employer=profile)
    context={
        'data':data
    }

    return render(req, 'jobPost.html', context)

@login_required(login_url='logIn')
def addJob(req):
    profile = employerProfileModel.objects.filter(employerUser=req.user).first()
    
    if req.method=='POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        requirements = req.POST.get('requirements')
        salary = req.POST.get('salary')
        jobType = req.POST.get('jobType')
        deadline = req.POST.get('deadline')

        data = jobModel.objects.create(
            employer=profile,
            title=title,
            description=description,
            requirements=requirements,
            salary=salary,
            jobType=jobType,
            deadline=deadline
        )
        return redirect('jobPost')
    return render(req, 'addJob.html')

@login_required(login_url='logIn')
def deletejob(req, id):
    data = jobModel.objects.get(id=id).delete()
    return redirect ('jobPost')

@login_required(login_url='logIn')
def viewjob(req,id):
    data = jobModel.objects.get(id=id)
    context={
        'data':data
    }
    return render(req,"viewjob.html", context)

@login_required(login_url='logIn')
def updatejob(req,id):
    data=jobModel.objects.get(id=id)
    context={
        'data':data
    }
    if req.method=='POST':
        data.id=id
        data.title=req.POST.get('title')
        data.description=req.POST.get('description')
        data.requirements=req.POST.get('requirements')
        data.salary=req.POST.get('salary')
        data.jobType=req.POST.get('jobType')
        data.deadline=req.POST.get('deadline')

        data.save()
        return redirect ('jobPost')

    return render(req,"updatejob.html", context)

@login_required(login_url='logIn')
def jobApplications(req):
    profile = employerProfileModel.objects.get(employerUser=req.user)
    job = jobModel.objects.filter(employer=profile)
    data = jobApplicationModel.objects.filter(job__in=job)

    context = {
        'data': data
    }
    return render(req, 'jobApplications.html', context)

@login_required(login_url='logIn')
def callInterview(req, id):
    data = jobApplicationModel.objects.get(id=id)

    newData = jobApplicationModel(
    id=id,
    job = data.job,
    candidate = data.candidate,
    status = 'Interview',
    appliedAt = data.appliedAt,
    lastEducation = data.lastEducation,
    workExprience = data.workExprience
    )
    newData.save()
    return redirect('jobApplications')

@login_required(login_url='logIn')
def rejectApplication(req, id):
    data = jobApplicationModel.objects.get(id=id)

    newData = jobApplicationModel(
    id=id,
    job = data.job,
    candidate = data.candidate,
    status = 'Rejected',
    appliedAt = data.appliedAt,
    lastEducation = data.lastEducation,
    workExprience = data.workExprience
    )
    newData.save()
    return redirect('jobApplications')

@login_required(login_url='logIn')
def offeerApplication(req, id):
    data = jobApplicationModel.objects.get(id=id)

    newData = jobApplicationModel(
    id=id,
    job = data.job,
    candidate = data.candidate,
    status = 'Offered',
    appliedAt = data.appliedAt,
    lastEducation = data.lastEducation,
    workExprience = data.workExprience
    )
    newData.save()
    return redirect('jobApplications')