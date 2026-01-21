from django.forms import ModelForm
from .models import Recolte

class RecolteForm(ModelForm):
    class Meta:
        model = Recolte
        fields = ['parcelle', 'culture', 'quantite']
