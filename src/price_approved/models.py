
from django.db import models
import os
from django.db import models
from products.models import Product
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
import datetime


class PriceApprovedManager(models.Manager):
	def get_queryset(self):
		x=Product.objects.values(Q('VAR') | Q('OEM')).annotate(Count('id')).order_by().filter(id__count__gt=1)
		# y=part_number_var__in=[item['part_number_var'] for item in x]
		return super(DuplicateManager, self).get_queryset().filter(Q(VAR__in=[item['VAR'] for item in x])| Q(OEM__in=[item['OEM'] for item in x])).filter(PriceChange=True).filter(GoogleApprover__isnull=True)
		
class PriceApproved(Product):
	objects=PriceApprovedManager()

	class Meta:
		proxy = True