from django.shortcuts import render
from results.models import ResultPage, Results

# Create your views here.


def result(request):
    value = ResultPage.objects.get(default='results')
    result = Results.objects.all()
    ctx = {"result": result}
    if value.show:
        return render(request, 'results.html', ctx)
    else:
        return render(request, '404.html')
