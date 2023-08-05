from django.shortcuts import render, redirect, get_object_or_404

from .models import User


def login(request):
    return render(request, 'web/login.html')

def main1(request):
    return render(request, 'web/main1.html')


# 장애인 값 부여
def button01_true(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.category = True
    user.save()
    return render(request, 'web/button01.html', {'user': user})


# 봉사자 값 부여
def button01(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.category = False
    user.save()
    return render(request, 'web/button01.html', {'user': user})


