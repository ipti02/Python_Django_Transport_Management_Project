# models.py
from django.db import models

class YourModel(models.Model):
    # Define your fields
    SL = models.IntegerField()
    Name = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Email = models.EmailField()
    # Add more fields as needed
