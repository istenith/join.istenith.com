from .forms import RegistrationForm
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
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html", {"template": template})
        else:
            context = {"form": form, "template": template}
            return render(request, "index.html", context)
    form = RegistrationForm()
    return render(request, "index.html", {"form": form, "template": template, "social": social, "terms": terms})
