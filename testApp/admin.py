from django.contrib import admin

from testApp.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.unregister(User)
admin.site.register(MyUser, UserAdmin)
