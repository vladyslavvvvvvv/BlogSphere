from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, DeleteView,UpdateView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from blogsphere_app.forms import CommentForm, CreateupdatePostForm
from blogsphere_app.mixins import UserIsOwnerMixin
from .models import Post,Comment

class Register(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("main-page")
    template_name = "registration/register.html"

class CreatePostView(CreateView, UserIsOwnerMixin):
    model = Post
    form_class = CreateupdatePostForm
    template_name = "blogsphere_app/createpost.html"
    success_url = reverse_lazy("main-page")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        
        return super().form_valid(form)
class PostListView(ListView):
    model = Post
    template_name = "blogsphere_app/mainpage.html"
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    def post(self, request: HttpRequest,  *args, **kwargs):
        if request.user.is_authenticated:

            form = CommentForm(request.POST, request.FILES)
            print("-------------")
            print(request.FILES)
            print("-------------")
            if form.is_valid():
                new_comment: Comment = form.instance
                new_comment.task = self.get_object()
                new_comment.user = self.request.user
                new_comment.save()
        
            return redirect(request.path_info)
        else:
            return HttpResponse("Try to login or register", status=403)



class PostEditView(UpdateView,UserIsOwnerMixin):
    model = Post
    form_class = CreateupdatePostForm
    template_name = "blogsphere_app/createpost.html"
    success_url = reverse_lazy("main-page")

class DeletePostView(DeleteView,UserIsOwnerMixin):
    model = Post
    success_url = reverse_lazy("main-page")

class CommentCreateView(CreateView, UserIsOwnerMixin):
    model = Comment
    form_class = CommentForm
    template_name = "blogsphere_app/create_comment.html"
    success_url = reverse_lazy("main-page")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        

        return super().form_valid(form)
class CommentDeleteView(DeleteView, UserIsOwnerMixin):
    model = Comment
    success_url = reverse_lazy("main-page")
class CommentEditView(UpdateView, UserIsOwnerMixin):
    model = Comment
    form_class = CommentForm
    template_name = "blogsphere_app/edit_comment.html"
    success_url = reverse_lazy("main-page")