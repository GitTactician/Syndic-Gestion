from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class Residence(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    block_number = models.CharField(max_length=10)
    app_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Habitant(AbstractUser):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=255)
    name_hab = models.CharField(max_length=255)
    lost_connexion = models.CharField(max_length=255)

    # Specify unique related_name values
    groups = models.ManyToManyField(Group, related_name='habitant_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='habitant_user_permissions')

    def __str__(self):
        return self.username

class Syndic(AbstractUser):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    access_etat = models.CharField(max_length=30)
    
    # Specify unique related_name values
    groups = models.ManyToManyField(Group, related_name='syndic_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='syndic_user_permissions')

    def __str__(self):
        return self.username

class Reglement(models.Model):
    id_res = models.ForeignKey(Residence, on_delete=models.CASCADE)
    id_hab = models.ForeignKey(Habitant, on_delete=models.CASCADE)
    mois = models.CharField(max_length=10)
    etat = models.CharField(max_length=10)
    
    def __str__(self):
        return self.etat
