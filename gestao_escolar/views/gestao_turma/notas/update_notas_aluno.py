from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from gestao_escolar.models import GestaoTurmas, Trimestre, Turmas, TurmaDisciplina
from django.forms import modelformset_factory

def gestao_turmas_update_view(request, pk):
    # Obter todos os objetos de GestaoTurmas para a turma com a chave primária 'pk'
    queryset = GestaoTurmas.objects.filter(aluno__turma=pk)
    matricula = TurmaDisciplina.objects.filter(turma=pk)
    context = {
        'disciplina':matricula,
        'gestaoTurmas': queryset, 
        'conteudo_page': f"Gestão Turmas - Notas Aluno", 
        'page_ajuda': "<div class='m-2'><b>Nessa área, definimos todos os dados para a",        
        'trimestre': Trimestre.objects.all()
    }
       
    return render(request, 'Escola/inicio.html', context)

