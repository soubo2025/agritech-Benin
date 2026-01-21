from django.db import models
from django.contrib.auth.models import AbstractUser

# Si tu veux étendre User, sinon on utilisera le User par défaut
from django.contrib.auth.models import User


class Commune(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Arrondissement(models.Model):
    nom = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.commune.nom}"


class Producteur(models.Model):
    ROLE_CHOICES = (
        ('PRODUCTEUR', 'Producteur'),
        ('GESTIONNAIRE', 'Gestionnaire'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=20)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='PRODUCTEUR')
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.user.username})"






