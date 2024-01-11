from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import FemaleModel
from .models import MaleModel


def student_shedual(request):
    template=loader.get_template('my_template.html')

    return HttpResponse(template.render())





def female_view(request):
    data = FemaleModel.objects.all()
    return render(request, 'my_template.html', {'data': data})



def male_view(request):
    data = MaleModel.objects.all()
    return render(request, 'my_template.html', {'data': data})