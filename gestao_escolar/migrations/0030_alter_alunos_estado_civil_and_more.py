# Generated by Django 5.0.4 on 2024-05-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0029_alter_alunos_estado_civil_alter_alunos_tipo_certidao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('4', 'Divorciado'), ('3', 'Separado'), ('2', 'Casado'), ('6', 'União Estável'), ('1', 'Solteiro'), ('5', 'Viúvo')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='justificativa_falta_document',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Justificativa da falta de documentação'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='local_diferenciado',
            field=models.CharField(blank=True, choices=[('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)'), ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados')], max_length=2, null=True, verbose_name='Local Diferenciado'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('2', 'Casamento'), ('3', 'Outras'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('4', 'B-'), ('8', 'O-'), ('5', 'AB+'), ('1', 'A+'), ('0', 'Não informado'), ('6', 'AB-'), ('2', 'A-'), ('3', 'B+'), ('7', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('1', 'Médio'), ('2', 'Superior')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('2', 'Em hospital'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Transferido', 'Noturno'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Matutino', 'Matutino')], default=1, max_length=12),
        ),
    ]