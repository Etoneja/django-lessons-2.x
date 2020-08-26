from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, ListView,
    CreateView, UpdateView,
    DeleteView
)

from . import models
from . import forms


class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return self.model.objects.order_by("-date_pub")


class PostDetailsView(DetailView):
    model = models.Post


class TagsListView(ListView):
    model = models.Tag


class TagDetailsView(DetailView):
    model = models.Tag


class TagCreateView(CreateView):
    model = models.Tag
    form_class = forms.TagForm


class TagUpdateView(UpdateView):
    model = models.Tag
    form_class = forms.TagForm


class TagDeleteView(DeleteView):
    model = models.Tag
    success_url = reverse_lazy("blog:tags")


class PostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:posts")
