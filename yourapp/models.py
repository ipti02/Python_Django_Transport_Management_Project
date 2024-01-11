# yourapp/models.py
from django.db import models

class Student(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/')
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    bus_route = models.CharField(max_length=50, choices=[('route1', 'Route 1'), ('route2', 'Route 2')])

    def __str__(self):
        return self.student_name
