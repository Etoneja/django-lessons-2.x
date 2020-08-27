from django.db.models import Q, Count
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView, ListView,
    CreateView, UpdateView,
    DeleteView
)

from . import models
from . import forms


class PostListView(ListView):
    model = models.Post
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search")
        if search:
            self.queryset = self.model.objects.filter(
                Q(title__icontains=search) | Q(body__icontains=search)
            ).order_by("-date_pub")
            self.extra_context = {
                "search": search
            }
        return super().get(request, *args, **kwargs)


class PostDetailsView(DetailView):
    model = models.Post


class TagsListView(ListView):
    model = models.Tag
    paginate_by = 5

    def get_queryset(self):
        queryset = models.Tag.objects.annotate(
            total_posts=Count("posts")
        ).order_by("-total_posts")
        return queryset


class TagDetailsView(DetailView):
    model = models.Tag


class TagCreateView(LoginRequiredMixin, CreateView):
    model = models.Tag
    form_class = forms.TagForm


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Tag
    form_class = forms.TagForm
    raise_exception = True


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Tag
    success_url = reverse_lazy("blog:tags")
    raise_exception = True


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    form_class = forms.PostForm
    raise_exception = True


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:posts")
    raise_exception = True
