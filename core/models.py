from django.db import models

# Create your models here.

class Track(models.Model):
	autor = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	length = models.CharField(max_length=6)

	def __str__(self):
		return self.name
