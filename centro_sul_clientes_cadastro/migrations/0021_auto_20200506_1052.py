# Generated by Django 3.0.5 on 2020-05-06 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centro_sul_clientes_cadastro', '0020_auto_20200506_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 13, 52, 2, 397275, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edit_data',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 13, 52, 2, 397245, tzinfo=utc)),
        ),
    ]