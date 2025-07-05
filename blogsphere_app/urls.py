from django.urls import path


from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("main/page/", views.PostListView.as_view(), name="main-page"),
    path("post/detail/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.CreatePostView.as_view(), name="post-create"),
    path("register/", views.Register.as_view(), name="register")
      ]