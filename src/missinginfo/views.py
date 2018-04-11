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



def mi_form(requests):
	
	return render(requests, 'reports/mi/mi_form.html')

def mi_table(requests):
	pn = requests.POST.get('partnumber')
	name = requests.POST.get('productname')
	region =requests.POST.getlist('region')
	category = requests.POST.get('category')
	supplier  = requests.POST.get('supplier')
	fromdate = requests.POST.get('fromdate')
	todate = requests.POST.get('todate')

	q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	q2 = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	qs1 = read_frame(q1)
	qs2 = read_frame(q2)
	

	if category == "Hardware":
		if pn!=None:
			q2 = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
		elif name!=None:
			q2 = Product.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
				
		elif supplier!=None:
			q2 = Product.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			
		elif region!=None:
			q2 = Product.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			
		else:
			q2 = Product.objects.filter(DateofEntry__range=[fromdate,todate])
			
	elif category == "Accessory":
		if pn!=None:
			q2 = ProductAccessory.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
			
		elif name!=None:
			q2 = ProductAccessory.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			
		elif supplier!=None:
			q2 = ProductAccessory.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			
		elif region!=None:
			q2 = ProductAccessory.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])

		else:
			q2 = ProductAccessory.objects.filter(DateofEntry__range=[fromdate,todate])
			
	elif category == "AVEng":
		if pn!=None:
			q2 = ProductAVEng.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
		elif name!=None:
			q2 = ProductAVEng.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])		
			
		elif supplier!=None:
			q2 = ProductAVEng.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			
		elif region!=None:
			q2 = ProductAVEng.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])		

	else:
			q2 = ProductAVEng.objects.filter(DateofEntry__range=[fromdate,todate])
			
	qs2 = read_frame(q2)
	qs2['MissingInfo'] = qs2.apply(lambda x: x.isnull().sum(), axis='columns')
	qs2['Total'] = qs2.apply(lambda x: x.count(), axis='columns')
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "MissingInfo" : "Products with Missing Info", "Total": "Total No. of Products"}

	table = qs2.groupby(['Supplier','ProductCategory','Region'])[['MissingInfo']].sum()
	table1 = qs2.groupby(['Supplier','ProductCategory','Region'])[['Total']].sum()
	table = pd.merge(table,table1, left_index=True, right_index=True)
	table['Missing Info %'] = ((table.MissingInfo/table.Total) * 100).round(1)
	table= table.rename(columns=x)
	
	html_table = table.to_html()
	print(q2)

	if category == "Hardware":
		template = "reports/mi/mi_table_h.html"
	elif category == "Accessory":
		template = "reports/mi/mi_table_a.html"
	elif category == "AVEng":
		template = "reports/mi/mi_table_a.html"

	return render(requests, template,{'html_table':html_table,'q2':q2})