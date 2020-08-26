from django import forms
from django.core.exceptions import ValidationError

from . import models


class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = [
            "title", "body", "tags"
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "body": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),
            "tags": forms.SelectMultiple(attrs={
                "class": "form-control"
            })
        }

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()

        if new_slug == "create":
            raise ValidationError("You cant create tag 'create'")

        return new_slug


class TagForm(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = ["title", "slug"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control"}
            )
        }

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()

        if new_slug == "create":
            raise ValidationError("You cant create tag 'create'")
        if models.Tag.objects.filter(slug=new_slug).count():
            raise ValidationError(f"Tag '{new_slug}' already created")

        return new_slug
