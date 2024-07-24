# Generated by Django 5.0.4 on 2024-07-24 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0141_bairro_cidade_estado_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='bairro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.bairro'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestao_escolar.cidade'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('5', 'Viúvo'), ('1', 'Solteiro'), ('3', 'Separado'), ('6', 'União Estável'), ('2', 'Casado'), ('4', 'Divorciado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'), ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('5', 'AB+'), ('0', 'Não informado'), ('3', 'B+'), ('6', 'AB-'), ('2', 'A-'), ('7', 'O+'), ('1', 'A+'), ('4', 'B-'), ('8', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Transferido', 'Noturno'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
    ]
