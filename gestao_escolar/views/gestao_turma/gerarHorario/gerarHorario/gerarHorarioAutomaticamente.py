from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from constraint import Problem, AllDifferentConstraint
from gestao_escolar.models import TurmaDisciplina, Turmas, Horario, Periodo

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import HorarioForm
from django.contrib import messages

from django import forms
from gestao_escolar.models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['turma','disciplina', 'periodo', 'turno', 'segunda', 'terca', 'quarta', 'quinta', 'sexta']


def gerar_contexto_dinamico():
    # Busca todos os periodos
    periodos = Periodo.objects.all()
    # Cria um dicionário para armazenar os contextos
    context = {}
    # Itera sobre os períodos e filtra os horários correspondentes
    for periodo in periodos:
        nome_periodo = periodo.nome_periodo
        context[nome_periodo] = Horario.objects.filter(periodo=periodo.id)
    return context

def GerarHorarioView(request, id=None):
    if id:
        horario = get_object_or_404(Horario, id=id)
    else:
        horario = None

    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            new_horario = form.save(commit=False)
            conflicts = []

            # Verifica conflitos para cada dia da semana
            for day in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
                turma_disciplina = getattr(new_horario, day)
                if turma_disciplina:
                    periodo = new_horario.periodo
                    professor = turma_disciplina.professor

                    # Verifica se há um horário existente com o mesmo professor no mesmo período
                    conflict = Horario.objects.filter(
                        periodo=periodo,
                        **{day: turma_disciplina}
                    ).exclude(id=new_horario.id).first()
                    
                    if conflict:
                        conflicts.append((day, conflict.turma))

            if conflicts:
                conflict_messages = ", ".join([f"{day.capitalize()} em {turma}" for day, turma in conflicts])
                messages.warning(request, f"O professor já está cadastrado no(s) seguinte(s) horário(s): {conflict_messages}")
            else:
                new_horario.save()
                return redirect('horario_list')  # Redireciona para a lista de horários ou outra view desejada

    else:
        form = HorarioForm(instance=horario)

    return render(request, 'Escola/inicio.html', {'form': form, 'horario': horario, 'conteudo_page': "Gestão Turmas - GerarHorario"})