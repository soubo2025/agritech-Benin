from django.contrib import admin
from .models import Commune, Arrondissement, Producteur

admin.site.register(Commune)
admin.site.register(Arrondissement)
admin.site.register(Producteur)

