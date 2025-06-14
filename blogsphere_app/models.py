from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    describition = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="file/",blank=True, null=True)
    class Meta:
        ordering=["pub_date"]
        verbose_name = "post"
        verbose_name_plural = "posts"

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_file = models.FileField(upload_to="comment_file/", blank=True, null=True)
    class Meta: 
        ordering=["pub_date"]
        verbose_name = "comment"
        verbose_name_plural = "comments"