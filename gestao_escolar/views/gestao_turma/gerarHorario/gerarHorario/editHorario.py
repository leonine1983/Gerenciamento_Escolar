"""from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from gestao_escolar.models import Turmas, Horario, TurmaDisciplina, Periodo
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from django import forms
from gestao_escolar.models import Horario


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['turma_disciplina']
    
    def __init__(self, *args, **kwargs):
        super(HorarioForm, self).__init__(*args, **kwargs)
        # Torne os campos não obrigatórios
        #self.fields['periodo'].required = False
        self.fields['turma_disciplina'].required = False


from django.urls import reverse_lazy

class HorarioUpdateView(UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'Escola/inicio.html'

    def get_object(self, queryset=None):
        horario_id = self.kwargs['pk']
        turma_id = self.kwargs['turma_id']
        return get_object_or_404(Horario, id=horario_id, turma_id=turma_id)
    
    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:edit_horario', kwargs={'turma_id': self.kwargs['turma_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context.update({
            'horarios': Horario.objects.filter(turma=self.kwargs['turma_id']),
            'periodos': Periodo.objects.all(),
            'conteudo_page': "Gestão Turmas - GerarHorario"
        })
        return context

def UpdateAulas(request, turma_id):
    turma = get_object_or_404(Turmas, id=turma_id)
    gradeAulas = Horario.objects.filter(turma=turma)

    # Criar um formset usando o formulário personalizado HorarioForm, sem a opção de deletar
    HorarioFormSet = modelformset_factory(Horario, form=HorarioForm, extra=1)
    
    if request.method == 'POST':
        formset = HorarioFormSet(request.POST, queryset=gradeAulas)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Horários atualizados com sucesso.')
            context = {
                            'turma': turma,
                            'formset': formset,
                            'turmas_disciplinas': TurmaDisciplina.objects.filter(turma=turma),
                            'horarios': Horario.objects.filter(turma=turma_id),
                            'periodos': Periodo.objects.all(),
                            'dias_semana': DiaSemana.objects.all(),
                            'conteudo_page': "Gestão Turmas - GerarHorario"
                        }

            return render(request, 'Escola/inicio.html', context)

        else:
            messages.error(request, 'Corrija os erros no formulário.')
    else:
        formset = HorarioFormSet(queryset=gradeAulas)

    context = {
        'turma': turma,
        'formset': formset,
        'turmas_disciplinas': TurmaDisciplina.objects.filter(turma=turma),
        'horarios': Horario.objects.filter(turma=turma_id),
        'periodos': Periodo.objects.all(),
        'dias_semana': DiaSemana.objects.all(),
        'conteudo_page': "Gestão Turmas - GerarHorario"
    }

    return render(request, 'Escola/inicio.html', context)

"""
