from django.conf import settings
from django.db import models
from django.utils import timezone




# Create your models here.


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=60)
    detalhes_cliente = models.TextField(max_length=400)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now,blank=True)
    updated = models.DateTimeField(auto_now=True)
    telefone = models.IntegerField(default=0)
    STATUS_TYPE_CHOICES = (('Aguardando avaliação','Aguardando avaliação'),('Concluido','Concluido'))
    status = models.CharField('Status', max_length=255,choices=STATUS_TYPE_CHOICES,default="Aguardando ser avaliado")
    STATUS_CHOICES_AVALIACAO = (('Em analise','Em analise'),('Concluido','Concluido'),('Sem sinal','Sem sinal'))
    avaliacao_localizacao = models.CharField('Avaliação', max_length=255,choices=STATUS_CHOICES_AVALIACAO, default='Em analise')
    STATUS_CHOICES_LOGRADOURO = (('Barra do Ribeiro','Barra do Ribeiro'),('Mariana Pimentel','Mariana Pimentel'),('Petim','Petim'), ('Passo da Estancia','Passo da Estancia'),('Douradilho','Douradilho'),('California City','California City'), ('N/D','N/D'))
    regiao_cliente = models.CharField('Cidade/Logradouro', max_length=255,choices=STATUS_CHOICES_LOGRADOURO, default='N/D')
    condicao_atendimento = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nome_cliente
