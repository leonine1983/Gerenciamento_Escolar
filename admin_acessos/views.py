from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib import messages

from admin_acessos.models import message_user
#from .forms import MessageUserForm
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class Create_Login(LoginView):
    template_name = 'admin_acessos/index.html'
    success_url = reverse_lazy('admin_acessos:painel_acesso')

    def form_invalid(self, form):
        messages.error(self.request, 'Credenciais inválidas. Por favor, tente novamente.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin_acessos:painel_acesso')

    



# Faz o logout
class Faz_logout(LogoutView):
    next_page = reverse_lazy('admin_acessos:login_create')

    def dispatch(self, request, *args, **kwargs):
        # Limpara a sessão do usuario
        logout(request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Exibir mensagem de contexto, se existir
        message = messages.get_messages(request)
        return render(request, self.template_name, {'message': message})


class Painel_Acesso(TemplateView):
    template_name = 'admin_acessos/features/panel_acesso.html'



class MessageUserForm(forms.ModelForm):

    messagem= forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = message_user
        fields = ['user', 'assunto', 'messagem']
        widgets = {
            'remetente': forms.HiddenInput,
          
        }




class Mensagem_create(CreateView):
    model = message_user
    #fields = ['user', 'assunto', 'messagem']
    form_class = MessageUserForm
    template_name = 'Controle_Estoque/mensagem/mensagem_envia.html'
    success_url = reverse_lazy("admin_acessos:mensagem_lista")

    def form_valid(self, form):
        # Crie uma instância do objeto mas não o salve ainda
        mensagem = form.save(commit=False)
        # Defina o remetente como o usuário logado
        mensagem.remetente = self.request.user
        # Agora salve a instância com o remetente definido
        mensagem.save()
        return super(Mensagem_create, self).form_valid(form)



class Mensagem_lista(ListView):
    model = message_user
    template_name = 'Controle_Estoque/mensagem/mensage_lista.html'

    # Filtrar as mensagens em que o usuario logado é um dos destinatários
    def get_queryset(self):
        return message_user.objects.filter(user=self.request.user)
    



class Mensagem_uptade(UpdateView):
    model = message_user
    fields = '__all__'    
    template_name = 'Controle_Estoque/mensagem/mensagem_envia.html'


class Mensagem_delete(DeleteView):
    model = message_user 
    template_name = 'Controle_Estoque/mensagem/mensagem_envia.html'


from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.urls import reverse

from .models import message_user  # Importe o modelo message_user

class UpdateMessageView(View):
    def get(self, request, *args, **kwargs):
        # Obtenha o ID da mensagem da URL
        message_id = kwargs.get('pk')
        
        # Recupere a mensagem pelo ID, ou retorne 404 se não existir
        message = get_object_or_404(message_user, id=message_id)
        
        # Atualize o campo 'aberta' para True
        message.aberta = True
        message.save()
        
        # Redirecione para a URL 'admin_acessos:mensagem_lista'
        return redirect(reverse('admin_acessos:mensagem_detalhe', args=[message_id]))

class DetalheView_mensage(DetailView):
    model = message_user
    template_name = 'Controle_Estoque/mensagem/mensage_lista.html'
    context_object_name = 'mensagem'

    def get_context_data(self, **kwargs):
        svg = '<svg class="bi" width="30"  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M256 4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM92.7-16V253.3c18.6-6.6 32-24.4 32-4B8r3B4p7yhRXuBWLqsQ546WR43cqQwrbXMDFnBi6vSJBeif8tPW85a7r7DM961Jvk4hdryZoByEp8GC8HzsqJpRN4FxGM96.2-22.6 0l-64 64c-6.2 6.2-6.2 16.4 0 22.6s16.4 6.2 22.6 0L480 310.6V432c0 8.8 7.2 16 16 16s16-7.2 16-16V310.6l36.7 36.7c6.2 6.2 16.4 6.2 22.6 0zM0 176c0-8.8 7.2-16 16-16H368c8.8 0 16 7.2 16 16v32c0 8.8-7.2 16-16 16H16c-8.8 0-16-7.2-16-16V176zm352 80V480c0 17.7-14.3 32-32 32H64c-17.7 0-32-14.3-32-32V256H352zM144 320c-8.8 0-16 7.2-16 16s7.2 16 16 16h96c8.8 0 16-7.2 16-16s-7.2-16-16-16H144z"/></svg>'
        context = super().get_context_data(**kwargs)
        context["svg"] = svg
        context["title"] = 'Mensagem para o usuario'
        context ['active'] = 'mensagem'
        context ['tipo'] = 'visualiza'
        return context