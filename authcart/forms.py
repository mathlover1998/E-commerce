from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Row,Column
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.forms.widgets import SelectDateWidget
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

class UpdateProfileForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),

    ]
    # username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'disabled':True,'class': 'form-control'}))
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email Address',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget())
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    DoB = forms.DateField(label='Date of Birth',widget=SelectDateWidget)
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number',
        })



# class UpdateProfileForm(forms.ModelForm):
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('unknown', 'Unknown'),
#     ]
#     phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget())
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#     DoB = forms.DateField(label='Date of Birth',widget=SelectDateWidget)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'phone_number', 'gender', 'DoB']
#         widgets = {
#             'username': forms.TextInput(attrs={'disabled': 'disabled','class': 'form-control'}),
#             'first_name':forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            
#         }
