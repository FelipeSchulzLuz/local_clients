# Generated by Django 3.0.5 on 2020-05-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro_sul_clientes_cadastro', '0009_auto_20200505_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='anotacoes',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='edit_data',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='cliente',
            name='status_2',
            field=models.CharField(choices=[('Em analise', 'Em analise'), ('Confirmado', 'Confirmado'), ('Sem sinal', 'Sem sinal')], default='Em analise', max_length=255, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(default=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='detalhes_cliente',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluido', 'Concluido')], default='Concluido', max_length=255, verbose_name='Status'),
        ),
    ]
