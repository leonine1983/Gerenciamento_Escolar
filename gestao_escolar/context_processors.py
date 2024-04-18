from django.shortcuts import redirect
from django.urls import reverse



def verifica_sessoes(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'anoLetivo_id' not in request.session or 'escola_nome' not in request.session:
                return redirect(reverse('Gestao_Escolar:GE_inicio'))  # Substitua pelo nome da URL da página de login
        return view_func(request, *args, **kwargs)
    return wrapper
