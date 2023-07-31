from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('create/<int:board_id>/', views.comment_create, name='comment_create'),
    # 다른 URL 패턴들
]
