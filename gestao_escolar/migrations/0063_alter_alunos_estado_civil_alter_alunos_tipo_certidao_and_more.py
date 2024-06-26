# Generated by Django 5.0.4 on 2024-05-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_escolar', '0062_alter_alunos_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('4', 'Divorciado'), ('6', 'União Estável'), ('1', 'Solteiro'), ('2', 'Casado'), ('3', 'Separado'), ('5', 'Viúvo')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_certidao',
            field=models.CharField(blank=True, choices=[('3', 'Outras'), ('2', 'Casamento'), ('1', 'Nascimento')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('8', 'O-'), ('7', 'O+'), ('1', 'A+'), ('0', 'Não informado'), ('4', 'B-'), ('2', 'A-'), ('5', 'AB+'), ('3', 'B+'), ('6', 'AB-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matriculas',
            name='escolarizacao_fora',
            field=models.CharField(choices=[('2', 'Em hospital'), ('1', 'Não recebe'), ('3', 'Em domicílio')], default=1, max_length=1),
        ),
    ]
