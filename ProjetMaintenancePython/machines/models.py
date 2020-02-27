from django.db import models


class Niveau(models.Model):
    sfm = models.DecimalField(max_digits=5, decimal_places=2)
    m_min = models.DecimalField(max_digits=5, decimal_places=2)
    in_th = models.DecimalField(max_digits=5, decimal_places=2)
    mm_th = models.DecimalField(max_digits=5, decimal_places=2)
    nom = models.CharField(max_length=50)
    dia_in = models.DecimalField(max_digits=5, decimal_places=2)
    longueur_sortie_outil = models.DecimalField(max_digits=5, decimal_places=2)
    action = models.CharField(max_length=50)


class Modele(models.Model):
    nom = models.CharField(max_length=50)
    fabricant = models.CharField(max_length=50)
    type_machine = models.CharField(max_length=50)
    modèle = models.CharField(max_length=50)
    num_série = models.BigIntegerField()


class Essai(models.Model):
    ordre_essais = models.IntegerField()
    état = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    vitesse = models.IntegerField()
    vitesse_coupe = models.IntegerField()
    rpm = models.IntegerField()
    avancée = models.DecimalField(max_digits=5, decimal_places=2)
    alimentation_coupe = models.CharField(max_length=50)
    temps_coupe = models.DurationField()
    nom_matière = models.CharField(max_length=50)
    type_machine = models.CharField(max_length=50)
    nom_machine = models.CharField(max_length=50)
    fabricant = models.CharField(max_length=50)
    modèle = models.CharField(max_length=50)
    nom_outil = models.CharField(max_length=50)
