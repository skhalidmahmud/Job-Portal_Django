from django.urls import path

from .views import *

urlpatterns = [
    path('updateProfiles/', updateProfiles, name='candidateUpdateProfiles'),
    path('applyJob/<int:id>', applyJob, name='applyJob'),
    # path('addJob/', addJob, name='addJob'),

    # path('viewjob/<int:id>',viewjob,name='viewjob'),
    # path('updatejob/<int:id>',updatejob,name='updatejob'),
    # path('deletejob/<int:id>',deletejob,name='deletejob'),
    
    # path('jobApplications/',jobApplications,name='jobApplications'),
]