from django.urls import path
from django.urls.conf import include

from forms.views import indexe

urlpatterns = [
    path('', indexe, name='index' ) 
]
