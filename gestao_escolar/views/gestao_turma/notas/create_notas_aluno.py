from django.shortcuts import redirect
from django.urls import reverse
from gestao_escolar.models import Matriculas, GestaoTurmas

def verifica_e_cria_gestao_turmas(request):
    # Obtém todos os alunos matriculados
    matriculas = Matriculas.objects.all()

    # Itera sobre as matrículas e verifica se cada aluno já possui um registro em GestaoTurmas
    for matricula in matriculas:
        if not GestaoTurmas.objects.filter(matriculas_ptr=matricula).exists():
            # Se não existir, cria um novo registro com os campos vazios
            GestaoTurmas.objects.create(matriculas_ptr=matricula)
    
    # Redireciona para a UpdateView (ajuste o nome da URL conforme necessário)
    return redirect(reverse('Gestao_Escolar:gestao_turmas_update'))

