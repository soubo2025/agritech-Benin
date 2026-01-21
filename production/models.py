from django.db import models

class Parcelle(models.Model):
    producteur = models.ForeignKey('users.Producteur', on_delete=models.CASCADE)
    superficie = models.FloatField(help_text="en hectares")
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return f"Parcelle de {self.producteur}"

class Recolte(models.Model):
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    date = models.DateField()
    quantite = models.FloatField(help_text="en tonnes")

    def __str__(self):
        return f"Récolte du {self.date}"
