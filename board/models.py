from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    contents = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"작성자: {self.author.username if self.author else '알 수 없음'}, 내용: {self.content}"

    #def get_absolute_url(self):
        #return f'/board/{self.post.pk}/#comments-{self.pk}'

    # class Meta:
    #     ordering = ['-id']


##봉사자프로필
class VolunteerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    available_dates = models.ManyToManyField('AvailableDate', blank=True)

    def __str__(self):
        return self.user.username


#리뷰
class Review(models.Model):
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='volunteer_reviews', on_delete=models.CASCADE)
    help_seeker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='help_seeker_reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.volunteer.username} - {self.help_seeker.username}'

#가능한 날짜와 시간대
class AvailableDate(models.Model):
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='available_dates', on_delete=models.CASCADE)
    date = models.DateField()
    time_slots = models.ManyToManyField('TimeSlot')

    def __str__(self):
        return f'{self.volunteer.username} - {self.date}'

#시간대
class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    available_date = models.ForeignKey(AvailableDate, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


#메시지
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'From {self.sender} to {self.recipient}'

    class Meta:
        ordering = ['timestamp']


#알람

User = get_user_model()

class alarm_push(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarm_push_user')  # 알람을 받을 사용자
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarm_push_sender')  # 알람을 보낸 사용자
    content = models.CharField(max_length=200)  # 알람 내용
    post = models.ForeignKey('board.Post', on_delete=models.CASCADE, related_name='post_alarm', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 알람 생성 시간

    def __str__(self):
        return self.content