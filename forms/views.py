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
def error_404_view(request, exception):
    return render(request, '404.html')
def error_500_view(request):
    return render(request, '500.html')



def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            context = {'form': form}
            return render(request, 'index.html', context)
    form = RegistrationForm()
    return render(request, 'index.html', {'form': form})
