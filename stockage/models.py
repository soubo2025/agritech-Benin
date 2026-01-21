from django.db import models
class Entrepot(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Stock(models.Model):
    entrepot = models.ForeignKey(Entrepot, on_delete=models.CASCADE)
    culture = models.CharField(max_length=10)
    quantite = models.FloatField()
    seuil_alerte = models.FloatField(default=100)

    def stock_bas(self):
        return self.quantite < self.seuil_alerte

