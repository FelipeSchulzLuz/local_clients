from django.conf import settings
from django.db import models
from django.utils import timezone




# Create your models here.


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=60)
    detalhes_cliente = models.TextField(max_length=400)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)
    STATUS_TYPE_CHOICES = (('Pendente','Pendente'),('Concluido','Concluido'))
    status = models.CharField('Status', max_length=255,choices=STATUS_TYPE_CHOICES)
    

    def __str__(self):
        return self.nome_cliente
