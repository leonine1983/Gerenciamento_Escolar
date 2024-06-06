from django import forms
from gestao_escolar.models import Horario, Turmas, TurmaDisciplina, Periodo
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from django import forms
from gestao_escolar.models import Horario

class HorarioForm(forms.ModelForm):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # Tornando data_inicio não obrigatório
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # Tornando data_fim não obrigatório
    )

    class Meta:
        model = Horario
        fields = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'data_inicio', 'data_fim']

    def __init__(self, *args, **kwargs):
        # Recebendo a data inicial do contexto
        data_inicio = kwargs.pop('data_inicio', None)
        super().__init__(*args, **kwargs)
        # Definindo o valor da data inicial no campo do formulário
        if data_inicio:
            self.fields['data_inicio'].initial = data_inicio
            # Preenchendo automaticamente o campo de data de fim com a mesma data de início
            self.fields['data_fim'].initial = data_inicio



from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from gestao_escolar.models import Horario, Turmas, Periodo

class HorarioCreateView(View):
    template_name = 'Escola/inicio.html'

    def get(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        forms_periodos = [(HorarioForm(initial={'turma': turma, 'periodo': periodo}, prefix=str(periodo.id)), periodo) for periodo in periodos]
        context = {
            'forms_periodos': forms_periodos,
            'turma': turma,
            'conteudo_page': "Gestão Turmas - GerarHorario",
            'horarios': Horario.objects.filter(turma=turma)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        forms = [HorarioForm(request.POST, prefix=str(periodo.id)) for periodo in periodos]

        if all(form.is_valid() for form in forms):
            for form in forms:
                periodo_id = request.POST.get(f'{form.prefix}-periodo')
                periodo = get_object_or_404(Periodo, pk=periodo_id)
                Horario.objects.update_or_create(
                    turma=turma, periodo=periodo,
                    defaults=form.cleaned_data
                )
            messages.success(request, 'Horários atualizados com sucesso.')
            return HttpResponseRedirect(self.get_success_url())
        else:
            for form in forms:
                if not form.is_valid():
                    print(form.errors)
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            forms_periodos = [(form, Periodo.objects.get(pk=form.prefix).nome_periodo) for form in forms]
            context = {
                'forms_periodos': forms_periodos,
                'turma': turma,
                'conteudo_page': "Gestão Turmas - GerarHorario",
                'horarios': Horario.objects.filter(turma=turma)
            }
            return render(request, self.template_name, context)

    def get_success_url(self):
        return reverse_lazy('Gestao_Escolar:criar_horario', kwargs={'turma_id': self.kwargs['turma_id']})
