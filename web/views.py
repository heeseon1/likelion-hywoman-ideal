from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from .models import User

# 로그인 페이지 + 로그인한 유저라면 button페이지로 이동
def login(request):
    if request.user.is_authenticated:
        if request.user.category == True:
            return redirect('web:button01_true')
        else:
            return redirect('web:button02')
    else:
        return render(request, 'web/login.html')

@login_required
def main1(request):
    if request.user.category == True:
        return redirect('web:button01_true')
    else:
        return render(request, 'web/main1.html')

# 봉사자 값 부여
def button02(request):
    user = request.user
    user.category = False
    user.save()
    return render(request, 'web/button02.html')

# 장애인 값 부여
def button01_true(request):
    user = request.user
    user.category = True
    user.save()
    return render(request, 'web/button01.html')

# 마이 페이지 > 설정
def setting_page(request):
    return render(request, 'web/setting.html')

# 유저 탈퇴 기능
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('web:login')
    return render(request, 'web/setting.html')