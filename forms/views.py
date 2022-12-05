from .forms import RegisterationForm
from django.shortcuts import render
from .models import FAQ, FormPlaceholder, Template, Social_Link, Terms_n_Condition
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string 


def error_404_view(request, exception):
    return render(request, "404.html")


def error_500_view(request):
    return render(request, "500.html")


def index(request):
    template = Template.objects.all()
    social = Social_Link.objects.all()
    terms = Terms_n_Condition.objects.all()
    placeholder = FormPlaceholder.objects.all()
    faq = FAQ.objects.all()
    if request.method == "POST":
        form = RegisterationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ctx = {
                "template": template,
                "social": social,
                "terms": terms,
                'faq': faq,
            }
            emailTemplate= render_to_string('email_template.html')
            sendEmail= EmailMessage(
              'subject',
               emailTemplate,
               settings.EMAIL_HOST_USER,
               ['swastkk@gmail.com']
            )
            sendEmail.fail_silently= False
            sendEmail.send()
            return render(request, "success.html", ctx)
        else:
            context = {
                'placeholder': placeholder,
                'faq': faq,
                "form": form,
                "template": template,
                "social": social,
                "terms": terms
            }
            return render(request, "index.html", context)
    form = RegisterationForm()
    ctx = {
        'faq': faq,
        'placeholder': placeholder,
        "form": form,
        "template": template,
        "social": social,
        "terms": terms
    }

    return render(request, "index.html", ctx)


def filedownload(request, filename):
    zf = zipfile.ZipFile('download.zip', 'w', zipfile.ZIP_DEFLATED)
    zf.write("media/" + filename)
    response = HttpResponse(zf, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="download.zip"'
    return response
