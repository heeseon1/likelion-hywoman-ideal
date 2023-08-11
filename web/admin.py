from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

# class CustomUserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class CustomUserAdmin(UserAdmin):
    # form = CustomUserUpdateForm
    list_display = ['username', 'id', 'category', 'is_active']

admin.site.register(User, CustomUserAdmin)
