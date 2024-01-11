from django.http import HttpResponse
from django.template import loader


def shedual(request):
    template=loader.get_template('shedual.html')

    return HttpResponse(template.render())