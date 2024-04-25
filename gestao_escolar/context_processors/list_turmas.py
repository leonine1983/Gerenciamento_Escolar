from gestao_escolar.models import Turmas


def list_turmas (request):
    contexto = {}
    ano = request.session['anoLetivo_id']
    escola =  request.session['escola_id']

    contexto ['turmas'] = Turmas.objects.filter(escola = escola, ano_letivo = ano)

    return contexto