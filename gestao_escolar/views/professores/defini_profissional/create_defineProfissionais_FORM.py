from django import forms
from gestao_escolar.models import Profissionais, Encaminhamentos, Cargo

class Form_defineProfissionais(forms.ModelForm):
    class Meta:
        model =  Profissionais
        fields = "__all__" 

    nome = forms.ModelChoiceField(
        queryset=Encaminhamentos.objects.none(),
        widget=forms.Select(attrs={'class':'border border-info p-3 pb-3 bg-transparent text-info  m-2 rounded-1 col-9'})               
    )    
    cargo = forms.ModelChoiceField(
        queryset=Cargo.objects.all(),        
        widget=forms.Select(attrs={'class':' border border-info p-3 pb-3 bg-transparent text-info col-8 m-2 rounded-1'})    
#widget=forms.DateInput(attrs={'class':  'type': 'date'}), 
    )
    area_especializacao = forms.CharField(        
        widget=forms.TextInput(attrs={'class':' border border-info p-3 pb-3 bg-transparent text-info col-7 m-2 rounded-1'})      
    )

    def __init__(self, *args, **kwargs):
        nome_query = kwargs.pop('nome_query', None)
        super().__init__(*args, **kwargs)

        if nome_query is not None:
            self.fields['nome'].queryset = nome_query
            self.fields['nome'].initial = nome_query.first()

            # para pegar o nome completo e adicionar ao select
            self.fields['nome'].label_from_instance = lambda obj: f'{obj.encaminhamento.contratado.nome} {obj.encaminhamento.contratado.sobrenome}'




            """
            
               # Atualize o rótulo do campo 'nome' para exibir o nome completo
            self.fields['nome'].label_from_instance..label_from_instance  = lambda obj: f'{obj.nome} {obj.sobrenome}'
            
            """