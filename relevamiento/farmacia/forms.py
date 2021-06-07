from django import forms
#from django.db import forms
from django.forms import fields, widgets
from .models import Farmacia, Fcia, Provincia, Programa

class FarmaciaForm(forms.ModelForm):
    class Meta:     
        model = Farmacia
        fields = ['fica_id', 'nombre', 'direccion']

class ProvinciaForm(forms.ModelForm):
    class Meta:     
        model = Provincia
        fields = ['id_provincia', 'descripcion']
        widgets={
            'id_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'id' : 'id_provincia',
            'descripcion' : 'nombre de la provincia'
        }

class ProgramaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Programa
        
        fields = ['programa','nombre','version','fecha_install']

        widgets = {
            'programa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_install': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'programa': 'id del programa',
            'nombre': 'nombre del programa',
            'version': 'version del programa actual',
            'fecha_install': 'fecha de instalacion'
        }         


# class FciaForm(forms.ModelForm):
#     class Meta:
#         model = Fcia
#         fields = ['','','','']
