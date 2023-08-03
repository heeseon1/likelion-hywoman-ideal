from django.shortcuts import render, redirect
from .models import User


# Create your views here.

def main1(request):
    return render(request, 'web/main1.html')

def login(request):
    return render(request, 'web/login.html')

def button01(request):
    return render(request, 'web/button01.html')

