from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from gestao_escolar.models import Horario, TurmaDisciplina, Turmas
from django.shortcuts import get_object_or_404

class HorarioCreateView(CreateView):
    model = Horario
    fields = ['periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('nome_da_url')

    def form_valid(self, form):
        # Pegar o ID da turma da URL
        turma_id = self.kwargs['turma_id']
        # Obter a turma com base no ID
        turma = get_object_or_404(Turmas, pk=turma_id)
        turmaDisciplina = get_object_or_404(TurmaDisciplina, turma=turma_id)

        # Adicionando a turma ao formulário
        form.instance.turma = turma

        # Realizar as verificações de restrições
        periodo = form.cleaned_data.get('periodo')
        disciplinas_dia = [form.cleaned_data.get(field) for field in ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado'] if form.cleaned_data.get(field)]

        # Restrição de Período
        for disciplina in disciplinas_dia:
            if Horario.objects.filter(turma=turma, periodo=periodo, segunda=disciplina).exists():
                messages.error(self.request, f"O professor já ocupa o período {periodo} na turma {turma}.")
                return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id':self.kwargs['turma_id']}))

        # Restrição de Aulas por Dia
        for disciplina in disciplinas_dia:
            if turmaDisciplina.quant_aulas_dia > 0:                
                if disciplinas_dia.count(disciplina) >= turmaDisciplina.quant_aulas_dia:
                    messages.error(self.request, f"A quantidade máxima de aulas diárias para a disciplina {disciplina} foi atingida.")
                    return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id':self.kwargs['turma_id']}))

        # Restrição de Aulas por Semana
        if turmaDisciplina.quant_aulas_semana > 0:            
            if Horario.objects.filter(turma=turma, segunda__in=disciplinas_dia).count() >= turmaDisciplina.quant_aulas_semana:
                messages.error(self.request, f"A quantidade máxima de aulas semanais para a turma {turma} foi atingida.")
                return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id':self.kwargs['turma_id']}))

        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        # Pegar o ID da turma da URL
        turma_id = self.kwargs['turma_id']
        # Definir a turma como inicial
        initial['turma'] = turma_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conteudo_page'] = "Gestão Turmas - GerarHorario"
        return context
