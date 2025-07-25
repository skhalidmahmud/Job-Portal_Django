from django.urls import path

from .views import *

urlpatterns = [
    path('updateProfiles/', updateProfiles, name='candidateUpdateProfiles'),
    path('applyJob/<int:id>', applyJob, name='applyJob'),
    path('appliedJobs/', appliedJobs, name='appliedJobs'),

    path('updateAppliedJob/<int:id>', updateAppliedJob, name='updateAppliedJob'),
    path('deleteAppliedJob/<int:id>', deleteAppliedJob, name='deleteAppliedJob'),
    
    # path('jobApplications/',jobApplications,name='jobApplications'),
]