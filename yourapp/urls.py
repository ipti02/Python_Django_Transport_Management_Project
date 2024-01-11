# yourapp/urls.py
from django.urls import path
from .views import student_form, profile

urlpatterns = [
    path('form/', student_form, name='student_form'),
    path('profile/', profile, name='profile'),
]
