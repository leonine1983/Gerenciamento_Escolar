from django import forms
from django.forms import HiddenInput
from controle_estoque.models import Alimentos

class Forms_alimento(forms.ModelForm):
    class Meta: 
        model= Alimentos
        fields = ['categoria_alimento', 'nome']      

        widgets = {            
            'prefeitura': forms.Select(attrs={'disabled':True}),
            'prefeitura': HiddenInput(),
        }


