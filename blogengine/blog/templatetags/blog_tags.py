from django import template
from .. import models


register = template.Library()


@register.simple_tag
def total_posts():
    return models.Post.objects.count()


@register.simple_tag
def total_tags():
    return models.Tag.objects.count()
