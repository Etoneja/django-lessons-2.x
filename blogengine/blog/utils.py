from django.utils.text import slugify
from time import time


def get_slug(s):
    return f"{slugify(s)}-{str(int(time()))}"
