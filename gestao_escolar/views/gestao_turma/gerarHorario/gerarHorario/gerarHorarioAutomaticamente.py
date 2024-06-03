from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from gestao_escolar.models import Horario, TurmaDisciplina, Periodo, Turmas
from django import forms

from django.forms import ModelChoiceField

class HorarioForm(ModelForm):
    segunda = ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    terca = ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quarta = ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quinta = ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    sexta = ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)

    class Meta:
        model = Horario
        fields = '__all__'


def create_or_update_horario(request, turma_id, horario_id=None):
    turma = get_object_or_404(Turmas, pk=turma_id)
    
    if horario_id:
        horario = Horario.objects.get(pk=horario_id)
    else:
        horario = Horario(turma=turma)
    
    if request.method == "POST":
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            horario_instance = form.save(commit=False)
            professor_conflito = None
            turma_conflito = None

            # Verifica conflito de professor no mesmo período e turno
            for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
                turma_disciplina = getattr(horario_instance, dia)
                if turma_disciplina:
                    conflito = Horario.objects.filter(
                        periodo=horario_instance.periodo,
                        turno=horario_instance.turno,
                    ).exclude(pk=horario_instance.pk).filter(
                        **{f'{dia}': turma_disciplina}
                    ).first()

                    if conflito:
                        professor_conflito = turma_disciplina.professor
                        turma_conflito = conflito.turma
                        break

            if professor_conflito:
                messages.warning(
                    request, 
                    f"O professor {professor_conflito} já está cadastrado no horário {horario_instance.periodo} no turno {horario_instance.turno} na turma {turma_conflito}."
                )
            else:
                horario_instance.save()
                messages.success(request, "Horário salvo com sucesso.")
                return redirect('create_horario', turma_id=turma_id)
        else:
            messages.error(request, f"Erro ao salvar o formulário: {form.errors}")
    else:
        # Carregar os períodos existentes
        periodos = Periodo.objects.all()

        # Verifica se já existe um horário para essa turma e preenche o formulário com os dados existentes
        horarios_existente = Horario.objects.filter(turma=turma)
        if horarios_existente.exists():
            # Aqui, ao invés de pegar o primeiro horário, você deveria pegar o último
            ultimo_horario = horarios_existente.last()
            form = HorarioForm(instance=ultimo_horario)
            form.fields['periodo'].initial = ultimo_horario.periodo
        else:
            form = HorarioForm(instance=horario)

    horarios = Horario.objects.filter(turma=turma)  # Carrega todos os horários existentes para a turma
    
    return render(request, 'Escola/inicio.html', {'turma_id':turma_id,'form': form, 'horarios': horarios, 'periodos': periodos, 'conteudo_page': "Gestão Turmas - GerarHorario", 'turma': turma})
