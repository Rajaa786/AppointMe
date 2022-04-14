from enum import unique
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .manager import CustomUserManager
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Create your models here.


class MyUser(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(
        _("Phone No"), max_length=12, blank=False, unique=True, default=0000000000)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.username)
