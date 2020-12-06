from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save



class Usuario(AbstractUser):
    bio = models.TextField(blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefone = models.IntegerField(null=True, blank=True)
    endereço_completo = models.CharField(max_length=500, blank=True, null=True)
    nome_completo = models.CharField(max_length=500, blank=True, null=True)
    funçao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=Usuario)