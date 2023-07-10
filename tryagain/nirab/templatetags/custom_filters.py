from django import template
from ..models import RecordImage

register = template.Library()

@register.simple_tag
def check_allowed_image_count(user):
    i_c_record = RecordImage.objects.filter(user=user).first()
    if i_c_record:
        remaining_image_count = i_c_record.allowed_image_count
        if remaining_image_count > 0:
            return True
        else:
            return False
    else:
        return False
