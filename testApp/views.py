from django.shortcuts import redirect, render, HttpResponse
from .forms import RegisterationForm, LoginForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def doctor(request):
    return render(request, 'dr.html')


def patient(request):
    return render(request, 'patient.html')


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            return redirect('/')
    else:
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})


def Register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid:
            form.save()
            print("success")
            return redirect('Login/')
    else:
        form = RegisterationForm()
        print("fail")
        return render(request, 'register.html', {'form': form})
