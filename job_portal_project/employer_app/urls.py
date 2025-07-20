from django.urls import path

from .views import *
urlpatterns = [
    path('updateProfiles/', updateProfiles, name='updateProfiles'),
    path('jobPost/', jobPost, name='jobPost'),
    path('addJob/', addJob, name='addJob'),
]