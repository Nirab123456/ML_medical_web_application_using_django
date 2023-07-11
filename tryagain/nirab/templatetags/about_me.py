from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def about_me(file_name):
    return "%s%s" % (settings.ABOUT_ME_URL, file_name)
