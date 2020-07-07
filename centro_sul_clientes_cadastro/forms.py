from django import forms
from .models import Cliente


class PostForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone','regiao_cliente', 'detalhes_cliente')

        


class PostFormEdit(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone', 'autor', 'regiao_cliente', 'avaliacao_localizacao', 'status','detalhes_cliente', 'condicao_atendimento')
