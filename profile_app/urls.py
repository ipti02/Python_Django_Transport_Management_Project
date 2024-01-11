from django.urls import path
from.import views

urlpatterns=[
    path('profile_app/',views.profile_app,name='profile_app'),
]