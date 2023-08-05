from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# 그냥 카테고리 필드를 추가하니까 admin 페이지에서 확인이 안 되길래
# 요렇게 바꿨습니다.... 죄삼다!........
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'id', 'category']

admin.site.register(User, CustomUserAdmin)
