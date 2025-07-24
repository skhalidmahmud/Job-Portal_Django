from django.shortcuts import render, redirect
from . import models

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