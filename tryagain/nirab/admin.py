from django.contrib import admin
from .models import Record, Event, EventVenue, EventAttendee , RecordImage,Record_mail_me,SocialMedia,Medication,MedicationDetails
from .models import med_Ques_Ans,SELECTED_QUESTION_ANSWER,Presciption_drug_class,MENTAL_HEALTH_PREDICTION_MODEL,PERSONAL_DIARY,PHENOMONIA_PREDICTION

# Register your models here.

admin.site.register(Record)
admin.site.register(EventVenue)
admin.site.register(EventAttendee)
admin.site.register(RecordImage)
admin.site.register(Record_mail_me)
admin.site.register(SocialMedia)
admin.site.register(Medication)
admin.site.register(MedicationDetails)
admin.site.register(SELECTED_QUESTION_ANSWER)
admin.site.register(MENTAL_HEALTH_PREDICTION_MODEL)
# admin.site.register(PERSONAL_DIARY)
@admin.register(PERSONAL_DIARY)
class PERSONAL_DIARYAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'id')
    list_filter = ('title', 'content', 'id')
    ordering = ('title',)
    search_fields = ('title', 'content', 'id')

@admin.register(PHENOMONIA_PREDICTION)
class PHENOMONIA_PREDICTIONAdmin(admin.ModelAdmin):
    list_display=('user','image','prediction','created_at')
    list_filter=('user','image','prediction','created_at')
    ordering=('user',)
    search_fields=('user','image','prediction','created_at')
    




#show Presciption_drug_class alpabetically
@admin.register(Presciption_drug_class)
class Presciption_drug_classAdmin(admin.ModelAdmin):
    list_display = ('generic_name', 'heading','drug_class')
    list_filter = ('generic_name', 'heading','drug_class')
    ordering = ('generic_name',)
    search_fields = ('generic_name', 'heading','drug_class')

    



@admin.register(med_Ques_Ans)
class Ques_AnsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')  # Corrected 'title' attribute name
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    search_fields = ('question', 'answer')
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue')  # Corrected 'title' attribute name
    list_filter = ('date', 'venue')
    ordering = ('-date',)
    search_fields = ('title', 'description')
