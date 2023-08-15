from django.conf import settings
from django.db import models
from allauth.socialaccount.signals import social_account_added
from django.contrib.auth.models import AbstractUser, UserManager
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    # False가 봉사자/ True가 장애인
    category = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return self.username




@receiver(social_account_added)  # 소셜로그인 계정 추가시 실행

def social_username(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    if not user.username and sociallogin.account.provider in ['google', 'kakao', 'naver']:
        user.username = sociallogin.account.extra_data.get('name')
        user.save()


class VolunteerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='volunteer_profile')
    # 봉사자가 선택한 가능한 날짜와 시간대를 저장하는 필드나 관계 설정 추가

class HelpSeekerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='help_seeker_profile')
    # 장애인이 볼 수 있는 정보나 필드 추가