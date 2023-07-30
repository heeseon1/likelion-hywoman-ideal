from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', main1, name='main1'),
    path('login/', login, name='login'),
]