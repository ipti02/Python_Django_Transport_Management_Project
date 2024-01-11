# admin.py
from django.contrib import admin
from .models import FemaleModel
from .models import MaleModel


admin.site.register(FemaleModel)
admin.site.register(MaleModel)