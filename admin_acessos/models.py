from django.db import models
from django.contrib.auth.models import  User
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from gestao_escolar.models import AnoLetivo


@receiver(post_migrate)
def create_groups_and_user(sender, **kwargs):
    group_names = ['Nutricionista', 'Professor', "Diretor", 'Aluno']

class message_user(models.Model):
    remetente = models.ForeignKey(User, null=True, on_delete=models.CASCADE, editable=False, verbose_name="Remetente da mensagem", related_name="sent_messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Pequise o nome do destinatário", related_name="received_messages")
    assunto = models.CharField(max_length=100, null=False, verbose_name='Escreva o assunto da sua mensagem')
    messagem = RichTextField(null=True, blank=True)
    aberta = models.BooleanField(default=False)
    foi_consultado = models.BooleanField(default=False)
    data_envio = models.DateTimeField(auto_now_add=True)
    exclude_msg = models.CharField(null=True, max_length=5)

    class Meta:
        ordering = ["-data_envio"]    

    def __str__(self) -> str:
        return self.assunto

@receiver(post_migrate)
def set_registro_teste(sender, **kwargs):
    if sender.name == 'admin_acessos':
        if not message_user.objects.exists():
            for user in User.objects.all():
                message_user.objects.create(
                    user=user,
                    assunto="Olá!",
                    messagem="Bem vindo ao nosso sistema!",
                )


class PaletaCores(models.Model):
    nome_paleta = models.CharField(max_length=20, default='Paleta Branca')
    cor_primaria = models.CharField(max_length=7, default='#fff')
    cor_secundaria = models.CharField(max_length=7, default='#fff')
    cor_sucesso = models.CharField(max_length=7, default='#fff')
    cor_info = models.CharField(max_length=7, default='#fff')
    cor_aviso = models.CharField(max_length=7, default='#fff')
    cor_perigo = models.CharField(max_length=7, default='#ffffff')
    cor_texto = models.CharField(max_length=7, default='#000')

    def __str__(self):
        return self.nome_paleta

class NomeclaturaJanelas(models.Model):
    nome_diciplina = models.CharField(max_length=50, default='')
    notas = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.nome_diciplina

    @receiver(post_migrate)
    def criarRegistro(sender, **kwargs):
        if not NomeclaturaJanelas.objects.exists():
            NomeclaturaJanelas.objects.create(
                nome_diciplina='Objetos da Aprendizagem/Disciplinas',
                notas = 'Notas do Aluno'
            )