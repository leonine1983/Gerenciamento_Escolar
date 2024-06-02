from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from constraint import Problem, AllDifferentConstraint
from gestao_escolar.models import TurmaDisciplina, Turmas, Horario, Periodo

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

class GerarHorarioView(CreateView):
    model = Horario
    fields = ['turma', 'periodo', 'turno', 'segunda', 'terca', 'quarta', 'quinta', 'sexta']
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('nome_da_url_de_sucesso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conteudo_page"] = "Gestão Turmas - GerarHorario"
        return context

    def post(self, request, *args, **kwargs):
        # Lógica para processar os dados do formulário e criar/atualizar horários das turmas
        turmas_disciplinas = request.POST.getlist('turmas_disciplinas')
        periodos = Periodo.objects.all()

        for turma_disciplina_id in turmas_disciplinas:
            turma_disciplina = TurmaDisciplina.objects.get(id=turma_disciplina_id)
            turma = turma_disciplina.turma

            for periodo in periodos:
                turno = request.POST.get(f'turno_{turma_disciplina_id}_{periodo.id}')

                # Verifica se já existe um horário para esta turma e este período
                horario, created = Horario.objects.get_or_create(turma=turma, periodo=periodo)

                # Atualiza os dados do horário
                horario.turno = turno
                horario.segunda = request.POST.get(f'segunda_{turma_disciplina_id}_{periodo.id}')
                horario.terca = request.POST.get(f'terca_{turma_disciplina_id}_{periodo.id}')
                horario.quarta = request.POST.get(f'quarta_{turma_disciplina_id}_{periodo.id}')
                horario.quinta = request.POST.get(f'quinta_{turma_disciplina_id}_{periodo.id}')
                horario.sexta = request.POST.get(f'sexta_{turma_disciplina_id}_{periodo.id}')

                horario.save()

        return render(request, self.template_name, self.get_context_data())
