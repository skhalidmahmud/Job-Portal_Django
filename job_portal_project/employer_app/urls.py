from django.urls import path

from .views import *

urlpatterns = [
    path('updateProfiles/', updateProfiles, name='employerUpdateProfiles'),
    path('jobPost/', jobPost, name='jobPost'),
    path('addJob/', addJob, name='addJob'),

    path('viewjob/<int:id>',viewjob,name='viewjob'),
    path('updatejob/<int:id>',updatejob,name='updatejob'),
    path('deletejob/<int:id>',deletejob,name='deletejob'),
    
    path('jobApplications/', jobApplications, name='jobApplications'),

    path('callInterview/<int:id>', callInterview, name='callInterview'),
    path('rejectApplication/<int:id>', rejectApplication, name='rejectApplication'),
    path('offeerApplication/<int:id>', offeerApplication, name='offeerApplication'),
]