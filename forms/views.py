from .forms import RegisterationForm
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Template, Social_Link, Terms_n_Condition, Results


def error_404_view(request, exception):
    return render(request, "404.html")


def error_500_view(request):
    return render(request, "500.html")


def index(request):
    template = Template.objects.all()
    social = Social_Link.objects.all()
    terms = Terms_n_Condition.objects.all()

    if request.method == "POST":
        form = RegisterationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html", {"template": template})
        else:
            context = {"form": form, "template": template}
            return render(request, "index.html", context)
    form = RegisterationForm()
    return render(request, "index.html", {"form": form, "template": template, "social": social, "terms": terms})


def results(request):
    results = Results.objects.all()
    if request.method == "Post":
        return render(request, "results.html")

    return render(request, "400.html")


def redirect_view(request):
    response = redirect('index')
    return response
