from django import forms
from django.contrib.auth.models import User
from .models import Producteur, Commune, Arrondissement
from django.contrib.auth.forms import UserCreationForm


class ProducteurRegistrationForm(UserCreationForm):
    nom = forms.CharField(max_length=150, required=True)
    prenom = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=20, required=True)
    commune = forms.ModelChoiceField(queryset=Commune.objects.all(), required=True)
    arrondissement = forms.ModelChoiceField(queryset=Arrondissement.objects.none(), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'nom', 'prenom', 'telephone', 'commune', 'arrondissement', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'commune' in self.data:
            try:
                commune_id = int(self.data.get('commune'))
                self.fields['arrondissement'].queryset = Arrondissement.objects.filter(commune_id=commune_id).order_by('nom')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['arrondissement'].queryset = Arrondissement.objects.none()
