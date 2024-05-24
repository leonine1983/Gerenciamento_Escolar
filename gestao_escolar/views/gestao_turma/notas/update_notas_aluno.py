from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from gestao_escolar.models import GestaoTurmas

class GestaoTurmasUpdateView(UpdateView):
    model = GestaoTurmas
    fields = ['grade', 'trimestre', 'notas']
    template_name = 'gestao_turmas_form.html'
    success_url = reverse_lazy('success_url')  # Ajuste conforme necessário

    def get_object(self):
        # Obtenha o objeto específico que você deseja atualizar.
        # Isso pode ser ajustado conforme suas necessidades específicas.
        matriculas_ptr = self.kwargs.get('pk')
        return GestaoTurmas.objects.get(matriculas_ptr=matriculas_ptr)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)        
        
        context['conteudo_page'] = "Gestão Turmas - Notas Aluno"        
        context['page_ajuda'] = "<div class='m-2'><b>Nessa área, definimos todos os dados para a"
        
        return context
