from django.contrib import admin
from .models import Record, Event, EventVenue, EventAttendee

# Register your models here.

admin.site.register(Record)
admin.site.register(EventVenue)
# admin.site.register(EventAttendee)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue')  # Corrected 'title' attribute name
    list_filter = ('date', 'venue')
    ordering = ('-date',)
    search_fields = ('title', 'description')

@admin.register(EventAttendee)
class EventAttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name', 'email', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'email', 'phone')
    
