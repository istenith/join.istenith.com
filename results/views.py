from django.shortcuts import render
from results.models import ResultPage, Results

# Create your views here.


def result(request):
    value = ResultPage.objects.get(default='results')
    content = ResultPage.objects.all()
    result = Results.objects.all()
    ctx = {"result": result, "content": content}
    if value.show:
        return render(request, 'results.html', ctx)
    else:
        return render(request, '404.html')
