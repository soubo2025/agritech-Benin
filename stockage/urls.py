

from django.urls import path
from .views import etat_stock

urlpatterns = [
    path('etat/', etat_stock, name='etat_stock'),
]




from django.urls import path
from .views import stock_list

urlpatterns = [
    path('stocks/', stock_list, name='stock_list'),
]
