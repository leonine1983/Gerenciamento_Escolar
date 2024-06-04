
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.forms import modelformset_factory
from gestao_escolar.models import Turmas, Horario, Periodo, TurmaDisciplina

class GerarHorarioView(View):
    template_name = 'Escola/inicio.html'

    def get(self, request, turma_id):
        turma = get_object_or_404(Turmas, id=turma_id)
        PeriodoFormSet = modelformset_factory(
            Horario, fields=('periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta'), extra=0
        )

        # Criar instâncias de Horário se não existirem
        periodos = Periodo.objects.all().order_by('hora_inicio')
        for periodo in periodos:
            Horario.objects.get_or_create(turma=turma, periodo=periodo)

        formset = PeriodoFormSet(queryset=Horario.objects.filter(turma=turma).order_by('periodo'))

        context = {
            'formset': formset,
            'turma': turma,
            'conteudo_page': 'Gestão Turmas - GerarHorario'
        }
        return render(request, self.template_name, context)

    def post(self, request, turma_id):
        turma = get_object_or_404(Turmas, id=turma_id)
        PeriodoFormSet = modelformset_factory(
            Horario, fields=('periodo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta'), extra=0
        )
        formset = PeriodoFormSet(request.POST)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.turma = turma
                instance.save()
            return redirect('nome_da_sua_view_de_sucesso')  # Redirecionar para a view de sucesso ou outra página

        context = {
            'formset': formset,
            'turma': turma,
            'conteudo_page': 'Gestão Turmas - GerarHorario'
        }
        return render(request, self.template_name, context)