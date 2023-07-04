from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records', null=True)
    photo = models.ImageField(upload_to='images/profile/',null=True,blank=True)
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
    def __str__(self):
        return f'{self.user}'
    

class Record_mail_me(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    

    
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
