from django import forms
from .models import Profile, phone_regex
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def email_exist(value):
    if User.objects.filter(email=value).exists():
        return forms.ValidationError("Profile with this Email Address already exists")

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(validators=[email_exist])
    class Meta:
        model = User
        fields  =['username','email']

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=17,validators=[phone_regex])
    
    class Meta:
        model = Profile
        fields = ['phone_number']