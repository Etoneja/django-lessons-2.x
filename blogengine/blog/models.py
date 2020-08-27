from django.db import models
from django.urls import reverse
from .utils import get_slug


class Post(models.Model):

    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        "tag", blank=True, related_name="posts"
    )

    class Meta:
        ordering = ["-date_pub"]

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={
            "slug": self.slug
        })

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):

    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("blog:tag_details", kwargs={
            "slug": self.slug
        })

    def __str__(self):
        return f"{self.title}"
