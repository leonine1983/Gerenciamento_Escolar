from gestao_escolar.models import Horario, Turmas
from django.shortcuts import render, redirect

def criaIdHorarioTurma(request, turma_id):
    turma = Turmas.objects.get(id=turma_id)

    # Verifica se existe algum horário para essa turma
    horario = Horario.objects.filter(turma=turma).first()
    
    if not horario:
        # Se não houver nenhum horário, cria um novo
        novo_horario = Horario.objects.create(turma=turma)
        return redirect('Gestao_Escolar:criarHorarioUpdate', pk=novo_horario.id)
    else:
        return redirect('Gestao_Escolar:criarHorarioUpdate', pk=horario.id)
