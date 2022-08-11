from django.urls import path, re_path
from django.urls.conf import include
from .views import redirect_view
from forms.views import index, results


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^adminactions/', include('adminactions.urls')),
    path('results', redirect_view)

]
