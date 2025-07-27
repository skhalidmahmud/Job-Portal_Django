from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required 

@login_required(login_url='logIn')
def updateProfiles(req):
    data = models.candidateProfileModel.objects.filter(candidateUser=req.user).first()
    context = {
        'data': data
    }
    if not data:
        data = models.candidateProfileModel.objects.create(candidateUser=req.user)

    if req.method == 'POST':
        data.candidateUser = req.user
        data.fullName = req.POST.get('fullName')
        data.adress = req.POST.get('adress')
        data.dateOfBirth = req.POST.get('dateOfBirth')

        data.save()

        return redirect('index')
    return render(req, 'candidateUpdateProfiles.html', context)

@login_required(login_url='logIn')
def applyJob(req, id):
    getJob = models.jobModel.objects.get(id=id)
    candidate = models.candidateProfileModel.objects.get(candidateUser=req.user)

    jobApplication = models.jobApplicationModel(
        job = getJob,
        candidate= candidate,
        status = 'Applied'
    )
    jobApplication.save()

    return redirect('index')

@login_required(login_url='logIn')
def appliedJobs(req):
    if models.candidateProfileModel.objects.filter(candidateUser=req.user):
        candidate=models.candidateProfileModel.objects.get(candidateUser=req.user)
        data = models.jobApplicationModel.objects.filter(candidate=candidate)
        context={
            'data':data
        }
    else:
        return redirect('candidateUpdateProfiles')
    return render(req, 'appliedJobs.html', context)

@login_required(login_url='logIn')
def deleteAppliedJob(req, id):
    data = models.jobApplicationModel.objects.get(id=id)
    data.delete()
    return redirect('appliedJobs')

@login_required(login_url='logIn')
def updateAppliedJob(req, id):
    data = models.jobApplicationModel.objects.get(id=id)
    context={
        'data':data
    }
    if req.method == "POST":
        workExprience = req.POST.get('workExprience')
        lastEducation = req.POST.get('lastEducation')

        new = models.jobApplicationModel(
            id = id,
            job = data.job,
            candidate = data.candidate,
            status = data.status,
            workExprience =workExprience,
            lastEducation =lastEducation
        )
        new.save()
        return redirect('appliedJobs')
    return render(req, 'updateAppliedJob.html', context)