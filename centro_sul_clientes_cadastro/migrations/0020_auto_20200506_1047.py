# Generated by Django 3.0.5 on 2020-05-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro_sul_clientes_cadastro', '0019_auto_20200506_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='status_2',
            field=models.CharField(choices=[('Em analise', 'Em analise'), ('Confirmado', 'Confirmado'), ('Sem sinal', 'Sem sinal')], default='Em analise', max_length=255, verbose_name='Avaliação da localização'),
        ),
    ]
