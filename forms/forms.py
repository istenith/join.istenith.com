from django import forms
from .models import Registeration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = "__all__"
