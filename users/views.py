from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

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
            user.set_password(form.cleaned_data['password1'])
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

            messages.success(request, "Compte créé avec succès. Connectez-vous.")
            return redirect('login')
        else:
            messages.error(request, "Veuillez corriger les erreurs.")
    else:
        form = ProducteurRegistrationForm()

    return render(request, 'users/register.html', {
        'form_register': form
    })


# =========================
# CONNEXION
# =========================
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard_producteur')
        else:
            messages.error(request, "Identifiants incorrects")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {
        'form': form
    })


# =========================
# DASHBOARD PRODUCTEUR
# =========================
@login_required
def dashboard_producteur(request):
    return render(request, 'users/dashboard.html')


# =========================
# ÉTAT DU STOCK (GESTIONNAIRE)
# =========================
@login_required
def etat_stock(request):
    if not est_gestionnaire(request.user):
        return render(request, '403.html')

    stocks = Stock.objects.all()
    return render(request, 'stockage/etat_stock.html', {'stocks': stocks})
