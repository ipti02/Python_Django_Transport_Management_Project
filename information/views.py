from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import YourModel


def information(request):
    template=loader.get_template('information.html')

    return HttpResponse(template.render())





def your_view(request):
    data = YourModel.objects.all()
    return render(request, 'your_template.html', {'data': data})
