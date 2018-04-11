from django.db import models
import os
from django.db import models

from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.db.models import Q,Count
# from django.db.models.signals import pre_save, post_save
import datetime
from django_pandas.managers import DataFrameManager


class DuplicateManager(models.Manager):

	def get_queryset(self):
		x=Product.objects.values('Partnumber').annotate(Count('id')).order_by().filter(id__count__gt=1)
		# y=part_number_var__in=[item['part_number_var'] for item in x]
		return super(DuplicateManager, self).get_queryset().filter(Partnumber__in=[item['Partnumber'] for item in x]).filter(PriceChange=False)
		
	
class Duplicate(Product):
	objects=DuplicateManager()
	hpdobjects = DataFrameManager()

	class Meta:
		proxy = True
		verbose_name = 'Duplicate_Hardware'





class DuplicateAccessoryManager(models.Manager):

	def get_queryset(self):
		x=ProductAccessory.objects.values('Partnumber').annotate(Count('id')).order_by().filter(id__count__gt=1)
		# y=part_number_var__in=[item['part_number_var'] for item in x]
		return super(DuplicateAccessoryManager, self).get_queryset().filter(Partnumber__in=[item['Partnumber'] for item in x]).filter(PriceChange=False)
		
class DuplicateAccessory(ProductAccessory):
	objects=DuplicateAccessoryManager()
	acpdobjects = DataFrameManager()

	class Meta:
		proxy = True
		verbose_name = 'Duplicate_Accessory'





class DuplicateAVEngManager(models.Manager):

	def get_queryset(self):
		x=ProductAVEng.objects.values('Partnumber').annotate(Count('id')).order_by().filter(id__count__gt=1)
		# y=part_number_var__in=[item['part_number_var'] for item in x]
		return super(DuplicateAVEngManager, self).get_queryset().filter(Partnumber__in=[item['Partnumber'] for item in x]).filter(PriceChange=False)
		
	
class DuplicateAVEng(ProductAVEng):
	objects=DuplicateAVEngManager()
	avpdobjects = DataFrameManager()


	class Meta:
		proxy = True

		verbose_name = 'Duplicate_AVEng'
		