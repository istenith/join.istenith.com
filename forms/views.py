from http.client import HTTPResponse
from urllib.request import Request
from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.


def index(request):
    # form = RegistrationForm(request.POST,request.FILES)
    # # if form.is_valid():
    # print(form)
    # registeration = form.save()
    # registeration.save()
    #     # return HTTPResponse("form saved")
    # # else:
    # context = {'form':form}
    # print(" index views")

    if request.method=="POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save()
            return HTTPResponse("form ")
        else:
            print("not valid")
    else:
        form = RegistrationForm()
        print("not post")
    return render(request, 'form.html', {'form':form})


# def submit(request):
#     # form = RegistrationForm(request.POST,request.FILES)
#     # # if form.is_valid():
#     # print(form)
#     # registeration = form.save()
#     # registeration.save()
#     #     # return HTTPResponse("form saved")
#     # # else:
#     # context = {'form':form}
#     # print(" index views")

#     if request.method=="POST":

#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form = form.save()
#             return HTTPResponse("form ")
#         else:
#             print("form not valid")
    
#     return render(request, 'form.html', {'form':form})