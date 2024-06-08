from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.views.generic import CreateView
from gestao_escolar.models import Horario, Validade_horario, Turmas
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from django import forms
from django.core.exceptions import ValidationError

from django import forms
from django.core.exceptions import ValidationError
from gestao_escolar.models import Validade_horario, Turmas


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from gestao_escolar.models import Validade_horario, Turmas


class HorarioCriaForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    nome_validade = forms.CharField(label="Defina um nome para o horário ex.: Horário Geral")
    turma = forms.ModelChoiceField(queryset=Turmas.objects.none())  # Adicionando o campo 'turma' como um ModelChoiceField

    class Meta:
        model = Validade_horario
        fields = ['data_inicio', 'data_fim', 'nome_validade', 'turma', 'horario_ativo']

    def __init__(self, *args, **kwargs):
        initial_turma = kwargs.pop('initial_turma', None)
        queryset_turma = Turmas.objects.filter(pk=initial_turma.id) if initial_turma else Turmas.objects.none()
        super().__init__(*args, **kwargs)
        self.fields['turma'].queryset = queryset_turma
        if initial_turma:
            self.fields['turma'].initial = initial_turma

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        if data_inicio and data_fim and data_fim < data_inicio:
            raise ValidationError("A data de término não pode ser anterior à data de início.")
        return cleaned_data


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conteudo_page'] = "Gestão Turmas - DefineValidadeHorario"
        return context

    def form_valid(self, form):
        data_inicio = form.cleaned_data['data_inicio']
        data_fim = form.cleaned_data['data_fim']
        turma = form.cleaned_data['turma']
        horarios_vigentes = Validade_horario.objects.filter(turma=turma, data_fim__gte=data_inicio, data_inicio__lte=data_fim)

        if horarios_vigentes.exists():
            mensagem = "Já existe um horário vigente no período especificado. Se desejar adicionar um novo horário para esta data, é necessário reduzir o período de vigência do horário existente."
            form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList()).append(mensagem)
            return self.form_invalid(form)
        
        if form.cleaned_data['horario_ativo']:
            Validade_horario.objects.filter(turma=turma, horario_ativo=True).update(horario_ativo=False)
        
        messages.success(self.request, "O período de validade foi criado com sucesso. Você acaba de ser redirecionado para a criação do horário das turmas.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']})
