from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q,Count
from django import forms
import csv
from django.http import HttpResponse
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng



def compare_home(request):
	x=request.POST.getlist('radio')
	table = Product.objects.filter(pk__in=x)

	return render(request,"home/deep/compare.html",{'table': table})
	# return render(request, 'compare.html',)

# def compare_update(request):

def compare_home_accessory(request):
	x=request.POST.getlist('radio')
	table = ProductAccessory.objects.filter(pk__in=x)

	return render(request,"home/deep/compare_aa.html",{'table': table})


def compare_home_aveng(request):
	x=request.POST.getlist('radio')
	table = ProductAVEng.objects.filter(pk__in=x)

	return render(request,"home/deep/compare_aa.html",{'table': table})




	# product_id=1
	# product_obj = Product.objects.get(id=product_id)
	# cart_obj,new_obj = Cart.objects.new_or_get(request)
	# cart_obj.products.add(obj)
	# return redirect(product_obj.get_absolute_url())


def export_hardware_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="hardware_catalog.csv"'
	writer = csv.writer(response)
	writer.writerow(['MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions'])
	products = Product.objects.all().values_list('MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions')
	for user in products:
		writer.writerow(user)
	return response

def export_accessory_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hardware_catalog.csv"'

    writer = csv.writer(response)
    writer.writerow(['MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions'])

    products = ProductAccessory.objects.all().values_list('MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions')
    for user in products:
        writer.writerow(user)

    return response


def export_aveng_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hardware_catalog.csv"'

    writer = csv.writer(response)
    writer.writerow(['MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions'])

    products = ProductAVEng.objects.all().values_list('MonthofEntry', 'DateofEntry', 'ProductName', 'ProductCategory', 'ProductType', 'RAM', 'HardDiskStorage', 'OS', 'Processor', 'TouchScreen', 'ScreenSize', 'ScreenBorder', 'Warranty', 'WarrantyPeriod', 'Image', 'Supplier', 'StockAvailable', 'SupplierType', 'OEM', 'VAR', 'UPC', 'SKU', 'Region', 'Country', 'QuoteValidity', 'UnitofMeasure', 'Currency', 'TotalPrice', 'BasePriceperUnit', 'MarkupPriceperUnit', 'DeliveryChargeperunit', 'WarrantyPrice', 'AssetTagPrice', 'Taxes', 'RecycleFee', 'FreightCharge', 'AnyOtherFee', 'StockLeadTime', 'DeliveryLeadTime', 'PriceChange', 'GoogleApproverNameAvailable', 'GoogleApprover', 'ReasonForPriceChange', 'EoLStatus', 'EoLDate', 'PreviousMPN', 'PreviousPartNumber', 'SplInstructions')
    for user in products:
        writer.writerow(user)

    return response

