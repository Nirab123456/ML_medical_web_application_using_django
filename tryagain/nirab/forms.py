from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, PasswordChangeForm, 
                                       PasswordResetForm, SetPasswordForm, AuthenticationForm)
from django.contrib.auth.models import User 
from django import forms
from .models import Record, Event, EventVenue, EventAttendee,RecordImage,Record_mail_me,SocialMedia,Medication,handwritten_text_model,MENTAL_HEALTH_PREDICTION_MODEL,PERSONAL_DIARY,PHENOMONIA_PREDICTION
from django.forms import ModelForm




class phenomonia_prediction_form(forms.ModelForm):
    image = forms.ImageField(required=True,label="",widget=forms.FileInput(attrs={'class':'form-control'}))
    prediction = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prediction'}))
    class Meta:
        model = PHENOMONIA_PREDICTION
        fields = ['image','prediction']
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
            'prediction': forms.TextInput(attrs={'class':'form-control','placeholder':'Prediction'}),
        }










class PERSONAL_DIARY_FORM(forms.ModelForm):
    id = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ID'}))
    title = forms.TextInput(attrs={'class':'form-control','placeholder':'Title'})
    content = forms.TextInput(attrs={'class':'form-control','placeholder':'Content'})
    class Meta:
        model = PERSONAL_DIARY
        fields = ['id','title','content']











class MedicineForm(ModelForm):
    name = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Medicine Name'}))
    generic_name = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Generic Name'}))
    class Meta:
        model = Medication
        fields = ['name','generic_name']






class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))



    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    new_password1 = forms.CharField(max_length=100,label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(max_length=100,label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

        



class SocialMediaForm(forms.ModelForm):
    website = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website'}))
    facebook = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook'}))
    instagram = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Instagram'}))
    twitter = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Twitter'}))
    linkedin = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Linkedin'}))
    github = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Github'}))
    upwork = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Upwork'}))
    discord = forms.CharField(required=False,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Discord'}))
    class Meta:
        model = SocialMedia
        fields = ['website','facebook','instagram','twitter','linkedin','github','upwork','discord']
        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control'}),
            'upwork': forms.TextInput(attrs={'class': 'form-control'}),
            'discord': forms.TextInput(attrs={'class': 'form-control'}),
        }






class Mail_me_Form(forms.ModelForm):
    TOPIC_CHOICES = [
        ('HIRE_ME', 'HIRE ME'),
        ('CONTACT_ME', 'CONTACT ME'),
        ('COLLABORATION', 'COLLABORATION REQUEST'),
    ]

    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    message = forms.CharField(max_length=100, label="", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}))
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, label="", widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Record_mail_me
        fields = ['name', 'email', 'message', 'topic']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
        }




class addrecord(forms.ModelForm):
    first_name = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone = forms.CharField(required=True,max_length=15,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    address = forms.CharField(required=True,max_length=200,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    country = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}))
    city = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    zipcode = forms.CharField(required=True,max_length=10,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}))
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','country','city','zipcode']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'country': forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
        }


class profilepicForm(forms.ModelForm):
    photo = forms.ImageField(required=True,label="",widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Record
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class':'form-control','placeholder':'Photo'}),
        }






class VenueForm(ModelForm):
    class Meta:
        model = EventVenue
        fields = ['name', 'address', 'zipcode', 'phone', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'website': forms.URLInput(attrs={'class':'form-control','placeholder':'Website'}),
        }

        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'venue', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Title'}),
            'date': forms.DateInput(attrs={'class':'form-control','placeholder':'Date'}),
            'time': forms.TimeInput(attrs={'class':'form-control','placeholder':'Time'}),
            'venue': forms.Select(attrs={'class':'form-control','placeholder':'Venue'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),        
            }


# class OCRImageForm(ModelForm):
#     image = forms.FileInput
#     class Meta:
#         model = RecordImage
#         fields = ['image']
#         widgets = {
#             'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
#         }

class OCRImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))
    class Meta:
        model = RecordImage
        fields = ['image']  # Specify the fields you want to include in the form

class handwritten_text_form(forms.ModelForm):
    text_handwritten = forms.TextInput(attrs={'class':'form-control','placeholder':'Handwritten Text'})
    class Meta:
        model = handwritten_text_model
        fields = ['text_handwritten']



