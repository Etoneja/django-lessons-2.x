from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.posts_list, name="blog"),
    path("<slug:slug>/", views.post_details, name="details")
]
