from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def blog_static(file_name):
    return "%s%s" % (settings.BLOG_STATIC_URL, file_name)
