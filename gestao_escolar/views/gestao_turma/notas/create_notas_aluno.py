from django.shortcuts import redirect
from django.urls import reverse
from gestao_escolar.models import Matriculas, GestaoTurmas

def verifica_e_cria_gestao_turmas(request, pk):
    # Obtém todos os alunos matriculados
    matriculas = Matriculas.objects.filter(turma=pk) 
    n = []
    # Itera sobre as matrículas e verifica se cada aluno já possui um registro em GestaoTurmas    
    for m in matriculas:
        n.append(m.id)
    
    for m in n: 
        if not GestaoTurmas.objects.filter(aluno= m):
            GestaoTurmas.objects.create(aluno = Matriculas.objects.get(pk = m))          
    """
    if not GestaoTurmas.objects.filter(matriculas_ptr=m.matricula.id).exists():
            # Se não existir, cria um novo registro com os campos vazios
            GestaoTurmas.objects.create(matriculas_ptr=m.matricula)
    """
    # Redireciona para a UpdateView (ajuste o nome da URL conforme necessário)
    return redirect(reverse('Gestao_Escolar:gestao_turmas_update', kwargs={'pk': pk}))

