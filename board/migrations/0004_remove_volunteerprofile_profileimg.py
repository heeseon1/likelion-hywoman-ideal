# Generated by Django 3.2.20 on 2023-08-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_volunteerprofile_profileimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='profileimg',
        ),
    ]