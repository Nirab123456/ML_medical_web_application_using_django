from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.dispatch import receiver





class Classify_Drug_Class(models.Model):
    group = models.CharField(max_length=100)
    indication = models.CharField(max_length=100)
    drug_class = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.drug_class






class Classify_Side_Effect(models.Model):
    generic_name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    indication = models.CharField(max_length=200)
    side_effect = models.TextField(max_length=1000)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.generic_name







class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=200)
    strength = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    price_analysis = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class MedicationDetails(models.Model):
    generic_name = models.TextField(max_length=500)
    drug_class = models.TextField(max_length=500)
    indication = models.TextField(max_length=500)
    indication_description = models.TextField(max_length=500)
    therapeutic_class_description = models.TextField(max_length=500)
    pharmacology_description = models.TextField(max_length=500)
    dosage_description = models.TextField(max_length=500)
    interaction_description = models.TextField(max_length=500)
    contraindications_description = models.TextField(max_length=500)
    side_effects_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.generic_name
    






















class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records', null=True)
    photo = models.ImageField(upload_to='images/profile/', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





class RecordImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', null=True)
    image = models.ImageField(upload_to='images/')
    image_count = models.IntegerField(default=0)
    allowed_image_count = models.IntegerField(default=5)
    def __str__(self):
        return f'{self.user}'

@receiver(post_save, sender=RecordImage)
def update_image_count(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance already exists
        try:
            old_instance = RecordImage.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:  # Check if the image field has changed
                instance.image_count = old_instance.image_count + 1  # Increment the count by 1
        except RecordImage.DoesNotExist:
            pass  # Handle the case if the old instance doesn't exist yet
    else:  # New instance is being created
        instance.image_count += 1  # Increment the count by 1 for new instance

@receiver(post_save, sender=RecordImage)
def reduce_allowed_image_count(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = RecordImage.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                instance.allowed_image_count = old_instance.allowed_image_count - 1
        except RecordImage.DoesNotExist:
            pass
    else:
        instance.allowed_image_count -= 1




class Record_mail_me(models.Model):
    TOPIC_CHOICES = [
        ('HIRE_ME', 'HIRE ME'),
        ('CONTACT_ME', 'CONTACT ME'),
        ('COLLABORATION', 'COLLABORATION REQUEST'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    topic = models.CharField(max_length=100, default='CONTACT_ME', choices=TOPIC_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.topic}'


class Event(models.Model):
    title = models.CharField(max_length=100)
    mannager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()
    # venue = models.CharField(max_length=100)
    venue = models.ForeignKey('EventVenue', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class EventVenue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    website = models.URLField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class EventAttendee(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.record.first_name



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
# i will change the name of this model  next time i work on this project
class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_media', null=True)
    website = models.URLField(max_length=200,blank=True)
    facebook = models.URLField(max_length=200,blank=True)
    instagram = models.URLField(max_length=200,blank=True)
    twitter = models.URLField(max_length=200,blank=True)
    linkedin = models.URLField(max_length=200,blank=True)
    github = models.URLField(max_length=200,blank =True)
    upwork = models.URLField(max_length=200,blank=True)
    discord = models.URLField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.user}'

