from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import MyUser
from django import forms


class RegisterationForm(UserCreationForm):
    class Meta():
        model = MyUser
        fields = ('username', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus',
                                                     'required': 'required', 'placeholder': 'Enter You Name'})


class LoginForm(forms.ModelForm):
    password_ = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta():
        model = MyUser
        fields = ('email', 'password_')

    def clean(self):
        email = ""
        password = ""
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password_']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Credentials")
