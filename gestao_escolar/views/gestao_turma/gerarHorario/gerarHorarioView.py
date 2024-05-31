from django.shortcuts import render, redirect
from django.views import View
from gestao_escolar.models import HorarioAula, TurmaDisciplina, Turmas
from constraint import Problem
from django.contrib import messages
from django.urls import reverse

class GerarHorarioView(View):
    def get(self, request, turma_id):
        turma = Turmas.objects.get(id=turma_id)
        turma_disciplinas = TurmaDisciplina.objects.filter(turma=turma)

        problem = Problem()

        # Variáveis: disciplina-período
        for td in turma_disciplinas:
            for dia in range(1, 6):
                for periodo in range(1, 4):
                    problem.addVariable(f"{td.id}-{dia}-{periodo}", [0, 1])

        # Restrição: Cada disciplina pode ter apenas um período por dia
        for td in turma_disciplinas:
            for dia in range(1, 6):
                problem.addConstraint(lambda *args: sum(args) <= 1,
                                      [f"{td.id}-{dia}-{p}" for p in range(1, 4)])

        # Restrição: Cada período pode ter apenas uma disciplina
        for dia in range(1, 6):
            for periodo in range(1, 4):
                problem.addConstraint(lambda *args: sum(args) <= 1,
                                      [f"{td.id}-{dia}-{periodo}" for td in turma_disciplinas])

        # Não há restrição de disponibilidade do professor
        solution = problem.getSolution()

        if solution:
            HorarioAula.objects.filter(turma=turma).delete()  # Limpar horários antigos
            for key, value in solution.items():
                if value == 1:
                    td_id, dia, periodo = map(int, key.split('-'))
                    turma_disciplina = TurmaDisciplina.objects.get(id=td_id)
                    HorarioAula.objects.create(
                        turma=turma,
                        turma_disciplina=turma_disciplina,
                        dia_semana=dia,
                        periodo=periodo
                    )
            messages.success(request, 'Horário gerado com sucesso!')
            return redirect(reverse('Escola/inicio.html', kwargs={
                'turma_id': turma.id,                
                'conteudo_page': 'Gestão Turmas - GerarHorario'}))
        else:
            messages.error(request, 'Não foi possível gerar um horário válido.')
            return render(request, 'Escola/inicio.html', {
                'conteudo_page': 'Gestão Turmas - GerarHorario',
                'turma': turma
            })

class HorarioListView(View):
    def get(self, request, turma_id):
        turma = Turmas.objects.get(id=turma_id)
        horarios = HorarioAula.objects.filter(turma=turma).order_by('dia_semana', 'periodo')
        return render(request, 'Escola/inicio.html', {
            'horarios': horarios,
            'turma': turma,
            'conteudo_page': 'Gestão Turmas - GerarHorario'
        })
