
from django import forms
import random
from rh.models import Uf_Unidade_Federativa, Sexo
from gestao_escolar.models import (Alunos, Alunos_Documentacao, Etnia, Nacionalidade,
                                     Pais_origem, Deficiencia_aluno)
                                     

choices = {
    ('1','A+'),
    ('2','A-'),
    ('3','B+'),
    ('4','B-'),
    ('5','AB+'),
    ('6','AB-'),
    ('7','O+'),
    ('8','O-'),    
    ('0','Não informado')
}


class Alunos_form(forms.ModelForm):

    nome_completo = forms.CharField(
        label='Nome Social (Se possuir):',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
    )

    nome_social = forms.CharField(
        label='Nome Social (Se possuir):',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )   


    idade = forms.CharField(
        label='Nome Social (Se possuir):',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    sexo = forms.ModelChoiceField(
        label='Sexo:',
        queryset=Sexo.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    data_nascimento = forms.DateField(
        label='Data de Nascimento:',
        widget=forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col2 m-2 rounded-1', 'type': 'date'}),        
    )
    etnia = forms.ModelChoiceField(
        queryset=Etnia.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    tel_celular_aluno = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control  border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=True
    )
    email = forms.CharField(        
        widget=forms.EmailInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    nome_mae = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
    )
    tel_celular_mae = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control  border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    nome_pai = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    
    tel_celular_pai = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    naturalidade = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
    )
    nacionalidade = forms.ModelChoiceField(
        queryset=Nacionalidade.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    pais_origem = forms.ModelChoiceField(
        queryset=Pais_origem.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    data_entrada_no_pais = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col2 m-2 rounded-1', 'type': 'date'}),      
        required=False  
    )
    documento_estrangeiro = forms.CharField(        
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    deficiencia_aluno = forms.ModelChoiceField(
        queryset=Deficiencia_aluno.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    )
    tipo_sanguineo = forms.ChoiceField(
    choices=choices,
    widget=forms.Select(attrs={'class': ' border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False
    )

    beneficiario_aux_Brasil = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )

    necessita_edu_especial = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    
    sindrome_de_Down = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    quilombola = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    irmao_gemeo  = forms.BooleanField(   
    label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
    widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
    required=False        
    )
    vacina_covid_19  = forms.BooleanField(   
        label='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil',
        widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False        
    )
    dose_vacina_covid_19 = forms.IntegerField(        
        widget=forms.NumberInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    ) 
    class Meta:
        model = Alunos
        fields = '__all__'
        exclude = ['idade', 'aluno_inativo']


choice_estado_civil = {
    ('1', 'Solteiro'),
    ('2', 'Casado'),
    ('3', 'Separado'),
    ('4', 'Divorciado'),
    ('5', 'Viúvo'),
    ('6', 'União Estável'),
}

choice_modelo_certidao = {
    ('1', 'Antigo'),
    ('2', 'Novo'),
    ('3', 'Nenhuma')
}


class Aluno_documento_form(forms.ModelForm):

    
    def __init__(self, *args, **kwargs):
        aluno_create = kwargs.pop('aluno_create', None)
        super().__init__(*args, **kwargs)

        if aluno_create is not None:
            self.fields['aluno'].queryset = aluno_create
            self.fields['aluno'].initial = aluno_create.first()

    
    class Meta:
        model = Alunos_Documentacao
        fields = "__all__"

    aluno = forms.ModelChoiceField(
        queryset=Alunos.objects.none(),
        widget=forms.Select(attrs={'class': 'border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1',  'readonly': 'readonly'}),
    ) 
    CPF = forms.CharField(
        label='Número do CPF',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    RG = forms.CharField(
        label='Número do RG',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    RG_emissao = forms.DateField(
        label = "Data de emissão do RG",
        widget= forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )

    RG_UF = forms.ModelChoiceField(
        label="UF do RG",
        queryset=Uf_Unidade_Federativa.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),  
        required=False   
    )
    orgao_emissor = forms.CharField(
        label="Órgão Emissor",
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    renda_familiar = forms.CharField(
        label='Renda Familiar',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    situacao_familiar = forms.CharField(
        label='Situação Familiar',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    login_aluno = forms.CharField(
        label='Login',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        
    )
   
    senha = forms.CharField(
        label='Senha do aluno',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    cartao_nacional_saude_cns = forms.CharField(
        label='Cartão Nacional de Saúde / CNS',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    nis = forms.CharField(
        label='NIS',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    inep = forms.CharField(
        label='INEP',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    estado_civil = forms.ChoiceField(
        label='Estado Civil',
        choices=choice_estado_civil,
        widget=forms.Select(attrs={'class': ' border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    tipo_certidao = forms.ChoiceField(
        label='Tipo de Certidão',
        choices=choice_modelo_certidao,
        widget=forms.Select(attrs={'class': ' border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    numero_certidao = forms.CharField(
        label='Número da Certidão',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    livro = forms.CharField(
        label='Livro',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    folha = forms.CharField(
        label='Folha',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    termo = forms.CharField(
        label='Termo',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    emissao = forms.DateField(
        label = "Data de emissão do RG",
        widget=forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col2 m-2 rounded-1', 'type': 'date'}),      
        required=False 
    )
    distrito_certidao = forms.CharField(
        label='Distrito',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    cartorio = forms.CharField(
        label='Cartório',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    comarca = forms.CharField(
        label='Comarca',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    cartorio_uf = forms.ModelChoiceField(
        label="UF do Cartório",
        queryset = Uf_Unidade_Federativa.objects.all(),
        widget=forms.Select(attrs={'class': ' border border-info p-2 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False        
    )
    
    justificativa_falta_documento = forms.CharField(
        label='Justificativa da falta de documentação',
        widget=forms.TextInput(attrs={'class': ' border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    local_diferenciado = forms.CharField(
        label='Local Diferenciado',
        widget=forms.TextInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False
    )
    obito  = forms.BooleanField(   
        label='Óbito / Falecimento do aluno',
        widget = forms.CheckboxInput(attrs={'class': 'border border-info p-1 pb-1 bg-transparent text-info col m-2 rounded-1'}),
        required=False        
    )
    data_obito = forms.DateField(
        label = "Data óbito / Data de Falecimento",
        widget= forms.DateInput(attrs={'class': 'form-control border border-info p-3 pb-3 bg-transparent text-info col m-2 rounded-1'}),
        required=False  
    )

    


        
        

      




