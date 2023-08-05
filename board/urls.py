from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.post_list.as_view(), name='post_list'),
    path('register/', views.post_register.as_view(), name='post_register'),
    path('list/<int:pk>', views.post_detail.as_view(), name='post_detail'),
    path('list/<int:pk>/update/', views.post_update.as_view(), name='post_update'),
    path('list/<int:pk>/delete/', views.post_delete.as_view(), name='post_delete'),
    # 코멘트 작성
    path("<int:pk>/comment/write/", views.CommentWrite.as_view(), name="cm-write"),
    # 코멘트 삭제
    path("delete/<int:pk>/comment/delete/", views.CommentDelete.as_view(), name="cm-delete"),
    path("comment/update/<int:pk>/", views.CommentUpdate.as_view(), name="cm-update"),
]

