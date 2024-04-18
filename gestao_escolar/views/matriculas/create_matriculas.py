from gestao_escolar.models import Escola, Matriculas, AnoLetivo, Turmas, Alunos
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.urls import reverse_lazy
from .matriculas_form import Matricula_form
from django.core.paginator import Paginator
from django.db.models import Q


class Create_Matriculas(LoginRequiredMixin, CreateView):
    model = Matriculas
    #fields = '__all__'
    form_class = Matricula_form
    template_name = 'Escola/inicio.html'
    success_url = reverse_lazy('Gestao_Escolar:GE_Escola_inicio')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs ['turma_queryset'] = Turmas.objects.filter(pk = self.kwargs['pk'])
        aluno_da_turma = Matriculas.objects.filter(turma = self.kwargs['pk']).values_list('id', flat=True)       
        todos  = Alunos.objects.exclude(id__in = aluno_da_turma)
        kwargs ['aluno_query'] = todos
        return kwargs

    def get_queryset(self):
        txt_aluno = self.request.GET.get('busca-aluno')
        print(f'esse o valor que veio de txt_aluno {txt_aluno}')
        busca = False
        if txt_aluno:
            alunos = Matriculas.objects.filter(Q(turma__id =self.kwargs['pk']) and Q(aluno__nome_completo__icontains = txt_aluno))
            busca = True
            print(f'esse e o valor alunos após clicar em pesquisar: alunos {alunos} e valor de busca={busca}')
        else:
            alunos = Matriculas.objects.filter(turma =self.kwargs['pk'])
            busca = False
            print(f'esse e o valor alunos após clicar em pesquisar: alunos {alunos} e valor de busca={busca}')
        return alunos, busca
    
    def get_context_data(self, **kwargs):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M38-160v-94q0-35 18-63.5t50-4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM9-103.5T622-423q69 8 130 23.5t99 35.5q33 19 52 47t19 63v94H738ZM358-481q-66 0-108-4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM94B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM90 108 4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM96-23 21t-9 31v34Zm260-321q39 0 64.5-25.5T448-631q0-39-25.5-64.5T358-721q-39 0-64.5 25.5T268-631q0 39 25.5 64.5T358-541Zm0 321Zm0-411Z"/></svg>'
        context = super().get_context_data(**kwargs)        
        context['titulo_page'] = 'Matrículas'          
        context['svg'] = svg 

        # Essa condiçao verifica o valor da variavel busca acessada no metodo get_queryset que retorna alunos, busca
        alunos, busca = self.get_queryset()
        if busca:
            matriculas = alunos
            context['matriculas'] = matriculas
        else:
            matriculas = Matriculas.objects.filter(turma =self.kwargs['pk'])
            paginato = Paginator(matriculas, per_page=15)
            page_number = self.request.GET.get('page')
            page_obj = paginato.get_page(page_number)
            context['matriculas'] = page_obj
        
        context['n_matriculas'] = matriculas
        #context['now'] = datetime.now()
        context['serie_multi'] = Turmas.objects.get(pk = self.kwargs['pk']).turma_multiserie
        context['turma_ativa'] = Turmas.objects.get(pk = self.kwargs['pk']).nome          

        context['conteudo_page'] = "Matricular Aluno"       
        
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
    
    # O form foi sobrescrito para passar o objeto request no método form_valid para verificar 
    # se a matricula do aluno já existe no ano letivo atual e enviar a mensagem de erro    
    
    def form_valid(self, form):
        # Imprima o conteúdo do objeto
        print("Conteúdo do objeto self.object:")
        print(f"Aluno: {self.object.aluno}")
        print(f"Outro Atributo: {self.object.outro_atributo}")
    # Chame o método da superclasse para definir self.object
        self.object = form.save(commit=False)  # Isso pode variar com base na lógica do seu formulário

        if self.object:
            matricula_exist = Matriculas.objects.filter(aluno=self.object.aluno, turma__ano_letivo=self.request.session['anoLetivo_id'])
            matricula_exist = matricula_exist.exclude(pk=self.object.pk) if self.object.pk else matricula_exist

            if matricula_exist.exists():
                for n in matricula_exist:
                    matricula_turma = n.turma
                    matricula_escola = n.turma.escola
                    matricula_ano = n.turma.ano_letivo
                form.add_error(f"O aluno já está matriculado na turma do {matricula_turma}, da escola {matricula_escola} no Ano Letivo {matricula_ano}")
            
            

        return super().form_valid(form)
