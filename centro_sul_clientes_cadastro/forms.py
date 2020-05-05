from django import forms
from .models import Cliente


class PostForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'detalhes_cliente', 'autor', 'data_criacao', 'status')

        