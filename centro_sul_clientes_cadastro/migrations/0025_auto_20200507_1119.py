# Generated by Django 3.0.5 on 2020-05-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro_sul_clientes_cadastro', '0024_auto_20200506_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
    ]
