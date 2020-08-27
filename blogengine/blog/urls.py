from django.urls import path

from . import views
from .feed import LatestPostFeed

app_name = "blog"

urlpatterns = [

    path("", views.PostListView.as_view(), name="posts"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("posts/<slug:slug>/", views.PostDetailsView.as_view(), name="post_details"),

    path("tags/", views.TagsListView.as_view(), name="tags"),
    path("tags/create", views.TagCreateView.as_view(), name="tag_create"),
    path("tags/<slug:slug>/update", views.TagUpdateView.as_view(), name="tag_update"),
    path("tags/<slug:slug>/delete", views.TagDeleteView.as_view(), name="tag_delete"),
    path("tags/<slug:slug>/", views.TagDetailsView.as_view(), name="tag_details"),

    path("search/", views.SearchView.as_view(), name="search"),

    path("feed", LatestPostFeed(), name="post_feed")

]
