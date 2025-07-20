from django.shortcuts import render, redirect
from .models import *


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
    
    return render(req, 'updateProfiles.html', context)