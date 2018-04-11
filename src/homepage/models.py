from django.db import models
import os
from products.models import Product
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
import datetime
import django_filters

class HomeManager(models.Manager):
	pass

class HomePage(Product):
	objects=HomeManager()

	class Meta:
		proxy = True
		ordering = ('ProductName','ProductCategory',)



class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['ProductName','ProductCategory', 'Supplier']