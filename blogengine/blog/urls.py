from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [

    path("", views.PostListView.as_view(), name="posts"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/", views.PostDetailsView.as_view(), name="post_details"),
    path("tags/", views.TagsListView.as_view(), name="tags"),
    path("tags/create", views.TagCreateView.as_view(), name="tag_create"),
    path("tags/<slug:slug>/", views.TagDetailsView.as_view(), name="tag_details"),

]
