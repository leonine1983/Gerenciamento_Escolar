
from django.shortcuts import get_object_or_404, redirect, render
from gestao_escolar.models import GestaoTurmas, Matriculas, Trimestre
from django import forms

class GestaoTurmasForm(forms.ModelForm):
    class Meta:
        model = GestaoTurmas
        fields = ['grade', 'notas']

def create_or_update_gestao_turmas(request, aluno_id, trimestre_id):
    aluno = get_object_or_404(Matriculas, pk=aluno_id)
    trimestre = get_object_or_404(Trimestre, pk=trimestre_id)

    # Verificar se já existe um registro para a combinação de aluno, trimestre e grade
    gestao_turma = GestaoTurmas.objects.filter(aluno=aluno, trimestre=trimestre).first()

    if request.method == 'POST':
        form = GestaoTurmasForm(request.POST, instance=gestao_turma)
        if form.is_valid():
            gestao_turma = form.save(commit=False)
            gestao_turma.aluno = aluno
            gestao_turma.trimestre = trimestre
            gestao_turma.save()
            return redirect('sua_view_detail', aluno_id=aluno_id)  # Redirecione para a visualização de detalhes do aluno
    else:
        form = GestaoTurmasForm(instance=gestao_turma)

    context = {
        'form': form,
        'aluno': aluno,
        'trimestre': trimestre,        
        'conteudo_page': f"Gestão Turmas - Notas Update",
        'gestao_turma': gestao_turma
    }    

       
    return render(request, 'Escola/inicio.html', context)