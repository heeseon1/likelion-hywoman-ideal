# Generated by Django 3.2.20 on 2023-08-17 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='available_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.availabledate'),
        ),
        migrations.AddField(
            model_name='review',
            name='help_seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_seeker_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post'),
        ),
        migrations.AddField(
            model_name='availabledate',
            name='time_slots',
            field=models.ManyToManyField(to='board.TimeSlot'),
        ),
        migrations.AddField(
            model_name='availabledate',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_dates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alarm_push',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_alarm', to='board.post'),
        ),
        migrations.AddField(
            model_name='alarm_push',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_push_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alarm_push',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_push_user', to=settings.AUTH_USER_MODEL),
        ),
    ]