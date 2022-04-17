from django.contrib import admin
from django.urls import path, include

from testApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dr/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('Login/', views.Login, name='login'),
    path('Register/', views.Register, name='register'),
    path('Logout/', views.Logout_, name='logout'),

]
