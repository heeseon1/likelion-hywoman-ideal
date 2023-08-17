from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'board'

urlpatterns = [
    path('community/', views.community.as_view(), name='community'),
    path('community/alarm/', views.alarm_list, name='alarm'),
    path('register/', views.post_register.as_view(), name='post_register'),
    path('list/<int:pk>', views.post_detail.as_view(), name='post_detail'),
    path('list/<int:pk>/update/', views.post_update.as_view(), name='post_update'),
    path('list/<int:pk>/delete/', views.post_delete.as_view(), name='post_delete'),
    # 코멘트 작성
    path("<int:pk>/comment/write/", views.CommentWrite.as_view(), name="cm-write"),
    # 코멘트 삭제,수정
    path("delete/<int:pk>/comment/delete/", views.CommentDelete.as_view(), name="cm-delete"),
    path("comment/update/<int:pk>/", views.CommentUpdate.as_view(), name="cm-update"),
    #매칭 화면#
    path('matching/', views.matching_view, name='matching'),
    path('matching2/', views.matching_view2, name='matching2'),
    #봉사자 등록
    path('register/volunteer/', views.RegisterVolunteerProfileView.as_view(), name='register_volunteer'),
    # 봉사자 프로필 보기
    path('volunteer/<int:pk>/', views.VolunteerProfileView.as_view(), name='volunteer_profile'),
    # 봉사자 목록 보기
    path('volunteer_list/', views.volunteer_list, name='volunteer_list'),
    # 봉사자 리뷰 보기
    path('volunteer/<int:volunteer_id>/reviews/', views.VolunteerReviews.as_view(), name='volunteer_reviews'),
    path('warning/<int:pk>/', views.given_warning, name='given_warning'),
    #메시지
    # path('send-message/<int:recipient_id>/', views.SendMessageView.as_view(), name='send_message'),
    # path('inbox/', views.InboxView.as_view(), name='inbox'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)