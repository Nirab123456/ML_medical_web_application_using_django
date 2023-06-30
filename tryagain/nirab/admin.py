from django.contrib import admin
from .models import Record,Event,EventVenue,EventAttendee

# Register your models here.


admin.site.register(Record)
admin.site.register(Event)
admin.site.register(EventVenue)
admin.site.register(EventAttendee)
