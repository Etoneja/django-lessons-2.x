from django.contrib.sitemaps import Sitemap

from . import models


class PostSitemap(Sitemap):

    changefreq = 'weekly'
    priority = .9

    def items(self):
        return models.Post.objects.all()

    @staticmethod
    def lastmod(obj):
        return obj.updated
