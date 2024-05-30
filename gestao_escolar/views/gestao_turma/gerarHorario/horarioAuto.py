from django.shortcuts import render
from gestao_escolar.models import TurmaDisciplina, HorarioAula
from gestao_escolar.utils import gerar_horario_auto
from django.http import HttpResponse, HttpResponseBadRequest

def gerar_horario(request):
    if request.method == 'POST':
        turmas_disciplinas = TurmaDisciplina.objects.all()
        gerar_horario_auto(turmas_disciplinas)
        return HttpResponse('Horário gerado com sucesso!')
    else:
        return HttpResponseBadRequest('Método não permitido')
