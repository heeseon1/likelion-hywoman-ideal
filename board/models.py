from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    contents = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"작성자: {self.author}, 내용: {self.content}"

    #def get_absolute_url(self):
        #return f'/board/{self.post.pk}/#comments-{self.pk}'

    # class Meta:
    #     ordering = ['-id']


