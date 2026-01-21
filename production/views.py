from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recolte
from users.utils import est_gestionnaire


@login_required
def liste_recoltes(request):
    if est_gestionnaire(request.user):
        recoltes = Recolte.objects.all()
    else:
        recoltes = Recolte.objects.filter(
            parcelle__producteur=request.user.producteur
        )

    return render(request, 'production/liste_recoltes.html', {
        'recoltes': recoltes
    })



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recolte

@login_required
def recolte_list(request):
    recoltes = Recolte.objects.all()
    return render(request, 'production/recolte_list.html', {'recoltes': recoltes})
