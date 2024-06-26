# Generated by Django 5.0.4 on 2024-05-03 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0015_turmas_descritivo_turma_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='res_atualiza_cadastro',
            field=models.CharField(default='Quem atualizou', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='alunos',
            name='res_cadastro',
            field=models.CharField(default='Quem criou o cadastro', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='etnia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.etnia', verbose_name='Etnia do aluno*:'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('2', 'A-'), ('4', 'B-'), ('8', 'O-'), ('0', 'Não informado'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('3', 'B+'), ('1', 'A+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('2', 'Casado'), ('3', 'Separado'), ('6', 'União Estável'), ('5', 'Viúvo'), ('1', 'Solteiro'), ('4', 'Divorciado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('1', 'Não recebe'), ('2', 'Em hospital')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Ativo', 'Na Turma'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Matutino', 'Matutino')], default=1, max_length=12),
        ),
    ]
