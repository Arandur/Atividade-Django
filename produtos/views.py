from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Listagem
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})

# Criação
def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

# Edição
def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

# Remoção
def remove_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete.html', {'produto': produto})
# vendas/views.py
from django.urls       import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.db.models import F, DecimalField, ExpressionWrapper
from .models  import Cliente, Venda
from .forms   import ClienteForm, VendaForm, VendaFilterForm


# -----------------  CLIENTE  -----------------
class ClienteListView(ListView):
    model               = Cliente
    template_name       = 'vendas/cliente_list.html'
    context_object_name = 'clientes'


class ClienteCreateView(CreateView):
    model         = Cliente
    form_class    = ClienteForm
    template_name = 'vendas/cliente_form.html'
    success_url   = reverse_lazy('cliente_list')


class ClienteUpdateView(UpdateView):
    model         = Cliente
    form_class    = ClienteForm
    template_name = 'vendas/cliente_form.html'
    success_url   = reverse_lazy('cliente_list')


class ClienteDeleteView(DeleteView):
    model         = Cliente
    template_name = 'vendas/cliente_confirm_delete.html'
    success_url   = reverse_lazy('cliente_list')


# ------------------  VENDA  ------------------
class VendaListView(ListView):
    """
    - Lista todas as vendas
    - Permite filtro por cliente, data inicial e data final
    - Anota o valor_total para usar em ordenação/template sem extra loop
    """
    model               = Venda
    template_name       = 'vendas/venda_list.html'
    context_object_name = 'vendas'

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .select_related('cliente', 'produto')
            .annotate(
                valor_total=ExpressionWrapper(
                    F('quantidade') * F('produto__preco'),
                    output_field=DecimalField(max_digits=12, decimal_places=2)
                )
            )
        )

        # filtros
        self.filter_form = VendaFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            cd = self.filter_form.cleaned_data
            if cd['cliente']:
                qs = qs.filter(cliente=cd['cliente'])
            if cd['data_inicial']:
                qs = qs.filter(data_venda__date__gte=cd['data_inicial'])
            if cd['data_final']:
                qs = qs.filter(data_venda__date__lte=cd['data_final'])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter_form'] = getattr(self, 'filter_form', VendaFilterForm())
        return ctx


class VendaCreateView(CreateView):
    model         = Venda
    form_class    = VendaForm
    template_name = 'vendas/venda_form.html'
    success_url   = reverse_lazy('venda_list')


class VendaUpdateView(UpdateView):
    model         = Venda
    form_class    = VendaForm
    template_name = 'vendas/venda_form.html'
    success_url   = reverse_lazy('venda_list')


class VendaDeleteView(DeleteView):
    model         = Venda
    template_name = 'vendas/venda_confirm_delete.html'
    success_url   = reverse_lazy('venda_list')
    # vendas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Cliente
    path('clientes/',                 views.ClienteListView.as_view(),   name='cliente_list'),
    path('clientes/novo/',            views.ClienteCreateView.as_view(), name='cliente_add'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    path('clientes/<int:pk>/apagar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # Venda
    path('vendas/',                 views.VendaListView.as_view(),   name='venda_list'),
    path('vendas/nova/',            views.VendaCreateView.as_view(), name='venda_add'),
    path('vendas/<int:pk>/editar/', views.VendaUpdateView.as_view(), name='venda_edit'),
    path('vendas/<int:pk>/apagar/', views.VendaDeleteView.as_view(), name='venda_delete'),
]