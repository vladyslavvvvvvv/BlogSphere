from django.contrib import admin

from blogsphere_app.models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)