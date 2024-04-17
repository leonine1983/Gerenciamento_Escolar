from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                         Group, Permission, PermissionsMixin)
from django.dispatch import receiver
from django.db.models.signals import post_migrate, pre_save, post_save
from django.conf import settings
from ckeditor.fields import RichTextField
from django.apps import apps
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_groups_and_user(sender, **kwargs):
    group_names = ['Nutricionista', 'Professor', "Diretor", 'Aluno']

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    
    first_name = models.CharField(max_length=30)
    foto = models.ImageField(null=True)
    last_name = models.CharField(max_length=30, null=True)
    telefone = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20, null=True)
    data_nascimento = models.DateField(null=True)
    endereco = models.CharField(max_length=255, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    objects = CustomUserManager()    

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.first_name
    

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'foto', 'telefone', 'data_nascimento', 'endereco')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    
    formfield_overrides = {
        CustomUser._meta.get_field('password'): {'widget': ReadOnlyPasswordHashField},
    }


class message_user(models.Model):
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, editable=False, verbose_name="Remetente da mensagem", related_name="sent_messages")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Pequise o nome do destinatário", related_name="related_message")
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
            for user in CustomUser.objects.all():
                message_user.objects.create(
                    user=user,
                    assunto="Olá!",
                    messagem="Bem vindo ao nosso sistema!",
                )




