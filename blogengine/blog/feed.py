from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse

from . import models


class LatestPostFeed(Feed):

    title = "My Blog"
    link = "/blog/"
    description = "New posts of my blog."

    def items(self):
        return models.Post.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

