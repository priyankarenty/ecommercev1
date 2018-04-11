import random
import os
from django.db import models
from django.db.models import Q,Count
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
import datetime
from django_pandas.managers import DataFrameManager

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,2342542352345)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format( new_filename=new_filename, final_filename=final_filename)

class ProductAccessoryQuerySet(models.query.QuerySet):
	def featured(self):
		return self.all()
	

	def search(self,query):
		lookups = Q(ProductName__icontains=query) | Q(Supplier__icontains=query)
		return self.filter(lookups).distinct()

class ProductAccessoryManager(models.Manager):
	def get_queryset(self):
		return ProductAccessoryQuerySet(self.model, using=self._db)

	def features(self):
		return self.get_queryset().featured()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

	def search(self, query):
		return self.get_queryset().search(query)

		return self.get_queryset().search(query)


class ProductAccessory(models.Model):
	MonthofEntry			= models.CharField(max_length=100,null=True, blank=True)
	DateofEntry				= models.DateField(auto_now_add=True, blank=True)
	slug 					= models.SlugField(blank=True,unique=True)
	ProductName 			= models.CharField(max_length=200,default="")
	ProductCategory	    	= models.CharField(max_length=50,default="")
	ProductType 			= models.CharField(max_length=100,null=True, blank=True)
	Specifications 			= models.TextField(null=True, blank=True)
	Warranty 				= models.NullBooleanField()
	WarrantyPeriod 			= models.CharField(max_length=100,null=True, blank=True)
	Image 					= models.FileField(upload_to=upload_image_path, null=True, blank=True)
	Supplier 				= models.CharField(max_length=100,default="")
	StockAvailable			= models.IntegerField(null=True, blank=True)
	SupplierType 			= models.CharField(max_length=100)
	Partnumber		 		= models.CharField(max_length=100, default="")
	UPC 					= models.CharField(max_length=100,null=True, blank=True)
	SKU 					= models.CharField(max_length=100,null=True, blank=True)
	Region					= models.CharField(max_length=100,null=True, blank=True)
	Country 				= models.CharField(max_length=100,null=True, blank=True)
	QuoteValidity 			= models.IntegerField(default=0)
	UnitofMeasure 			= models.CharField(max_length=100)
	Currency 				= models.CharField(max_length=100, default = "")
	TotalPrice 				= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	BasePriceperUnit 		= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	MarkupPriceperUnit 		= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	DeliveryChargeperunit 	= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	WarrantyPrice 			= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	AssetTagPrice			= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	Taxes					= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	RecycleFee 				= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	FreightCharge 			= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	AnyOtherFee 			= models.DecimalField(default = 0.00, decimal_places=2,max_digits=100)
	StockLeadTime 			= models.IntegerField(default = "")
	DeliveryLeadTime 		= models.IntegerField(default = "")
	PriceChange		    	= models.NullBooleanField()
	PriceChangeDate			= models.DateField(null=True, blank=True)
	GoogleApproverNameAvailable = models.NullBooleanField()
	GoogleApprover	 		= models.CharField(max_length=100,default = "",null=True, blank=True)
	ReasonForPriceChange	= models.CharField(max_length=100,default = "",null=True, blank=True)
	EoLStatus 				= models.NullBooleanField()
	EoLDate 				= models.DateField(null=True, blank=True)
	PreviousMPN 			= models.CharField(max_length=100,null=True, blank=True)
	PreviousPartNumber 		= models.CharField(max_length=100,null=True, blank=True)
	SplInstructions 		= models.CharField(max_length=100,null=True, blank=True)
	PriceApproved			= models.NullBooleanField()
	PriceApprovalDate		= models.DateField(null=True, blank=True)
	
	# def save(self, *args, **kwarg):
	# 	self.TotalPrice = self.BasePriceperUnit + self.MarkupPriceperUnit + self.DeliveryChargeperunit + self.WarrantyPrice + self.AssetTagPrice + self.Taxes + self.RecycleFee + self.FreightCharge + self.AnyOtherFee
	# 	super(ProductAccessory,self).save(*args, **kwarg)

	# def __str__(self):
	# 	return self.TotalPrice

	objects = ProductAccessoryManager()
	pdobjects = DataFrameManager()

	def get_absolute_url(self):
		return "/products/accessory/{slug}/".format(slug=self.slug)

	class Meta:
		verbose_name = 'Data Upload for Accessory'

	def __str__(self):
		return self.ProductName


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=ProductAccessory)
