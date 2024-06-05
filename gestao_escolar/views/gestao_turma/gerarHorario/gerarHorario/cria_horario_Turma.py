from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from gestao_escolar.models import Horario, TurmaDisciplina, Periodo

class HorarioCreateView(CreateView):
    model = Horario
    template_name = 'Escola/inicio.html'
    fields = ['periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

    def form_valid(self, form):
        turma_id = self.kwargs.get('turma_id')
        form.instance.turma_id = turma_id
        periodo = form.cleaned_data.get('periodo')
        turma_disciplina_ids = [
            form.cleaned_data.get('segunda'),
            form.cleaned_data.get('terca'),
            form.cleaned_data.get('quarta'),
            form.cleaned_data.get('quinta'),
            form.cleaned_data.get('sexta'),
            form.cleaned_data.get('sabado'),
        ]

        # Restrição de Período
        for turma_disciplina_id in turma_disciplina_ids:
            if turma_disciplina_id and Horario.objects.filter(turma_id=turma_id, periodo=periodo).exists():
                messages.error(self.request, f"O profissional já ocupa o período {periodo}.")
                return self.form_invalid(form)

        # Restrição de Aulas por Dia
        for turma_disciplina_id in turma_disciplina_ids:
            if turma_disciplina_id:
                quant_aulas_dia = turma_disciplina_id.quant_aulas_dia
                if quant_aulas_dia:
                    # Verificar se já existe um período com o mesmo dia da semana
                    if Horario.objects.filter(
                        turma_id=turma_id,
                        periodo__hora_inicio__week_day=periodo.hora_inicio.weekday()
                    ).exists():
                        messages.error(self.request, f"A quantidade máxima de aulas diárias para {turma_disciplina_id.disciplina.nome} foi atingida.")
                        return self.form_invalid(form)

        # Restrição de Aulas por Semana
        for turma_disciplina_id in turma_disciplina_ids:
            if turma_disciplina_id:
                quant_aulas_semana = turma_disciplina_id.quant_aulas_semana
                if quant_aulas_semana and Horario.objects.filter(
                    turma_id=turma_id, 
                    segunda=turma_disciplina_id
                ).count() >= quant_aulas_semana:
                    messages.error(self.request, f"A quantidade máxima de aulas semanais para {turma_disciplina_id.disciplina.nome} foi atingida.")
                    return self.form_invalid(form)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conteudo_page'] = "Gestão Turmas - GerarHorario"        
        context['horarios'] = Horario.objects.filter(turma = self.kwargs.get('turma_id'))
        return context

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criarIDhorario', kwargs={"turma_id": self.kwargs.get('turma_id')})
