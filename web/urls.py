from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', login, name='login'),
    path('main1/', main1, name='main1'),
    # 봉사자
    path('button01/<int:pk>/', button01, name='button01'),
    # 장애인
    path('button01_true/<int:pk>/', button01_true, name='button01_true'),
]
