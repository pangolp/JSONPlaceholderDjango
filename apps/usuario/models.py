from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Generador(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=50)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_user_generador(sender, instance, created, **kwargs):
	if created:
		Generador.objects.create(user=instance)
