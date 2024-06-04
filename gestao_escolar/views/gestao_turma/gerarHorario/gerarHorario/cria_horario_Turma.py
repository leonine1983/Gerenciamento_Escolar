from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from gestao_escolar.models import Horario, Turmas, TurmaDisciplina, Periodo

from django import forms

class HorarioForm(forms.ModelForm):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all(), required=False)
    segunda = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    terca = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quarta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quinta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    sexta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)

    class Meta:
        model = Horario
        fields = ['periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta']


class HorarioUpdateView(UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'Escola/inicio.html'  # Especifica o template a ser usado


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['periodos'] = Periodo.objects.all()
        context['conteudo_page'] = "Gestão Turmas - GerarHorario"
        return context

    def form_valid(self, form):
        horario = form.save(commit=False)
        turma = horario.turma

        # Verifica se o mesmo período está sendo ocupado em turmas diferentes
        for field_name in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
            turma_disciplina = getattr(horario, field_name)
            if turma_disciplina:
                # Verifica se existe algum horário para essa turma no mesmo período em outro dia da semana
                horario_conflitante = Horario.objects.exclude(pk=horario.pk).filter(turma__serie=turma.serie, periodo=horario.periodo)
                if horario_conflitante.filter(**{field_name: turma_disciplina}).exists():
                    # Se houver conflito, redireciona com uma mensagem de erro
                    return redirect('url_de_redirecionamento_com_mensagem_de_erro')

        return super().form_valid(form)
