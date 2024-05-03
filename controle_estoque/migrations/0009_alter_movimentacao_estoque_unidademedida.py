# Generated by Django 5.0.4 on 2024-05-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0008_remove_programacaosaidaestoque_escola_beneficiaria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao_estoque',
            name='unidadeMedida',
            field=models.CharField(choices=[('litros', 'litros'), ('kg', 'kg')], max_length=10, verbose_name='Unidade de Medida'),
        ),
    ]
