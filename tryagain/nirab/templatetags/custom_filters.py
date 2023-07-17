from django import template
from ..models import RecordImage , Record, SocialMedia , Medication
from ..forms import SocialMediaForm

register = template.Library()

@register.simple_tag
def check_allowed_image_count(user):
    i_c_record, created = RecordImage.objects.get_or_create(user=user)
    if created:
        # Set initial values for the newly created instance
        i_c_record.image_count = 0
        i_c_record.allowed_image_count = 5
        i_c_record.save()

    remaining_image_count = i_c_record.allowed_image_count
    return remaining_image_count > 0
    
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

@register.simple_tag
def social_media_link(user):
    try:
        social_media = SocialMedia.objects.get(user=user)
        return social_media
    except SocialMedia.DoesNotExist:
        return None


@register.simple_tag
def get_medication(strength):
    try:
        medication = Medication.objects.get(strength=strength)
        print("Medication found:", medication)
        return medication
    except Medication.DoesNotExist:
        print("Medication not found")
        return None
