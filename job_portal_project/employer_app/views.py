from django.shortcuts import render

# Create your views here.
def updateProfiles(req):
    return render(req, 'updateProfiles.html')