from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.views.generic import View
from django.db.models import Q,Avg
from itertools import chain
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import csv




def lta_form(requests):
	
	return render(requests, 'reports/lta/lta_form.html')

def lta_table(request):
	pn = request.POST.get('partnumber')
	name = request.POST.get('productname')
	region =request.POST.getlist('region')
	category = request.POST.get('category')
	supplier = request.POST.get('supplier')
	fromdate = request.POST.get('fromdate')
	todate = request.POST.get('todate')

	q = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	qs = read_frame(q)
	
	if category == "Hardware":
		if pn!=None:
			q = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = Product.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = Product.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = Product.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = Product.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

	elif category == "Accessory":
		if pn!=None:
			q = ProductAccessory.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = ProductAccessory.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = ProductAccessory.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = ProductAccessory.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = ProductAccessory.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

	elif category == "AVEng":
		if pn!=None:
			q = ProductAVEng.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = ProductAVEng.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = ProductAVEng.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = ProductAVEng.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = ProductAVEng.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "DeliveryLeadTime": "Delivery Lead Time", "StockAvailable": "Stock Available","StockLeadTime":"Stock Lead Time" }
	table =  qs.pivot_table(index=['Supplier','ProductCategory','Region'], values=['StockLeadTime','DeliveryLeadTime','StockAvailable'],aggfunc=({'mean'})).round(1)
	# table.columns = table.columns.droplevel([0])
	
	table.columns = table.columns.droplevel([-1])
	table = table.rename(columns=x)
	# table = table.reset_index(level=, drop=True).reset_index()
	# table.columns = table.columns.droplevel(-1)
	html_table = table.to_html()


	if category == "Hardware":
		template = "reports/lta/lta_table_h.html"
	elif category == "Accessory":
		template = "reports/lta/lta_table_a.html"
	elif category == "AVEng":
		template = "reports/lta/lta_table_a.html"

	return render(request, template,{'html_table':html_table,'q':q})

