from django import forms
#from django.db import forms
from django.forms import fields
from .models import Farmacia

class FarmaciaForm(forms.ModelForm):
    class Meta:     
        model = Farmacia
        fields = ['fica_id', 'nombre', 'direccion']
