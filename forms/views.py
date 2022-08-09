from .forms import RegisterationForm
from django.shortcuts import render
from .models import Template, Social_Link, Terms_n_Condition


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
            ctx = {"template": template, "social": social, "terms": terms}
            return render(request, "success.html", ctx)
        else:
            context = {
                "form": form,
                "template": template,
                "social": social,
                "terms": terms
            }
            return render(request, "index.html", context)
    form = RegisterationForm()
    ctx = {
        "form": form,
        "template": template,
        "social": social,
        "terms": terms
    }
    return render(request, "index.html", ctx)
