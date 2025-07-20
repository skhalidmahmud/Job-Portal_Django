from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('signUp/', signUp, name='signUp'),
    path('logIn/', logIn, name='logIn'),
    path('logOut/', logOut, name='logOut'),
    path('changePassword/', changePassword, name='changePassword'),
]