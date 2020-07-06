from django import forms
from .models import Cliente


class PostForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone', 'detalhes_cliente', 'autor','regiao_cliente')

        


class PostFormEdit(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone', 'detalhes_cliente', 'autor', 'regiao_cliente','condicao_atendimento', 'avaliacao_localizacao', 'status')
