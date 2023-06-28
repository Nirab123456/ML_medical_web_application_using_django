from django.db import models

# Create your models here.


class record(models.Model):
    created_act = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    zip_code = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')