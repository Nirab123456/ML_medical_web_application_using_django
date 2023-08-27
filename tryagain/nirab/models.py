from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.dispatch import receiver



class PHENOMONIA_PREDICTION(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phenomonia_prediction', null=True)
    image = models.ImageField(upload_to='images/phenomonia_prediction/', null=True, blank=True)
    prediction = models.CharField(max_length=200, null=True, blank=True)
    image_count = models.IntegerField(default=0)
    allowed_image_count = models.IntegerField(default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user}'








"""INDICATION_DESCRIPTION:all the use cases of{G_N}? ==A_T_U_C
side effect description :all side effects of {G_N}? == A_S_E_C
pharmacological description:all mechanism of action {G_N}? == A_M_O_C
interaction description :what to avoid when using {G_N}? == W_T_A_D_C
interaction description :what  meal or food to avoid when using {G_N}? == W_T_A_F_C

contradiction description :in which cases not to take  {G_N}? == I_W_C_N_T_T_C
"""

class SELECTED_QUESTION_ANSWER(models.Model):
    generic_name = models.CharField(max_length=200)
    A_T_U_C = models.CharField(max_length=200)
    A_S_E_C = models.CharField(max_length=200)
    A_M_O_C = models.CharField(max_length=200)
    W_T_A_D_C = models.CharField(max_length=200)
    W_T_A_F_C = models.CharField(max_length=200)
    I_W_C_N_T_T_C = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.generic_name


class MENTAL_HEALTH_PREDICTION_MODEL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mental_health_prediction_model', null=True)
    id = models.CharField(max_length=200, primary_key=True)
    admiration = models.CharField(max_length=200)
    amusement = models.CharField(max_length=200)
    anger = models.CharField(max_length=200)
    annoyance = models.CharField(max_length=200)
    approval = models.CharField(max_length=200)
    caring = models.CharField(max_length=200)
    confusion = models.CharField(max_length=200)
    curiosity = models.CharField(max_length=200)
    desire = models.CharField(max_length=200)
    disappointment = models.CharField(max_length=200)
    disapproval = models.CharField(max_length=200)
    disgust = models.CharField(max_length=200)
    embarrassment = models.CharField(max_length=200)
    excitement = models.CharField(max_length=200)
    fear = models.CharField(max_length=200)
    gratitude = models.CharField(max_length=200)
    grief = models.CharField(max_length=200)
    joy = models.CharField(max_length=200)
    love = models.CharField(max_length=200)
    nervousness = models.CharField(max_length=200)
    optimism = models.CharField(max_length=200)
    pride = models.CharField(max_length=200)
    realization = models.CharField(max_length=200)
    relief = models.CharField(max_length=200)
    remorse = models.CharField(max_length=200)
    sadness = models.CharField(max_length=200)
    surprise = models.CharField(max_length=200)
    neutral = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user}'
    




class PERSONAL_DIARY(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_diary', null=True)
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    content = models.TextField(blank=True,null=True,max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title











class med_Ques_Ans(models.Model):
    name = models.CharField(blank=True, null=True,max_length=100)
    generic_name = models.CharField(blank=True, null=True,max_length=200)
    question = models.TextField(blank=True, null=True,max_length=1000)
    answer = models.TextField(blank=True, null=True,max_length=1000)
    corrected_answer = models.TextField(blank=True, null=True,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.generic_name









class Presciption_drug_class(models.Model):
    generic_name = models.CharField(max_length=200)
    drug_class = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
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




class handwritten_text_model(models.Model):
    text_handwritten = models.TextField(max_length=5000)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.text_handwritten