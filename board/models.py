from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contents = models.CharField(max_length=300)

    def __str__(self):
        return self.title
