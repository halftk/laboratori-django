from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
	name = models.CharFierld(max_length= 40)

class Sobre(models.Model):
	date = models.DateTimeField()
	amount = models.IntegerField()
	concept = models.TextField(max_length=100)
	donor = models.ForeignKey(Donor)
	user = models.ForeignKey(User)
