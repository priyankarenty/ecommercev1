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

def pa_form(requests):
	return render(requests, 'reports/pa/pa_form.html')

def pa_table(requests):
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
			q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif name!=None:
			q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif supplier!=None:
			q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		elif region!=None:
			q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		else:
			q1 = Product.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

	elif category == "Accessory":
		if pn!=None:
			q1 = ProductAccessory.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif name!=None:
			q1 = ProductAccessory.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif supplier!=None:
			q1 = ProductAccessory.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		elif region!=None:
			q1 = ProductAccessory.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		else:
			q1 = ProductAccessory.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
	
	elif category == "AVEng":
		if pn!=None:
			q1 = ProductAVEng.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif name!=None:
			q1 = ProductAVEng.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)
			
		elif supplier!=None:
			q1 = ProductAVEng.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		elif region!=None:
			q1 = ProductAVEng.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

		else:
			q1 = ProductAVEng.objects.filter(PriceChange=True).filter(PriceApproved=True).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.filter(DateofEntry__range=[fromdate,todate])
			qs1 = read_frame(q1)
			qs2 = read_frame(q2)

	table1 = qs1.groupby(['Supplier','ProductCategory','Region'])[['Partnumber']].count()
	table2 = qs2.groupby(['Supplier','ProductCategory','Region'])[['Partnumber']].count()
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "Partnumber_x" : "No. of Price Approvals", "Partnumber_y": "Total No.of Products", "Approved %":"Approved %"}
	
	table = pd.merge(table1,table2, left_index=True, right_index=True)
	table['Approved %'] = ((table.Partnumber_x /table.Partnumber_y) * 100).round(2)
	table= table.rename(columns=x)


	html_table = table.to_html()

	if category == "Hardware":
		template = "reports/pa/pa_table_h.html"
	elif category =="Accessory":
		template = "reports/pa/pa_table_a.html"
	elif category == "AVEng":
		template = "reports/pa/pa_table_a.html"


	return render(requests, template,{'html_table':html_table, 'q1':q1})