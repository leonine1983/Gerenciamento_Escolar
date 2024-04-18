from django import forms
from gestao_escolar.models import Turmas, Serie_Escolar

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 

turno = {
    ('Matutino', 'Matutino'),
    ('Verspertino', 'Verspertino'),
    ('Noturno', 'Noturno')
}

class Turma_form(forms.ModelForm):
    
    nome = forms.CharField(
        #label='Nome da Turma:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )
    serie = forms.ModelChoiceField(
        queryset= Serie_Escolar.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-50'}),
    ) 
    turno = forms.ChoiceField(
        choices= turno,
        widget= forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-50'})
    )  
    quantidade_vagas = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-25'})
    )
   
    
    class Meta:
        model = Turmas
        fields =['nome', 'turno', 'turma_multiserie', 'serie']

