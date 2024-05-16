from django import forms
from gestao_escolar.models import Disciplina, Turmas, Encaminhamentos, TurmaDisciplina, Profissionais

# widget personalizado que usa as classes (form-control, border, p-3, pb-3 e bg-transparent) para ser atribuido ao campo 'tempo_meses' 


class Diciplina_Grade_form (forms.ModelForm):
    
    
    turma = forms.ModelChoiceField(
        label='Turma:',
        queryset = Turmas.objects.none(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1  text-info m-2 rounded-1 w-75'}),
    ) 
    disciplina= forms.ModelChoiceField(
        label='Selecione a Disciplina:',
        queryset = Disciplina.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1  text-info m-2 rounded-1 w-75'}),
    )   
    professor= forms.ModelChoiceField(
        label='Selecione o professor:',
        queryset = Profissionais.objects.none(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1  text-info m-2 rounded-1 w-75'}),
    )  
    professor2= forms.ModelChoiceField(
        label='Selicione o professor se houver necessidade de atribuir mais um professor na turma:',
        queryset = Profissionais.objects.none(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1  text-info m-2 rounded-1 w-75'}),
        required=False
    ) 
    auxiliar_classe= forms.ModelChoiceField(
        label='Selicione os auxiliares de classe, se houver necessidade:',
        queryset = Profissionais.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1  text-info m-2 rounded-1 w-75'}),
        required=False
    ) 
    carga_horaria_anual= forms.CharField(
        label='Carga horária anual da disciplina:',
        widget=forms.NumberInput(attrs={'class': ' border border-info p-1 pb-1 text-info m-2 rounded-1 '}),
    )    
    limite_faltas= forms.CharField(
        label='Atribua o número máximo de faltas que o aluno pode ter na disciplina e não ser reprovado:',
        widget=forms.NumberInput(attrs={'class': 'border border-info p-1 pb-1  text-info m-2 rounded-1'}),
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
                self.fields['professor2'].queryset= query_professor
                self.fields['professor2'].initial= query_professor.first() 

    class Meta:
        model = TurmaDisciplina
        fields =['turma', 'disciplina', 'professor', 'carga_horaria_anual', 'limite_faltas']
    


