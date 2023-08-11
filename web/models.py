from django.db import models
from allauth.socialaccount.signals import social_account_added
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    # False가 봉사자/ True가 장애인
    category = models.BooleanField(default=False)
    # 봉사자 레벨
    level = models.IntegerField(default=0)
    # 봉사자 경험치
    #experience = models.SmallIntegerField(default=0)
    # 활동 활성화 여부
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.username



@receiver(social_account_added)  # 소셜로그인 계정 추가시 실행
def social_username(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    if not user.username and sociallogin.account.provider in ['google', 'kakao', 'naver']:
        user.username = sociallogin.account.extra_data.get('name')
        user.save()
