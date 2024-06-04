# Generated by Django 5.0.4 on 2024-05-28 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0071_gestaoturmas_profissional_resp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestaoturmas',
            name='data_hora_mod',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 13, 49, 31, 614980, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('2', 'Casado'), ('3', 'Separado'), ('4', 'Divorciado'), ('5', 'Viúvo'), ('1', 'Solteiro'), ('6', 'União Estável')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('7', 'O+'), ('6', 'AB-'), ('8', 'O-'), ('1', 'A+'), ('3', 'B+'), ('0', 'Não informado'), ('4', 'B-'), ('2', 'A-'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('2', 'Em hospital'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno'), ('Ativo', 'Na Turma')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Verspertino', 'Verspertino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]