from django.shortcuts import render


# Create your views here.

def main1(request):
    return render(request, 'web/main1.html')

def login(request):
    return render(request, 'web/login.html')


