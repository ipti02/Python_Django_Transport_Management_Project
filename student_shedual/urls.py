from django.urls import path
from.import views
from .views import female_view
from .views import male_view


urlpatterns=[
 path('student_shedual/',views.female_view,name='female view'),
 path('student_shedual/',views.male_view,name='male view'),   
]