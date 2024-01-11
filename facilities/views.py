from django.http import HttpResponse
from django.template import loader


def facilities(request):
    template=loader.get_template('facilities.html')

    return HttpResponse(template.render())