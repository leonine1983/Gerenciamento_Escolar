from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from gestao_escolar.models import GestaoTurmas
from django.forms import modelformset_factory

def gestao_turmas_update_view(request, pk):
    # Obter todos os objetos de GestaoTurmas para a turma com a chave primária 'pk'
    queryset = GestaoTurmas.objects.filter(aluno__turma=pk)
    
    # Obter o nome da turma (supondo que o nome do aluno esteja na turma)
    nome_turma = queryset.first().aluno.turma.nome  # Assumindo que aluno.turma.nome é o nome da turma
    
    FormSet = modelformset_factory(GestaoTurmas, fields=['aluno','trimestre','grade',  'notas'], extra=0)
    
    if request.method == 'POST':
        formset = FormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('success_url')  # Redirecionar para a URL de sucesso
    else:
        formset = FormSet(queryset=queryset)
    
    context = {
        'formset': formset,
        'nome_turma': nome_turma,  # Adicionando o nome da turma ao contexto
        'conteudo_page': f"Gestão Turmas - Notas Aluno",  # Atualizando o conteúdo da página para incluir o nome da turma
        'page_ajuda': "<div class='m-2'><b>Nessa área, definimos todos os dados para a"
    }
       
    return render(request, 'Escola/inicio.html', context)

