from django import forms
from gestao_escolar.models import Horario, Turmas, TurmaDisciplina
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import HorarioForm
from django.shortcuts import get_object_or_404

class HorarioForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Horario
        fields = ['periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'data_inicio', 'data_fim']


class HorarioCreateView(CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'Escola/inicio.html'

    def form_valid(self, form):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        turmaDisciplina = get_object_or_404(TurmaDisciplina, turma=turma_id)
        form.instance.turma = turma

        periodo = form.cleaned_data.get('periodo')
        disciplinas_dia = [form.cleaned_data.get(field) for field in ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado'] if form.cleaned_data.get(field)]

        for disciplina in disciplinas_dia:
            if Horario.objects.filter(turma=turma, periodo=periodo, segunda=disciplina).exists():
                messages.error(self.request, f"O professor já ocupa o período {periodo} na turma {turma}.")
                return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']}))

        for disciplina in disciplinas_dia:
            if turmaDisciplina.quant_aulas_dia > 0:
                if disciplinas_dia.count(disciplina) >= turmaDisciplina.quant_aulas_dia:
                    messages.error(self.request, f"A quantidade máxima de aulas diárias para a disciplina {disciplina} foi atingida.")
                    return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']}))

        if turmaDisciplina.quant_aulas_semana > 0:
            if Horario.objects.filter(turma=turma, segunda__in=disciplinas_dia).count() >= turmaDisciplina.quant_aulas_semana:
                messages.error(self.request, f"A quantidade máxima de aulas semanais para a turma {turma} foi atingida.")
                return HttpResponseRedirect(reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']}))

        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['turma'] = self.kwargs['turma_id']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conteudo_page'] = "Gestão Turmas - GerarHorario"
        context['horarios'] = Horario.objects.filter(turma=self.kwargs['turma_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']})

