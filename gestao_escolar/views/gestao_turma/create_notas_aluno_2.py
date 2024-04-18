from gestao_escolar.models import Turmas, Trimestral_Notas_Aluno, Profissionais, Matriculas, TurmaDisciplina
from rh.models import Encaminhamentos
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .disciplina_notasAlunos_form import NotasAlunos_All_form
from django.db.models import Q


class Create_Notas_pk(LoginRequiredMixin, CreateView):
    model = Trimestral_Notas_Aluno
    #fields = "__all__"
    form_class = NotasAlunos_All_form
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('Gestao_Escolar:GE_Escola_inicio')

    """
    def get_queryset(self):
        buscar_turma = self.request.GET.get ('busca-turma')
        if buscar_turma:
            turmas = TurmaDisciplina.objects.filter(
                                Q(discipina__nome__icontains = buscar_turma)
                                and Q(turma__ano_letivo = self.request.session("anoLetivo_id")) 
                                and Q(turma = self.kwargs['pk']))
        else:
            turmas = TurmaDisciplina.objects.filter(turma = self.kwargs['pk'])

        return turmas




"""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['aluno_query'] = Matriculas.objects.filter(turma = self.kwargs['pk'])
        #kwargs['professor_query'] = Profissionais.objects.filter(nome__encaminhamento__nome_escola = self.request.session['escola_id'], nome__encaminhamento__ano_contrato__anoletivo = self.request.session['anoLetivo_id'], cargo__nome = "Professor")
        return kwargs

    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Gestão de Turmas'
        context['turmas'] = Turmas.objects.filter(escola = self.request.session['escola_id'], ano_letivo = self.request.session['anoLetivo_id'])
        context['matriculas'] = Matriculas.objects.filter(turma = self.kwargs['pk'])
        context['TurmaDisciplina'] = TurmaDisciplina.objects.filter(turma = self.kwargs['pk'])

        context['ativa'] = "Grades"
        #context['alunos'] = Matriculas.objects.all()
        
        context['conteudo_page'] = "Gestão Turmas"
        context['turmas_disciplinas'] = self.get_queryset
        
        context['page_ajuda'] = "<div class='m-2'><b>Nessa área, definimos todos os dados para a celebração do contrato com o profissional. </b>\
            <hr>\
                <div class='border bg-secondary p-2'>\
                    <h2>Pessoar a ser contratada</h2>\
                    <p>Espaço onde é selecionado no nome da pessoa que será contratada. Se por alguma razão estiver vazio, clique aqui: <a class='btn btn-sm btn-primary' href='pessoas/create/'>Clique aqui para cadastrar uma pessoa no sistema</a></p>\
                </div>\
                <div class=' p-2'>\
                    <p><h2>Ano de contrato</h2>\
                    <p>Espaço onde é selecionado o ano em que o profissional será contratado. Se por alguma razão estiver vazio, clique aqui: <a class='btn btn-sm btn-secondary' href='ano/create/'>Clique aqui para cadastrar um ANO no sistema</a></p>\
                </div>\
                <div class='border bg-secondary p-2'>\
                    <p><h2>Tipo de contrato</h2>\
                    <p>Espaço onde é selecionado o modelo de contrato que será utilizado para a contratação. Se estiver vazio,  clique aqui: <a class='btn btn-sm btn-primary' href='ano/create/'>Clique aqui para criar um MODELO DE CONTRATO no sistema</a></p>\
                </div>\
                <div class=' p-2'>\
                    <p><h2>Função que irá desempenhar na escola</h2>\
                    <p>Local em que é definido a função pela qual o profissional está sendo contratado</p>\
                </div>\
                <div class='border bg-secondary p-2'>\
                    <p><h2>Escola onde o profissional irá desempenhar suas funções</h2>\
                    <p>Espaço onde é selecionado a instituição que o profissional desempenhará suas funções. Se estiver vazio,  clique aqui: <a class='btn btn-sm btn-primary' href='escola/create/'>Clique aqui para Adicionar uma Escola</a></p>\
                </div>"
        
        return context
            



            