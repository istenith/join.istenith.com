from http.client import HTTPResponse
from urllib.request import Request
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.


# def index(request):
#     form = RegistrationForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#     else:
#         print('form is not working')
#     return render(request, 'form.html', {'form': form})

def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'base.html')
        else:
            context = {'form': form}
            return render(request, 'form.html', context)
    form = RegistrationForm()
    return render(request, 'form.html', {'form': form})
