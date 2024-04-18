from gestao_escolar.models import *
from django.shortcuts import redirect
from django.urls import reverse
from gestao_escolar.models import AnoLetivo
from django.contrib.auth.decorators import login_required


@login_required
def seleciona_anoLetivo_session(request, pk):
    ano = AnoLetivo.objects.filter(id=pk).first()  # Usando 'first()' para obter apenas um objeto
    if ano:
        request.session['anoLetivo_id'] = ano.id  # Armazenando apenas o ID   
        request.session['anoLetivo_nome'] = ano  # Armazenando apenas o ID   

    return redirect(reverse('Gestao_Escolar:GE_Escola_inicio'))