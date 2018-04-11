from django.db import models
import os
from django.db import models

from products.models import Product
from django.db.models import Q,Count
# from django.db.models.signals import pre_save, post_save
import datetime


class DepreciatedManager(models.Manager):

	def get_queryset(self):
		return super(DepreciatedManager, self).get_queryset().filter(EoLStatus="True") 


class Depreciated(Product):
	objects=DepreciatedManager()

	class Meta:
		proxy = True

		verbose_name = 'EoL'
		