from datetime import datetime
from time import time
from .models import AppointmentMade, Appointments, UserProfile, MyUser
from django.shortcuts import redirect, render, HttpResponse
from .forms import RegisterationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def doctor(request):
    appointMentList = request.user.appointments_set.all()
    return render(request, 'appointmentsMade.html', {'Appointments': appointMentList, 'User': request.user.userprofile.role})


@login_required(login_url='login')
def appoint(request):
    # appointMentList = AppointmentMade.objects.filter(user = request.user)
    appointMentList = request.user.appointmentmade_set.all()
    return render(request, 'appointmentsMade.html', {'Appointments': appointMentList, 'User': request.user.userprofile.role})


@login_required(login_url='login')
def patient(request):
    if request.method == 'POST':
        email = request.POST['email']
        # doctor_name = request.POST['doctor_name']
        desc = request.POST['desc']
        phoneNum = request.POST['phoneNum']
        doctorEmail = request.POST['doctor_name']
        doctor = MyUser.objects.get(email=doctorEmail)
        appointMent = Appointments.objects.create(
            user=doctor, desc=desc, emailField=email, contact=phoneNum, time=datetime.now())
        appointMentMade = AppointmentMade.objects.create(
            user=request.user, appointment=appointMent)
        return redirect('appointList')

    doctorList = UserProfile.objects.filter(role='Doctor')
    context = {'doctors_list': doctorList}
    return render(request, 'patient.html', context)


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.errors)
        str_ = form.non_field_errors()
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password_']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print("User Found")
                login(request, user)
                print(user.userprofile.role)
                if user.userprofile.role == 'Patient':
                    return redirect('patientPage')
                else:
                    return redirect('doctorPage')
            else:
                print("User Not Found")
                return redirect('register')
        else:
            return HttpResponse(str_)
    else:
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})


def Register(request):
    if request.method == 'POST':
        role = request.POST['selectInputData']
        form = RegisterationForm(request.POST)
        print("********", form.errors, "************")
        if form.is_valid():
            user = form.save()
            userProfile = UserProfile.objects.create(user=user, role=role)
            print(user)
            print("*****")
            print(userProfile)
            return redirect('login')
        else:
            # context{
            #     'form': form,
            # }
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterationForm()
        print("fail")
        return render(request, 'register.html', {'form': form})


def Logout_(request):
    logout(request)
    return redirect('login')
