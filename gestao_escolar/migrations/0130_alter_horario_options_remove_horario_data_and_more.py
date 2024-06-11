# Generated by Django 5.0.4 on 2024-06-11 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0129_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={},
        ),
        migrations.RemoveField(
            model_name='horario',
            name='data',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='dia_semana',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='turma_disciplina',
        ),
        migrations.AddField(
            model_name='horario',
            name='quarta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quarta_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AddField(
            model_name='horario',
            name='quinta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quinta_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AddField(
            model_name='horario',
            name='sabado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sabado_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AddField(
            model_name='horario',
            name='segunda',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='segunda_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AddField(
            model_name='horario',
            name='sexta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sexta_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AddField(
            model_name='horario',
            name='terca',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terca_prof', to='gestao_escolar.turmadisciplina'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Solteiro'), ('5', 'Viúvo'), ('3', 'Separado'), ('2', 'Casado'), ('4', 'Divorciado'), ('6', 'União Estável')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('1', 'Nascimento'), ('2', 'Casamento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('7', 'O+'), ('3', 'B+'), ('8', 'O-'), ('1', 'A+'), ('6', 'AB-'), ('4', 'B-'), ('5', 'AB+'), ('0', 'Não informado'), ('2', 'A-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nivel',
            field=models.CharField(choices=[('2', 'Superior'), ('1', 'Médio')], max_length=1),
        ),
        migrations.AlterField(
            model_name='horario',
            name='periodo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodo_Horario_related', to='gestao_escolar.periodo'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turma_Horario_related', to='gestao_escolar.turmas'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='validade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turma_Horario_related', to='gestao_escolar.validade_horario'),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('3', 'Em domicílio'), ('2', 'Em hospital'), ('1', 'Não recebe')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='tipo',
            field=models.CharField(choices=[('Ativo', 'Na Turma'), ('Desistente', 'Desistente/Evasão Escolar'), ('Transferido', 'Noturno')], default='Ativo', max_length=26, verbose_name='Tipo de remanejamento'),
        ),
    ]
