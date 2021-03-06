# Generated by Django 3.0.8 on 2020-07-07 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centro_sul_clientes_cadastro', '0026_auto_20200507_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='autor',
            field=models.ForeignKey(default='settings.AUTH_USER_MODEL', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='status',
            field=models.CharField(choices=[('Aguardando avaliação', 'Aguardando avaliação'), ('Concluido', 'Concluido')], default='Aguardando ser avaliado', max_length=255, verbose_name='Status'),
        ),
    ]
