from django.urls import path
from . views import (
    StockListView,
    StockDetailView,
    StockCreateView,
    SellsSellView,
    SellsDetailView,
    StockUpdateView,
    ClientCreateView,
    SellsUpdateView,
    delete_sale
)
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('magazine/', StockListView.as_view(), name='magazine'),
    path('magazine/<int:pk>/', StockDetailView.as_view(), name='magazine-detail'),
    path('magazine/new/', StockCreateView.as_view(), name='magazine-create'),
    path('magazine/update/<int:pk>/', StockUpdateView.as_view(), name='magazine-update'),
    path('sales/', views.sales, name='sales'),
    path('sales/<int:pk>/', SellsDetailView.as_view(), name='sales-detail'),
    path('sales/sell/', SellsSellView.as_view(), name='sales-sell'),
    path('sales/update/<int:pk>/', SellsUpdateView.as_view(), name='sells-update'),
    path('sales/delete/<int:pk>', views.delete_sale, name='sells-delete'),
    path('clients/', views.client, name='clients'),
    path('clients/new/', ClientCreateView.as_view(), name='client-create'),
]

