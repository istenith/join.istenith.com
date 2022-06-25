from django.shortcuts import render
from django.views import View
from forms.models import User

# Create your views here.


def indexe(request):
    return render(request, 'form.html')


# Create your views here.
class Form(View):
    template = "form_one.html"

    def get(self, request):
        

        return render(request, self.template)

    
def user_add(request):
    if(request.method=="POST"):
            name = request.POST.get('name')
            rollno = request.POST.get('rollno')
            branch = request.POST.get('branch')
            email = request.POST.get('email')
            reason = request.POST.get('reason')
            skills = request.POST.get('skills')

            user = User(name=name, email=email, rollno= rollno, branch=branch, reason=reason,skills=skills)
            user.save()
    
    return render(request,"success.html")