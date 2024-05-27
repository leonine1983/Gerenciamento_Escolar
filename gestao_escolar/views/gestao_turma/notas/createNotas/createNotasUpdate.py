from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from gestao_escolar.models import GestaoTurmas, Matriculas, Trimestre, TurmaDisciplina
from django import forms

class GestaoTurmasForm(forms.ModelForm):
    class Meta:
        model = GestaoTurmas
        fields = ['notas']

from django.http import QueryDict

def create_or_update_gestao_turmas(request, aluno_id, trimestre_id):
    aluno = get_object_or_404(Matriculas, pk=aluno_id)
    trimestre = get_object_or_404(Trimestre, pk=trimestre_id)
    disciplinas = TurmaDisciplina.objects.filter(turma=aluno.turma.id)

    if request.method == 'POST':
        for disciplina in disciplinas:
            # Verificar se já existe um registro para a combinação de aluno, trimestre e disciplina
            gestao_turma, created = GestaoTurmas.objects.get_or_create(aluno=aluno, trimestre=trimestre, grade=disciplina)
            form = GestaoTurmasForm(request.POST, instance=gestao_turma, prefix=disciplina.disciplina)  # Prefixo é o nome da disciplina
            if form.is_valid():
                form.save()
        return redirect(reverse('Gestao_Escolar:gestao_turmas_update', kwargs={'pk': aluno.turma.pk}))

    else:
        forms_dict = {}
        for disciplina in disciplinas:
            gestao_turma, created = GestaoTurmas.objects.get_or_create(aluno=aluno, trimestre=trimestre, grade=disciplina)
            initial_data = {'nota': gestao_turma.notas} if gestao_turma else None
            forms_dict[disciplina.disciplina] = GestaoTurmasForm(instance=gestao_turma, prefix=disciplina.disciplina, initial=initial_data)

    context = {
        'forms_dict': forms_dict,
        'aluno': aluno,
        'trimestre': trimestre,
        'conteudo_page': f"Gestão Turmas - Notas Update",
    }

    return render(request, 'Escola/inicio.html', context)
