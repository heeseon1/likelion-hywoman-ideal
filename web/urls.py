from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', login, name='login'),
    path('main1/', main1, name='main1'),
    path('button01/', button01, name='button01'),
    path('button01_true/', button01_true, name='button01_true'),
]
