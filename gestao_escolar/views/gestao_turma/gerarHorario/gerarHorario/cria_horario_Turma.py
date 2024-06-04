from django.shortcuts import render, redirect
from django.views.generic.edit import View
from gestao_escolar.models import Horario, Turmas, TurmaDisciplina, Periodo

from django import forms
from django.forms import modelformset_factory
from gestao_escolar.models import Horario, TurmaDisciplina, Periodo

class HorarioForm(forms.ModelForm):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all(), empty_label=None)
    segunda = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    terca = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quarta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quinta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    sexta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)

    class Meta:
        model = Horario
        fields = ['periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta']

HorarioFormSet = modelformset_factory(Horario, form=HorarioForm, extra=1, can_delete=True)



class HorarioUpdateView(View):
    template_name = 'Escola/inicio.html'

    def get(self, request, *args, **kwargs):
        formset = HorarioFormSet(queryset=Horario.objects.all())
        context = {
            'formset': formset,
            'periodos': Periodo.objects.all(),  # Embora não estritamente necessário
            'conteudo_page': "Gestão Turmas - GerarHorario",
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formset = HorarioFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
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

                horario.save()

            return redirect('url_de_sucesso')  # Redireciona após sucesso

        context = {
            'formset': formset,
            'periodos': Periodo.objects.all(),
            'conteudo_page': "Gestão Turmas - GerarHorario",
        }
        return render(request, self.template_name, context)