from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegisterationForm(UserCreationForm):
    class Meta():
        model = MyUser
        fields = ('username', 'email', 'phone')


class LoginForm(UserCreationForm):
    class Meta():
        model = MyUser
        fields = ('email',)
