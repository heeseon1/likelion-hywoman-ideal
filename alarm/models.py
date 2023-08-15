from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class alarm_push(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 알람을 받을 사용자
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_pushes')  # 알람을 보낸 사용자
    content = models.CharField(max_length=200)  # 알람 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 알람 생성 시간

    def __str__(self):
        return self.content