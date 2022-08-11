from django.shortcuts import render

from results.models import ResultPage

# Create your views here.


def result(request):
    value = ResultPage.objects.get(default='results')
    if value.show:
        return render(request, 'results.html')
    else:
        return render(request, '404.html')
