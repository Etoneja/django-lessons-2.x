from django import template
from django.utils.safestring import mark_safe
from markdown import markdown

from .. import models


register = template.Library()


@register.simple_tag
def total_posts():
    return models.Post.objects.count()


@register.simple_tag
def total_tags():
    return models.Tag.objects.count()


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown(text))
