# Generated by Django 5.0.4 on 2024-06-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0107_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('6', 'União Estável'), ('1', 'Solteiro'), ('4', 'Divorciado'), ('5', 'Viúvo'), ('3', 'Separado'), ('2', 'Casado')], max_length=13, null=True),
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
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('1', 'Nascimento'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('0', 'Não informado'), ('8', 'O-'), ('3', 'B+'), ('2', 'A-'), ('6', 'AB-'), ('4', 'B-'), ('1', 'A+'), ('7', 'O+'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('1', 'Não recebe'), ('3', 'Em domicílio'), ('2', 'Em hospital')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno'), ('Ativo', 'Na Turma')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
    ]