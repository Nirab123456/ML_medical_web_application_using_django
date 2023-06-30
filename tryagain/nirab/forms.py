from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



#1st way to create form
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



class eventrecord(forms.ModelForm):
    event_name = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}))
    event_date = forms.DateField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}))
    event_time = forms.TimeField(required=True,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Time'}))
    # event_location = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Location'}))
    # event_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_description = forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Description'}))
    event_image = forms.ImageField(required=True,label="",widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Event Image'}))

    class Meta:
        model = Record
        fields = ['event_name','event_date','event_time','event_location','event_description','event_image']
        widgets = {
            'event_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'event_time': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Time'}),
            'event_location': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Location'}),
            'event_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Description'}),
            'event_image': forms.FileInput(attrs={'class':'form-control','placeholder':'Event Image'}),
        }

class event_location(forms.ModelForm):
    name=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    address=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    zipcode=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}))
    phone=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    email=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    website=forms.CharField(required=True,max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website'}))
    class Meta:
        model=Event_location
        fields=['name','address','zipcode','phone','email','website']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'website':forms.TextInput(attrs={'class':'form-control','placeholder':'Website'}),
        }





# #2nd way to create form
# class addrecord(forms.ModelForm):
#     class Meta:
#         model = Record
#         fields = ['first_name','last_name','email','phone','address','country','city','zipcode']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
#             'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
#             'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
#             'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
#             'country': forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),
#             'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
#             'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
#         }