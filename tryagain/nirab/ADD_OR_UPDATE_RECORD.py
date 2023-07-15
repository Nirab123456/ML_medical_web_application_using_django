from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  addrecord , SocialMediaForm
from .models import Record ,SocialMedia







class ADD_OR_UPDATE_record:
    def __init__(self,request):
        self.request = request

    def add_or_update_record(self):
        request=self.request
        social_media_form = self.social_media_form_view()  # Capture the returned HTML

        record =  Record.objects.filter(user=request.user).first()
        if record and record.photo:
            photo_url = record.photo.url
            if request.method == 'POST':
                form = addrecord(request.POST, instance=record)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Record Updated Successfully')
                    return redirect('profile')
            else:
                form = addrecord(instance=record)
            return render(request, 'add_or_update_record.html', {'add_or_update_record_form': form, 'photo_url': photo_url, 'social_media': social_media_form})  # Pass the captured HTML to the template
        else:
            if request.method == 'POST':
                form = addrecord(request.POST)
                if form.is_valid():
                    record = form.save(commit=False)
                    record.user = request.user
                    record.save()
                    messages.success(request, 'Record Added Successfully')
                    return redirect('profile')
            else:
                form = addrecord()

            return render(request, 'add_or_update_record.html', {'add_or_update_record_form': form, 'social_media': social_media_form})  # Pass the captured HTML to the template


    def social_media_form_view(self):
        request=self.request
        record = SocialMedia.objects.filter(user=request.user).first()
        if record:
            if request.method == 'POST':
                form = SocialMediaForm(request.POST, instance=record)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Social Media Links Updated Successfully')
                    return redirect('profile')
            else:
                form = SocialMediaForm(instance=record)
            return form
        else:
            if request.method == 'POST':
                form = SocialMediaForm(request.POST)
                if form.is_valid():
                    record = form.save(commit=False)
                    record.user = request.user
                    record.save()
                    messages.success(request, 'Social Media Links Added Successfully')
                    return redirect('profile')
            else:
                form = SocialMediaForm()
            return form

