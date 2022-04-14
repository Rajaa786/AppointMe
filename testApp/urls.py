from django.contrib import admin
from django.urls import path ,include

from testApp import views

urlpatterns = [
    path('',views.index,name='testApp'),
    path('dr/',views.doctor,name='testApp'),
    path('patient/',views.patient,name='testApp'),
    path('Login/',views.Login, name='testApp'),
    path('Register/',views.Register, name='testApp'),
    
]