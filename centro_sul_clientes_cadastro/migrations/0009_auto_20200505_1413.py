# Generated by Django 3.0.5 on 2020-05-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro_sul_clientes_cadastro', '0008_auto_20200505_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluido', 'Concluido')], max_length=255, verbose_name='Status'),
        ),
    ]