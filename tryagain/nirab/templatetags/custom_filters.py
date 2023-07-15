from django import template
from ..models import RecordImage , Record, SocialMedia
from ..forms import SocialMediaForm

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
    
@register.simple_tag
def get_record(user):
    try:
        record = Record.objects.get(user=user)
        return record
    except Record.DoesNotExist:
        return None





@register.simple_tag
def add_or_update_social_media(user):
    try:
        social_media = SocialMedia.objects.get(user=user)
        form = SocialMediaForm(instance=social_media)
    except SocialMedia.DoesNotExist:
        form = SocialMediaForm(initial={'user': user})  # Set the initial value of 'user' field
    
    form.user = user  # Set the user attribute of the form
    
    return form


