from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.posts_list, name="posts"),
    path("posts/<slug:slug>/", views.post_details, name="post_details"),
    path("tags/", views.tags_list, name="tags"),
    path("tags/<slug:slug>/", views.tag_details, name="tag_details")
]
