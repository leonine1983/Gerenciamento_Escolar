from django.shortcuts import render, get_object_or_404
from gestao_escolar.models import Turmas, TurmaDisciplina, Horario, Periodo
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

def GerarHorarioView(request, turma_id):
    turma = get_object_or_404(Turmas, pk=turma_id)

    # Obter todas as disciplinas e profissionais associados à turma selecionada
    turma_disciplinas = TurmaDisciplina.objects.filter(turma=turma)
    disciplinas = [td.disciplina for td in turma_disciplinas]
    profissionais = [td.professor for td in turma_disciplinas]

    # Definir os períodos de aula disponíveis (assumindo que já foram criados)
    periodos = Periodo.objects.all()

    # Criar o problema de programação linear
    prob = LpProblem("GerarHorario", LpMaximize)

    # Variáveis de decisão
    horarios = LpVariable.dicts("Horario", ((p.pk, td.pk) for p in periodos for td in turma_disciplinas), cat='Binary')

    # Função objetivo: maximizar o número de horários atribuídos
    prob += lpSum(horarios[(p.pk, td.pk)] for p in periodos for td in turma_disciplinas)

    # Restrições: cada disciplina só pode ser atribuída a um horário por período
    for td in turma_disciplinas:
        for p in periodos:
            prob += lpSum(horarios[(p.pk, td.pk)] for p in periodos) <= 1

    # Restrições: cada profissional só pode ministrar aulas em no máximo três períodos por turno
    for profissional in profissionais:
        for p in periodos:
            prob += lpSum(horarios[(p.pk, td.pk)] for td in turma_disciplinas if td.professor == profissional) <= 3

    # Resolver o problema
    prob.solve()

    # Criar os registros de horário com base nas variáveis de decisão
    for p in periodos:
        for td in turma_disciplinas:
            if horarios[(p.pk, td.pk)].varValue == 1:
                Horario.objects.create(turma=turma, periodo=p, segunda=td if p.pk == 1 else None,
                                       terca=td if p.pk == 2 else None, quarta=td if p.pk == 3 else None,
                                       quinta=td if p.pk == 4 else None, sexta=td if p.pk == 5 else None)

    # Obter todos os horários gerados para a turma
    horarios = Horario.objects.filter(turma=turma)

    # Retornar o template com o resultado
    return render(request, 'Escola/inicio.html', {'conteudo_page': "Gestão Turmas - GerarHorario", 'horarios': horarios})
