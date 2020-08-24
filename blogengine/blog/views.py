from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from . import models


def posts_list(request):
    posts = models.Post.objects.order_by("-date_pub")
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context=context)


def post_details(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    context = {
        "post": post
    }
    return render(request, "blog/details.html", context=context)
