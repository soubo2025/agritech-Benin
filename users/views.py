from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from users.utils import est_gestionnaire
from stockage.models import Stock

from .forms import ProducteurRegistrationForm
from .models import Producteur

# =========================
# INSCRIPTION PRODUCTEUR
# =========================
def register_producteur(request):
    if request.method == 'POST':
        form = ProducteurRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nom']
            user.last_name = form.cleaned_data['prenom']
            user.email = form.cleaned_data['email']
            user.save()

            Producteur.objects.create(
                user=user,
                nom=form.cleaned_data['nom'],
                prenom=form.cleaned_data['prenom'],
                telephone=form.cleaned_data['telephone'],
                commune=form.cleaned_data['commune'],
                arrondissement=form.cleaned_data['arrondissement'],
                role='PRODUCTEUR'
            )

            messages.success(request, "Votre compte producteur a été créé avec succès !")
            return redirect('login')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = ProducteurRegistrationForm()

    return render(request, 'users/register_producteur.html', {'form_register': form})


# =========================
# DASHBOARD PRODUCTEUR
# =========================
@login_required
def dashboard_producteur(request):
    return render(request, 'users/dashboard.html')


# =========================
# CONNEXION
# =========================
def connexion(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Identifiants incorrects"

    return render(request, 'users/login.html', {'error': error})


# =========================
# ÉTAT DU STOCK (GESTIONNAIRE)
# =========================
@login_required
def etat_stock(request):
    if not est_gestionnaire(request.user):
        return render(request, '403.html')

    stocks = Stock.objects.all()
    return render(request, 'stockage/etat_stock.html', {'stocks': stocks})
