from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from constraint import Problem, AllDifferentConstraint
from gestao_escolar.models import TurmaDisciplina, Periodo, Turmas, Horario

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from constraint import Problem, AllDifferentConstraint
from gestao_escolar.models import TurmaDisciplina, Turmas, Horario

class GerarHorarioView(View):
    template_name = 'Escola/inicio.html'
    context = {'conteudo_page': "Gestão Turmas - GerarHorario"}

    def get(self, request, *args, **kwargs):
        # Obtendo todas as turmas
        turmas = list(Turmas.objects.all())

        # Criando um problema de restrição
        problem = Problem()

        # Adicionando variáveis de restrição para cada turma e dia
        dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
        variables = set()  # Usando um conjunto para garantir a exclusividade das variáveis
        for turma in turmas:
            for dia in dias_semana:
                var = (turma, dia)
                # Verifica se a variável já foi adicionada
                if var not in variables:
                    variables.add(var)
                    problem.addVariable(var, TurmaDisciplina.objects.all())

        # Adicionando restrição de que cada disciplina só pode ocorrer uma vez em um dia
        for dia in dias_semana:
            day_vars = []
            for turma in turmas:
                day_vars.append([(turma, dia)])
            for p in day_vars:
                problem.addConstraint(AllDifferentConstraint(), p)

        # Adicionando restrição de quantidade de aulas por dia e semana
        for td in TurmaDisciplina.objects.all():
            for dia in dias_semana:
                day_vars = [(turma, dia) for turma in turmas]
                problem.addConstraint(lambda *args, td=td, dia=dia: self.check_aulas(*args, td=td, dia=dia), day_vars)

        # Debug para verificar as variáveis e restrições do problema
        print("Variáveis do problema:")
        for variable, domain in problem._variables.items():
            print(f"  {variable}: {domain}")

        print("Restrições do problema:")
        for constraint in problem._constraints:
            print(f"  {constraint}")

        # Resolvendo o problema
        solutions = problem.getSolutions()
        print(f"Solution: {solutions}")
        for solution in solutions:
            print(f"Solution: {solution}")
            for key, value in solution.items():
                print(f" As soluções {key}: {value}")   # Adicione esta linha para verificar o conteúdo de cada solução

        # Salvando os horários no banco de dados
        for solution in solutions:
            for key, value in solution.items():
                if value:
                    turma, dia = key
                    # Criar uma nova instância de Horario
                    horario, created = Horario.objects.get_or_create(turma=turma, turno=dia)
                    # Atribuir o valor corretamente
                    setattr(horario, dia, value)
                    # Salvar a instância do Horario
                    horario.save()

        # Obtendo os horários gerados
        horarios = Horario.objects.all()

        # Renderizando o template
        return render(request, self.template_name, {**self.context, 'horarios': horarios})


    def check_aulas(self, *args, td, dia):
        count = 0
        for arg in args:
            if arg == td:
                count += 1
        if count > td.quant_aulas_dia:
            return False
        return True

    def __lt__(self, other):
        return self.nome < other.nome
