from django.urls import path
from django.urls.conf import include

from forms.views import index

urlpatterns = [
    path('', index, name='index' ) 
]
