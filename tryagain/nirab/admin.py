from django.contrib import admin
from .models import Record, Event, EventVenue, EventAttendee , RecordImage,Record_mail_me,Post,SocialMedia,Medication,MedicationDetails
from .models import Classify_Drug_Class,Classify_Side_Effect,Classify_CONTRADICTIONS

# Register your models here.

admin.site.register(Record)
admin.site.register(EventVenue)
admin.site.register(EventAttendee)
admin.site.register(RecordImage)
admin.site.register(Record_mail_me)
admin.site.register(Post)
admin.site.register(SocialMedia)
admin.site.register(Medication)
admin.site.register(MedicationDetails)
admin.site.register(Classify_Drug_Class)
admin.site.register(Classify_Side_Effect)
admin.site.register(Classify_CONTRADICTIONS)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue')  # Corrected 'title' attribute name
    list_filter = ('date', 'venue')
    ordering = ('-date',)
    search_fields = ('title', 'description')
