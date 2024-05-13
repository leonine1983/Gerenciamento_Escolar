# Generated by Django 5.0.4 on 2024-05-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0024_alunos_cpf_alunos_rg_alunos_rg_uf_alunos_rg_emissao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('4', 'Divorciado'), ('3', 'Separado'), ('6', 'União Estável'), ('2', 'Casado'), ('1', 'Solteiro'), ('5', 'Viúvo')], max_length=13, null=True),
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
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('2', 'Casamento'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('6', 'AB-'), ('7', 'O+'), ('8', 'O-'), ('4', 'B-'), ('1', 'A+'), ('0', 'Não informado'), ('5', 'AB+'), ('3', 'B+'), ('2', 'A-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('1', 'Médio'), ('2', 'Superior')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('3', 'Em domicílio'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
    ]
