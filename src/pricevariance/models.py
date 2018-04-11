
from django.db import models
import os
from django.db import models
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
import datetime

class PriceApprovedManager(models.Manager):
	def get_queryset(self):
		x=Product.objects.values(Q('VAR') | Q('OEM')).annotate(Count('id')).order_by().filter(id__count__gt=1)
		a = Product.objects.filter(created_at__year=today.year, created_at__month=today.month)
		last_month = today.month - 1 if today.month>1 else 12
		last_month_year = today.year if today.month > last_month else today.year - 1
		b = Product.objects.filter(created_at__year=today.year, created_at__month=last.month)
		# if a.TotalPrice = b.TotalPrice:
		return super(DuplicateManager, self).get_queryset().filter(Q(VAR__in=[item['VAR'] for item in x])| Q(OEM__in=[item['OEM'] for item in x])).filter(TotalPrice=TotalPrice)
		
class PriceApproved(Product):
	objects=PriceApprovedManager()

	class Meta:
		proxy = True