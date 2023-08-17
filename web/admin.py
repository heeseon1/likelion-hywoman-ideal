from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'id', 'category', 'is_active','warning']

admin.site.register(User, CustomUserAdmin)

