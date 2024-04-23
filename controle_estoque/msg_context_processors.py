from django.http import request
from admin_acessos.models import message_user



def message_user_contexto(request):
    usuario = request.user.id
    contexto = {}
    contexto['usuario'] = message_user.objects.filter(user_id=usuario)
    contexto['aberto'] = message_user.objects.exclude(aberta=True)

    return contexto