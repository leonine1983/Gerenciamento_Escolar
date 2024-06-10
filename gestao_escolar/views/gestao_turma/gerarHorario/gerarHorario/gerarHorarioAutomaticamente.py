"""from django import forms
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from gestao_escolar.models import Horario, Turmas, Periodo, Validade_horario
from .forms import HorarioForm

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'validade']   

    def __init__(self, *args, **kwargs):
        validade_ativa = kwargs.pop('validade_ativa', None)
        super().__init__(*args, **kwargs)
        if validade_ativa:
            self.fields['validade'].required = False
            self.fields['validade'].initial = validade_ativa
            self.fields['validade'].widget = forms.HiddenInput()  # Esconder o campo no formulário, se necessário


class HorarioCreateView(View):
    template_name = 'Escola/inicio.html'

    def get(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        validade_ativa = Validade_horario.objects.filter(horario_ativo=True).first()

        forms_periodos = [(HorarioForm(initial={'turma': turma, 'periodo': periodo}, prefix=str(periodo.id), validade_ativa=validade_ativa), periodo) for periodo in periodos]
        context = {
            'forms_periodos': forms_periodos,
            'turma': turma,
            'conteudo_page': "Gestão Turmas - GerarHorario",
            'horarios': Horario.objects.filter(turma=turma)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        validade_ativa = Validade_horario.objects.filter(horario_ativo=True).first()
        
        forms = [HorarioForm(request.POST, prefix=str(periodo.id), validade_ativa=validade_ativa) for periodo in periodos]

        if all(form.is_valid() for form in forms):
            for form in forms:
                periodo_id = request.POST.get(f'{form.prefix}-periodo')
                periodo = get_object_or_404(Periodo, pk=periodo_id)
                horario_instance = form.save(commit=False)
                horario_instance.turma = turma
                horario_instance.periodo = periodo
                horario_instance.validade = validade_ativa
                horario_instance.save()
            messages.success(request, 'Horários atualizados com sucesso.')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            forms_periodos = [(form, Periodo.objects.get(pk=form.prefix).nome_periodo) for form in forms]
            context = {
                'forms_periodos': forms_periodos,
                'turma': turma,
                'conteudo_page': "Gestão Turmas - GerarHorario",
                'horarios': Horario.objects.filter(turma=turma)
            }
            return render(request, self.template_name, context)

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']})
    
    """
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.forms import modelform_factory
from django.contrib import messages
from gestao_escolar.models import Turmas, Horario, TurmaDisciplina, Periodo, DiaSemana, Validade_horario
from ortools.sat.python import cp_model

def alocar_aulas(request, turma_id):
    turma = get_object_or_404(Turmas, id=turma_id)
    turmas_disciplinas = TurmaDisciplina.objects.filter(turma=turma)
    periodos = Periodo.objects.all()
    dias_semana = DiaSemana.objects.all()

    if request.method == "POST":
        form = modelform_factory(Horario, exclude=[])
        for field in request.POST:
            if 'turma_disciplina' in field:
                turma_disciplina_id = request.POST[field]
                dia_semana_id = request.POST[field.replace('turma_disciplina', 'dia_semana')]
                periodo_id = request.POST[field.replace('turma_disciplina', 'periodo')]

                turma_disciplina = get_object_or_404(TurmaDisciplina, id=turma_disciplina_id)
                dia_semana = get_object_or_404(DiaSemana, id=dia_semana_id)
                periodo = get_object_or_404(Periodo, id=periodo_id)

                conflito = Horario.objects.filter(
                    turma_disciplina__professor=turma_disciplina.professor,
                    dia_semana=dia_semana,
                    periodo=periodo
                ).exclude(turma=turma)

                if conflito.exists():
                    messages.error(request, f'O professor {turma_disciplina.professor} já está alocado no período {periodo.nome_periodo} de {dia_semana.nome_dia} na turma {conflito.first().turma.nome}')
                    return redirect('alocar_aulas', turma_id=turma_id)

                count_dia = Horario.objects.filter(
                    turma_disciplina=turma_disciplina,
                    dia_semana=dia_semana
                ).count()

                count_semana = Horario.objects.filter(
                    turma_disciplina=turma_disciplina
                ).count()

                if count_dia >= turma_disciplina.quant_aulas_dia:
                    messages.error(request, f'O limite de aulas por dia para a disciplina {turma_disciplina.disciplina.nome} foi alcançado.')
                    return redirect('alocar_aulas', turma_id=turma_id)

                if count_semana >= turma_disciplina.quant_aulas_semana:
                    messages.error(request, f'O limite de aulas por semana para a disciplina {turma_disciplina.disciplina.nome} foi alcançado.')
                    return redirect('alocar_aulas', turma_id=turma_id)

                Horario.objects.update_or_create(
                    turma=turma,
                    dia_semana=dia_semana,
                    periodo=periodo,
                    defaults={'turma_disciplina': turma_disciplina}
                )

        messages.success(request, 'Horários atualizados com sucesso!')
        return redirect('alocar_aulas', turma_id=turma_id)
    
    # Filtragem de horários por período e dia para passar para o template
    horarios_filtrados = {}
    for periodo in periodos:
        horarios_filtrados[periodo] = {}
        for dia in dias_semana:
            horarios_filtrados[periodo][dia] = periodo.horarios.filter(dia_semana=dia, turma=turma).first()

    context = {
        'conteudo_page': "Gestão Turmas - GerarHorario",
        'turma': turma,
        'turmas_disciplinas': turmas_disciplinas,
        'periodos': periodos,
        'dias_semana': dias_semana,
        'horarios_filtrados': horarios_filtrados,  # Passando os horários filtrados para o template
    }
    return render(request, 'Escola/inicio.html', context)

