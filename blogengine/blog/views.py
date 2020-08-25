from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    DetailView, ListView, CreateView, View
)

from . import models
from . import forms


class PostListView(ListView):
    model = models.Post
    template_name = "blog/posts.html"

    def get_queryset(self):
        return self.model.objects.order_by("-date_pub")


class PostDetailsView(DetailView):
    model = models.Post
    template_name = "blog/post_details.html"


class TagsListView(ListView):
    model = models.Tag
    template_name = "blog/tags.html"


class TagDetailsView(DetailView):
    model = models.Tag
    template_name = "blog/tag_details.html"


class TagCreateView(CreateView):
    form_class = forms.TagForm
    template_name = "blog/tag_form.html"


class PostCreateView(CreateView):
    form_class = forms.PostForm
    template_name = "blog/post_form.html"
