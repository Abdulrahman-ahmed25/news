from django import forms
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    # to make the email unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email = email).count()
        if user_count > 0:
            raise forms.ValidationError("this email already in use")
        return email

    phone_regex = RegexValidator( regex = r'^\+201[0125]{1}[0-9]{8}$', message ="Phone number must be entered in the format +201********. Up to 14 digits allowed.")
    phone_number= forms.CharField(validators =[phone_regex], max_length=13, required=True)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        user_count = User.objects.filter(phone_number = phone_number).count()
        if user_count > 0:
            raise forms.ValidationError("this phone_number already in use")
        return phone_number
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'password1',
            'password2' ]
