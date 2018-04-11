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
import datetime
import dateutil.relativedelta



def npa_form(requests):
	
	return render(requests, 'reports/npa/npa_form.html')

def npa_table(requests):
	pn = requests.POST.get('partnumber')
	name = requests.POST.get('productname')
	region =requests.POST.getlist('region')
	category = requests.POST.get('category')
	supplier  = requests.POST.get('supplier')
	fromdate1 = requests.POST.get('fromdate')
	fromdate = datetime.datetime.strptime(fromdate1, "%Y-%m-%d").date()
	todate1 = requests.POST.get('todate')
	todate = datetime.datetime.strptime(fromdate1, "%Y-%m-%d").date()
	lastfromdate = fromdate + dateutil.relativedelta.relativedelta(months=-1)
	lasttodate = fromdate + dateutil.relativedelta.relativedelta(months=-1)
	lastfromdate1 = lastfromdate.strftime('%Y-%m-%d')
	lasttodate1 = lasttodate.strftime('%Y-%m-%d')

	
	
	q1 = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	q2 = Product.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	s1 = read_frame(q1)
	s2 = read_frame(q2)
	q=0
	

	if category == "Hardware":
		if pn!=None:
			q1 = Product.objects.exclude(Partnumber__in=q2).values('Partnumber').filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
			
		elif name!=None:
			q1 = Product.objects.exclude(Partnumber__in=q2).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
		
		elif supplier!=None:
			q1 = Product.objects.exclude(Partnumber__in=q2).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		elif region!=None:
			q1 = Product.objects.exclude(Partnumber__in=q2).filter(Region__in=region).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(Region__in=region).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		else:
			q1 = Product.objects.exclude(Partnumber__in=q2).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

			
	elif category == "Accessory":
		if pn!=None:
			q1 = ProductAccessory.objects.exclude(Partnumber__in=q2).values('Partnumber').filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAccessory.objects.values_list('Partnumber',flat=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
			
		elif name!=None:
			q1 = ProductAccessory.objects.exclude(Partnumber__in=q2).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAccessory.objects.values_list('Partnumber',flat=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
		
		elif supplier!=None:
			q1 = ProductAccessory.objects.exclude(Partnumber__in=q2).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAccessory.objects.values_list('Partnumber',flat=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		elif region!=None:
			q1 = ProductAccessory.objects.exclude(Partnumber__in=q2).filter(Region__in=region).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAccessory.objects.values_list('Partnumber',flat=True).filter(Region__in=region).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		else:
			q1 = ProductAccessory.objects.exclude(Partnumber__in=q2).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAccessory.objects.values_list('Partnumber',flat=True).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
		
	elif category == "AVEng":
		if pn!=None:
			q1 = ProductAVEng.objects.exclude(Partnumber__in=q2).values('Partnumber').filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q2 = ProductAVEng.objects.values_list('Partnumber',flat=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
			
		elif name!=None:
			q1 = ProductAVEng.objects.exclude(Partnumber__in=q2).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAVEng.objects.values_list('Partnumber',flat=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
		
		elif supplier!=None:
			q1 = ProductAVEng.objects.exclude(Partnumber__in=q2).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = Product.objects.values_list('Partnumber',flat=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		elif region!=None:
			q1 = ProductAVEng.objects.exclude(Partnumber__in=q2).filter(Region__in=region).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAVEng.objects.values_list('Partnumber',flat=True).filter(Region__in=region).filter(DateofEntry__range=[lastfromdate1,lasttodate1])

		else:
			q1 = ProductAVEng.objects.exclude(Partnumber__in=q2).filter(DateofEntry__range=[fromdate1,todate1])
			q2 = ProductAVEng.objects.values_list('Partnumber',flat=True).filter(DateofEntry__range=[lastfromdate1,lasttodate1])
	
	
	s1 = read_frame(q1)
	s2 = read_frame(q2)
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "Partnumber" : "No. of New Products"}

	table = s1.groupby(['Supplier','ProductCategory','Region'])[['Partnumber']].nunique().rename(columns=x)	
	html_table = table.to_html()

	if category == "Hardware":
		template = "reports/npa/npa_table_h.html"
	elif category == "Accessory":
		template = "reports/npa/npa_table_a.html"
	elif category == "AVEng":
		template = "reports/npa/npa_table_a.html"



	return render(requests, template,{'html_table':html_table,'q1':q1})