from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),

    ]
    full_name = models.CharField(max_length=200, null=False,default='')
    email_verified = models.BooleanField(null=False,default=0)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=20,null=False,default=GENDER_CHOICES[2])
    phone = PhoneNumberField(null=False,default = '')
    DoB = models.DateField(default='1900-01-01')
    

    class Meta:
        db_table = 'User'

class Address(models.Model):
    city = models.CharField(max_length=100, null=False,default='')
    country = models.CharField(max_length=100, null=False,default='')
    address = models.CharField(max_length=200, null=False,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_address'

