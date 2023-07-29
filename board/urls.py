from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.post_list, name='post_list'),
    path('register/', views.post_register, name='post_register'),
    path('list/<int:pk>', views.post_detail, name='post_detail'),
]