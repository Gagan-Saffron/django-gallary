from django.db import models

# Create your models here.

class Image(models.Model):
	picture=models.ImageField()
	description=models.CharField(max_length=25,)