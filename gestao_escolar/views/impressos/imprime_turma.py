from typing import Any
from django.views.generic import ListView
from gestao_escolar.models import Turmas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class Imprime_Turmas (LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Turmas
    template_name = 'Escola/impressos/impressos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ano = self.request.session['anoLetivo_id']
        turmas = Turmas.objects.filter(ano_letivo=ano)
        print(f'lher o ano {ano}')
        context ['list_turmas'] = turmas
        return context