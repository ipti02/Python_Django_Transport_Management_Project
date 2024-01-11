from django.urls import path
from.import views
from .views import your_view

urlpatterns=[
    path('information/',views.your_view,name='your view'),
]