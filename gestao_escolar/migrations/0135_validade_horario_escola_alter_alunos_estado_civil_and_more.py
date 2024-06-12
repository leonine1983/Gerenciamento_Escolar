# Generated by Django 5.0.4 on 2024-06-12 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0134_alter_alunos_estado_civil_alter_alunos_tipo_certidao_and_more'),
        ('rh', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='validade_horario',
            name='escola',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='escola_validade_related', to='rh.escola'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('4', 'Divorciado'), ('3', 'Separado'), ('6', 'União Estável'), ('2', 'Casado'), ('5', 'Viúvo')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('2', 'Casamento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('0', 'Não informado'), ('2', 'A-'), ('7', 'O+'), ('6', 'AB-'), ('4', 'B-'), ('8', 'O-'), ('5', 'AB+'), ('3', 'B+'), ('1', 'A+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Transferido', 'Noturno'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Verspertino', 'Verspertino')], default=1, max_length=12),
        ),
    ]
