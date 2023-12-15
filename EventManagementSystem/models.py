from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# custom_table/models.py

 

class EventOrganizer(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)  # Consider using Django's authentication system
    phone = models.CharField(max_length=20, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    event_proposal = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=20, choices=[
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('cultural', 'Cultural Event'),
        ('sports', 'Sports Event'),
    ])
    event_date = models.DateField(blank=True, null=True)
    event_venue = models.CharField(max_length=100, blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    terms = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname


# models.py

 

class UserRegistration(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    enrollment = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)


    
    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

 