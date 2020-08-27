from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank
)
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


class SearchView(ListView):
    model = models.Post
    template_name = "blog/search.html"

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search")
        if search:
            search_vector = SearchVector("title", "body")
            search_query = SearchQuery(search)
            self.queryset = self.model.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by("-rank")

        return super().get(request, *args, **kwargs)
