from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        "tag", blank=True, related_name="posts"
    )

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={
            "slug": self.slug
        })

    def __str__(self):
        return f"{self.title}"


class Tag(models.Model):

    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("blog:tag_details", kwargs={
            "slug": self.slug
        })

    def __str__(self):
        return f"{self.title}"
