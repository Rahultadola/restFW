from django.db import models

# Create your models here.
class ItemGood(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)



class ItemGood2(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)