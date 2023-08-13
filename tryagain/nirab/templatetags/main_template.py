from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def main_template(file_name):
    return "%s%s" % (settings.MAIN_TAMPLATE_URL, file_name)
