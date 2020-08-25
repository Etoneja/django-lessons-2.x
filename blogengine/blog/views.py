from django.views.generic import DetailView, ListView

from . import models


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
