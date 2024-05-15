# Generated by Django 5.0.4 on 2024-05-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0019_alunos_sexo_alter_alunos_tipo_sanguineo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunos_documentacao',
            name='situacao_familiar',
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('1', 'A+'), ('6', 'AB-'), ('8', 'O-'), ('4', 'B-'), ('2', 'A-'), ('5', 'AB+'), ('0', 'Não informado'), ('3', 'B+'), ('7', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('6', 'União Estável'), ('5', 'Viúvo'), ('4', 'Divorciado'), ('1', 'Solteiro'), ('2', 'Casado'), ('3', 'Separado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos_documentacao',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('2', 'Casamento'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('1', 'Médio'), ('2', 'Superior')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('1', 'Não recebe'), ('2', 'Em hospital')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
    ]