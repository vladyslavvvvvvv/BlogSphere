from django import forms

from .models import Comment, Post

class CreateupdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["user"]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", "comment_file")