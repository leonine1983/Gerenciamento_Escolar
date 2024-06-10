"""
from django import forms
from gestao_escolar.models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'validade']

    def __init__(self, *args, **kwargs):
        validade_ativa = kwargs.pop('validade_ativa', None)
        instance = kwargs.get('instance', None)
        initial = kwargs.get('initial', {})
        
        if instance:
            kwargs['initial'] = {**initial, 'validade': instance.validade}
        elif validade_ativa:
            kwargs['initial'] = {**initial, 'validade': validade_ativa}
        
        super().__init__(*args, **kwargs)
        
        if validade_ativa:
            self.fields['validade'].required = False
            self.fields['validade'].widget = forms.HiddenInput()  # Hide the field if necessary




from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from gestao_escolar.models import Horario, Turmas, Periodo, Validade_horario
from .forms import HorarioForm

from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from gestao_escolar.models import Horario, Turmas, Periodo, Validade_horario
from .forms import HorarioForm


from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from gestao_escolar.models import Horario, Turmas, Periodo, Validade_horario
from .forms import HorarioForm

class HorarioUpdateCreateView(View):
    template_name = 'Escola/inicio.html'

    def get(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        validade_ativa = Validade_horario.objects.filter(horario_ativo=True).first()

        forms_periodos = []
        for periodo in periodos:
            horario = Horario.objects.filter(turma=turma, periodo=periodo).first()
            if horario:
                form = HorarioForm(instance=horario, prefix=str(periodo.id), validade_ativa=validade_ativa)
            else:
                form = HorarioForm(initial={'turma': turma, 'periodo': periodo}, prefix=str(periodo.id), validade_ativa=validade_ativa)
            forms_periodos.append((form, periodo))

        context = {
            'forms_periodos': forms_periodos,
            'turma': turma,
            'conteudo_page': "Gestão Turmas - Editar/Criar Horário",
            'horarios': Horario.objects.filter(turma=turma)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        turma_id = self.kwargs['turma_id']
        turma = get_object_or_404(Turmas, pk=turma_id)
        periodos = Periodo.objects.all()
        validade_ativa = Validade_horario.objects.filter(horario_ativo=True).first()

        # Get all Horario instances related to the current Turma
        horarios = Horario.objects.filter(turma=turma)

        forms = []
        for horario in horarios:
            form = HorarioForm(request.POST, instance=horario, prefix=str(horario.periodo.id), validade_ativa=validade_ativa)
            forms.append(form)

        if all(form.is_valid() for form in forms):
            for form in forms:
                horario_instance = form.save(commit=False)
                horario_instance.validade = validade_ativa
                horario_instance.save()
            messages.success(request, 'Horários atualizados com sucesso.')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            forms_periodos = [(form, Periodo.objects.get(pk=form.prefix)) for form in forms]
            context = {
                'forms_periodos': forms_periodos,
                'turma': turma,
                'conteudo_page': "Gestão Turmas - Editar/Criar Horário",
                'horarios': horarios  # Pass all Horario instances to display errors
            }
            return render(request, self.template_name, context)

"""