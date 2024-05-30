# utils.py

from constraint import Problem
from .models import HorarioAula, TurmaDisciplina

def gerar_horario_auto(turmas_disciplinas):
    problem = Problem()

    # Adiciona as variáveis de horário para cada turma_disciplina
    for turma_disciplina in turmas_disciplinas:
        dias_periodos = [(dia, periodo) for dia in range(1, 6) for periodo in range(1, 4)]
        for dia, periodo in dias_periodos:
            problem.addVariable(f"{turma_disciplina.id}_{dia}_{periodo}", [None, turma_disciplina])

    # Adiciona as restrições
    for turma_disciplina in turmas_disciplinas:
        count_restricao = f"count_{turma_disciplina.id}"
        problem.addConstraint(lambda *args: sum(1 for arg in args if arg == turma_disciplina) <= 3, [f"{turma_disciplina.id}_{dia}_{periodo}" for dia in range(1, 6) for periodo in range(1, 4)], count_restricao)

    # Resolve o problema
    solution = problem.getSolution()

    # Cria os objetos de HorarioAula com base na solução
    horarios = []
    for key, value in solution.items():
        if value is not None:
            turma_disciplina_id, dia, periodo = key.split("_")
            turma_disciplina = TurmaDisciplina.objects.get(id=int(turma_disciplina_id))
            horarios.append(HorarioAula(turma_disciplina=turma_disciplina, dia_semana=int(dia), periodo=int(periodo)))
    
    # Salva os horários de aula
    HorarioAula.objects.bulk_create(horarios)
