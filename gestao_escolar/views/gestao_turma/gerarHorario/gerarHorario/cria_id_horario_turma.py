from django.shortcuts import render, redirect
from gestao_escolar.models import Horario, Periodo
from .forms import HorarioForm
from gestao_escolar.models import Turmas  # Adicione o import do modelo Turma

def gerar_horario(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    periodos = Periodo.objects.all()
    horarios = []

    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            for periodo in periodos:
                horario = Horario(turma=turma, periodo=periodo)
                # Preencha os campos segunda, terca, etc. com base nos dados do formulário
                horarios.append(horario)
            return render(request, 'Escola/inicio.html', {'horarios': horarios})
    else:
        form = HorarioForm()

    return render(request, 'nome_da_template.html', {'form': form, 'conteudo_page': 'Gestão Turmas - GerarHorario'})
