from django.shortcuts import render

from django.http import JsonResponse

# Exemple simple : renvoie l'état du stock sous forme de JSON
def etat_stock(request):
    # Exemple de données de stock
    stock_data = {
        "pommes": 50,
        "bananes": 30,
        "maïs": 100
    }
    return JsonResponse(stock_data)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Stock

@login_required
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stockage/stock_list.html', {'stocks': stocks})
