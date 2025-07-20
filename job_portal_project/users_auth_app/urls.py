from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('signUp/', signUp, name='signUp'),
    path('logIn/', logIn, name='logIn'),
    path('logOut/', logOut, name='logOut'),
    path('changePassword/', changePassword, name='changePassword'),
    
    path('pendingAccount/', pendingAccount, name='pendingAccount'),

    
    path('accept/<int:id>', accept, name='accept'),
    path('deny/<int:id>', deny, name='deny'),
]