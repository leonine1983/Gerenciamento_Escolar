from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.views.generic import CreateView
from gestao_escolar.models import Horario, Validade_horario, Turmas
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django import forms
from django.core.exceptions import ValidationError

class HorarioCriaForm(forms.ModelForm):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    nome_validade = forms.CharField(
        label= "Defina um nome para o horário ex.: Horário Geral"
    )
    turma = forms.ModelChoiceField(queryset=Turmas.objects.none())  # Adicionando o campo 'turma' como um ModelChoiceField

    class Meta:
        model = Validade_horario
        fields = ['data_inicio', 'data_fim', 'nome_validade', 'turma']

    def __init__(self, *args, **kwargs):
        # Obtendo o valor inicial para o campo 'turma'
        initial_turma = kwargs.pop('initial_turma', None)
        queryset_turma = Turmas.objects.filter(pk=initial_turma.id) if initial_turma else Turmas.objects.none()

        super().__init__(*args, **kwargs)

        # Definindo o queryset para o campo 'turma'
        self.fields['turma'].queryset = queryset_turma

        # Definindo o valor inicial para o campo 'turma', se existir
        if initial_turma:
            self.fields['turma'].initial = initial_turma

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if data_inicio and data_fim and data_fim < data_inicio:
            raise ValidationError("A data de término não pode ser anterior à data de início.")

        return cleaned_data




from django.views.generic.edit import FormMixin
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic.edit import CreateView

class CriaValidadeHorario(CreateView):
    model = Validade_horario
    form_class = HorarioCriaForm
    template_name = 'Escola/inicio.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        turma_id = self.kwargs.get('turma_id')
        turma = get_object_or_404(Turmas, pk=turma_id)
        kwargs['initial_turma'] = turma
        return kwargs

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['conteudo_page'] = "Gestão Turmas - DefineValidadeHorario"
        return context
    
    def form_valid(self, form):
        # Verifica se já existe um horário vigente no período especificado
        data_inicio = form.cleaned_data['data_inicio']
        data_fim = form.cleaned_data['data_fim']
        turma = form.cleaned_data['turma']
        horarios_vigentes = Validade_horario.objects.filter(turma=turma, data_fim__gte=data_inicio, data_inicio__lte=data_fim)

        if horarios_vigentes.exists():
            mensagem = "Já existe um horário vigente no período especificado. Se desejar adicionar um novo horário para esta data, é necessário reduzir o período de vigência do horário existente."
            form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, ErrorList()).append(mensagem)
            return self.form_invalid(form)
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criar_horario')
