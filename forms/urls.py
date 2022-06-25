from django.urls import path
from django.urls.conf import include

from forms.views import indexe
from forms import views

urlpatterns = [
    path('', indexe, name='index' ),
    path('form/', views.Form.as_view(), name='form'),
    path('add_user/', views.user_add, name='add_user'),
]
