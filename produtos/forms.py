from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta: # armazena metadados
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque']
        # vendas/forms.py
from django import forms
from .models import Cliente, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nome', 'email', 'data_nascimento']
        widgets = {'data_nascimento': forms.DateInput(attrs={'type': 'date'})}


class VendaForm(forms.ModelForm):
    class Meta:
        model  = Venda
        fields = ['cliente', 'produto', 'quantidade', 'data_venda']
        widgets = {
            'data_venda': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# formulário só para filtros da tela central
class VendaFilterForm(forms.Form):
    cliente      = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), required=False, label='Cliente')
    data_inicial = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    data_final   = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))