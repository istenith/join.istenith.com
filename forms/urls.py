from django.urls import path, re_path
from django.urls.conf import include

from forms.views import index, result


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^adminactions/', include('adminactions.urls')),
    path('results', result, name= 'result' ),
]
