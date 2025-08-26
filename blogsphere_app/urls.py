from django.urls import path


from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("main/page/", views.PostListView.as_view(), name="main-page"),
    path("post/detail/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.CreatePostView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", views.DeletePostView.as_view(), name="delete-view"),
    path("post/edit/<int:pk>", views.PostEditView.as_view(), name="post-edit"),
    path("register/", views.Register.as_view(), name="register"),
    path("create/comment/", views.CommentCreateView.as_view(),name="create-comment"),
    path("user/list/", views.UserListView.as_view(),name="user-list"),
    path("user/detail/<int:pk>",views.UserDetailView.as_view(),name="user-detail")
      ]