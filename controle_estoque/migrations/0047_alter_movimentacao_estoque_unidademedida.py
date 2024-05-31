# Generated by Django 5.0.4 on 2024-05-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0046_alter_movimentacao_estoque_unidademedida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao_estoque',
            name='unidadeMedida',
            field=models.CharField(choices=[('litros', 'litros'), ('kg', 'kg')], max_length=10, verbose_name='Unidade de Medida'),
        ),
    ]
