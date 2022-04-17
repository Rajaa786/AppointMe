from multiprocessing import context
from ntpath import join
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
    return render(request, 'dr.html')


@login_required(login_url='login')
def patient(request):
    return render(request, 'patient.html')


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
                return redirect('home')
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
        form = RegisterationForm(request.POST)
        print("********", form.errors, "************")
        if form.is_valid():
            form.save()
            print("success")
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
