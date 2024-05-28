from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from gestao_escolar.models import GestaoTurmas, Matriculas, Trimestre, TurmaDisciplina
from django import forms
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class GestaoTurmasForm(forms.ModelForm):
    notas = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MaxValueValidator(10.00, message="O valor não pode ser maior que 10.00.")],
        required=False
    )
    
    class Meta:
        model = GestaoTurmas
        fields = ['notas', 'faltas']


from django.http import QueryDict
from django.db.models import Sum
@login_required
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
                form.instance.profissional_resp = request.user.username
                form.instance.data_hora_mod = timezone.now()

                # Recuperar todas as notas do aluno para a disciplina atual
                notas_aluno = GestaoTurmas.objects.filter(aluno=aluno, grade=disciplina).aggregate(Sum('notas'))
                total_notas = notas_aluno['notas__sum']
                
                ano_letivo = aluno.turma.ano_letivo
                quant_trimestres = Trimestre.objects.filter(ano_letivo=ano_letivo).count()

                # Calcular a média final se houver notas
                if total_notas is not None:
                    media_final = total_notas / (quant_trimestres - 1)
                    form.instance.media_final = media_final

                form.save()
        return redirect(reverse('Gestao_Escolar:gestao_turmas_update', kwargs={'pk': aluno.turma.pk}))

    else:
        forms_dict = {}
        for disciplina in disciplinas:
            gestao_turma, created = GestaoTurmas.objects.get_or_create(aluno=aluno, trimestre=trimestre, grade=disciplina)
            initial_data = {'nota': gestao_turma.notas, 'faltas': gestao_turma.faltas} if gestao_turma else None
            forms_dict[disciplina.disciplina] = GestaoTurmasForm(instance=gestao_turma, prefix=disciplina.disciplina, initial=initial_data)

    context = {
        'forms_dict': forms_dict,
        'aluno': aluno,
        'trimestre': trimestre,
        'conteudo_page': f"Gestão Turmas - Notas Update",
    }

    return render(request, 'Escola/inicio.html', context)
