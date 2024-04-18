from django import forms
from gestao_escolar.models import Disciplina, Turmas, Encaminhamentos, TurmaDisciplina, Profissionais

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 


class Diciplina_Grade_form (forms.ModelForm):
    
    
    turma = forms.ModelChoiceField(
        #label='Nome da Turma:',
        queryset = Turmas.objects.none(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    ) 
    disciplina= forms.ModelChoiceField(
        #label='Nome da Turma:',
        queryset = Disciplina.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )   
    professor= forms.ModelChoiceField(
        #label='Nome da Turma:',
        queryset = Profissionais.objects.none(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )  
    carga_horaria_anual= forms.CharField(
        #label='Nome da Turma:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )    
    limite_faltas= forms.CharField(
        #label='Nome da Turma:',
        widget=forms.TextInput(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info m-2 rounded-1 w-75'}),
    )  

    def __init__(self, *args, **kwargs):
            query_turma = kwargs.pop('turmas_query', None)
            query_professor = kwargs.pop('professor_query', None)
            super().__init__(*args, **kwargs)
            
            if query_turma is not None:
                self.fields['turma'].queryset = query_turma
                self.fields['turma'].initial = query_turma.first()
                self.fields['professor'].queryset= query_professor
                self.fields['professor'].initial= query_professor.first() 

    class Meta:
        model = TurmaDisciplina
        fields =['turma', 'disciplina', 'professor', 'carga_horaria_anual', 'limite_faltas']
    


