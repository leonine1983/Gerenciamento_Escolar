# Generated by Django 5.0.4 on 2024-05-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0051_alter_alunos_rg_uf_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('4', 'Divorciado'), ('6', 'União Estável'), ('2', 'Casado'), ('5', 'Viúvo'), ('3', 'Separado')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('1', 'Nascimento'), ('2', 'Casamento'), ('3', 'Outras')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('8', 'O-'), ('2', 'A-'), ('4', 'B-'), ('6', 'AB-'), ('3', 'B+'), ('1', 'A+'), ('7', 'O+'), ('0', 'Não informado'), ('5', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('1', 'Não recebe'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Transferido', 'Noturno'), ('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='turno',
            field=models.CharField(choices=[('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Matutino', 'Matutino')], default=1, max_length=12),
        ),
    ]