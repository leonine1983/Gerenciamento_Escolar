# Generated by Django 5.0.4 on 2024-05-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0026_alter_alunos_estado_civil_alter_alunos_tipo_certidao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('4', 'Divorciado'), ('3', 'Separado'), ('6', 'União Estável'), ('1', 'Solteiro'), ('5', 'Viúvo'), ('2', 'Casado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('3', 'Outras'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('4', 'B-'), ('1', 'A+'), ('6', 'AB-'), ('2', 'A-'), ('8', 'O-'), ('3', 'B+'), ('7', 'O+'), ('0', 'Não informado'), ('5', 'AB+')], max_length=3, null=True),
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
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Desistente', 'Desistente/Evasão Escolar'), ('Ativo', 'Na Turma'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Verspertino', 'Verspertino'), ('Noturno', 'Noturno')], default=1, max_length=12),
        ),
    ]