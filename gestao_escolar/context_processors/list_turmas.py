from gestao_escolar.models import Turmas


def list_turmas (request):
    contexto = {}
    contexto ['turmas'] = Turmas.objects.all()

    return contexto