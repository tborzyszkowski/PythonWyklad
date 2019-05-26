from django.shortcuts import render
from .models import stocks, clients, sells
from django.shortcuts import get_object_or_404
from .forms import SellForm
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

def DeleteSale(request):
    form = SellForm()
    return render(request, 'store/sales.html')

class StockListView(ListView):
    model = stocks
    template_name = 'store/magazine.html'
    context_object_name = 'stock'

class ClientCreateView(CreateView):
    model = clients
    fields = ['First_name', 'Last_name']

class SellsUpdateView(UpdateView):
    model = sells
    fields = ['stock', 'client', 'transaction_date']

class StockDetailView(DetailView):
    model = stocks

class SellsDetailView(DetailView):
    model = sells

class StockCreateView(CreateView):
    model = stocks
    fields = ['name', 'description', 'price', 'quantity']

class StockUpdateView(UpdateView):
    model = stocks
    fields = ['name', 'description', 'price', 'quantity']

class SellsSellView(CreateView):
    model = sells
    fields = ['stock', 'client', 'transaction_date']


def delete_sale(request, pk):
    template = 'store/sells_delete.html'
    sale = get_object_or_404(sells, pk=pk)

    try:
        if request.method == 'POST':
            form = SellForm(request.POST, instance=sale)
            sale.delete()
            messages.success(request, 'Usunięto')
        else:
            form = SellForm(instance=sale)
    except Exception as e:
        messages.warning(request, 'Error')

    context = {
        'form': form,
        'sale': sale,
    }
    return render(request, template, context)

def sellStock(request):
    context = {
        'st': stocks.objects.all()
    }
    return render(request, 'store/sales_sell.html', context)


def home(request):
    operations = ['Sprzedaż', 'Magazyn', 'Baza Klientów']
    context = {
        'op': operations
    }
    return render(request, 'store/home.html', context)


def ware(request):
    context = {
        'stock': stocks.objects.all()
    }
    return render(request, 'store/magazine.html', context)


def client(request):
    context = {
        'kl': clients.objects.all()
    }
    return render(request, 'store/clients.html', context)

def sales(request):
    context = {
        'sl': sells.objects.all()
    }
    return render(request, 'store/sales.html', context)