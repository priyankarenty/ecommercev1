from django.db import models
from django.conf import settings

from products.models import Product

User = settings.AUTH_USER_MODEL

class CompareManager(models.Manager):
	def new(self, user=None):
		return self.model.objects.create(user=user)

class CompareModel(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	products = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return str(self.id)
