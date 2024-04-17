from controle_estoque.models import Prefeitura
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Prefeitura_Create (CreateView):
    model = Prefeitura
    fields = '__all__'
    template_name = 'Controle_Estoque/prefeitura/prefeitura_cadastro.html'
    success_url = reverse_lazy('Controle_Estoque:prefeitura_view')