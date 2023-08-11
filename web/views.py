from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import User

# 로그인 페이지 + 로그인한 유저라면 button페이지로 이동
def login(request):
    if request.user.is_authenticated:
        if request.user.category == True:
            return redirect('web:button01_true')
        else:
            return redirect('web:button01')
    else:
        return render(request, 'web/login.html')

def main1(request):
    return render(request, 'web/main1.html')

# 봉사자 값 부여
def button01(request):
    user = request.user
    user.category = False
    user.save()
    return render(request, 'web/button01.html')

# 장애인 값 부여
def button01_true(request):
    user = request.user
    user.category = True
    user.save()
    return render(request, 'web/button01.html')

