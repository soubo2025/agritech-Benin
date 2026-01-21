from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from production.models import Recolte


@login_required
def dashboard(request):
    stats = (
        Recolte.objects
        .values(
            'parcelle__producteur__arrondissement__commune__nom',
            'culture'
        )
        .annotate(total=Sum('quantite'))
    )

    return render(request, 'dashboard/dashboard.html', {
        'stats': stats
    })



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from production.models import Recolte

@login_required
def dashboard(request):
    data = Recolte.objects.values(
        'parcelle__producteur__arrondissement__commune__nom'
    ).annotate(total=Sum('quantite'))

    return render(request, 'dashboard/dashboard.html', {'data': data})
