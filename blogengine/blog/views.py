from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from . import models


def posts_list(request):
    posts = models.Post.objects.order_by("-date_pub")
    context = {
        "posts": posts
    }
    return render(request, "blog/posts.html", context=context)


def post_details(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    context = {
        "post": post
    }
    return render(request, "blog/post_details.html", context=context)


def tags_list(request):
    tags = models.Tag.objects.all()
    context = {
        "tags": tags
    }
    return render(request, "blog/tags.html", context=context)


def tag_details(request, slug):
    tag = get_object_or_404(models.Tag, slug=slug)
    context = {
        "tag": tag
    }
    return render(request, "blog/tag_details.html", context=context)
