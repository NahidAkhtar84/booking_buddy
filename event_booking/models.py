from django.db import models

from django.db import models
from colorfield.fields import ColorField
from django import forms

STATUS_CHOICE = (
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected')
)

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='default event')
    username = models.CharField(max_length=255, default='user')
    phone = models.CharField(max_length=20, default='123456789')
    email = models.CharField(max_length=400, null=True, blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    status = models.CharField(default='pending', max_length=100, choices=STATUS_CHOICE)
    color = ColorField(default='#FF0000')
    textcolor = ColorField(default='#000000')

    def __str__(self):
        return self.name