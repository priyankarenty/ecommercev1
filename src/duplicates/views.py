from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from duplicates.models import Duplicate,DuplicateAccessory,DuplicateAVEng
from django.views.generic import View
from django.db.models import Q,Avg
from itertools import chain
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import csv
from itertools import chain
import requests



def duplicates_form(requests):
	return render(requests, 'reports/duplicates/duplicates_form.html')

def duplicates_table(request):
	pn = request.POST.get('partnumber')
	name = request.POST.get('productname')
	region =request.POST.getlist('region')
	category = request.POST.get('category')
	supplier = request.POST.get('supplier')
	fromdate = request.POST.get('fromdate')
	todate = request.POST.get('todate')

	q = Duplicate.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	qs = read_frame(q)
	
	if category == "Hardware":
		if pn!=None:
			q = Duplicate.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = Duplicate.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = Duplicate.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = Duplicate.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = Duplicate.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

	elif category == "Accessory":
		if pn!=None:
			q = DuplicateAccessory.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = DuplicateAccessory.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = DuplicateAccessory.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = DuplicateAccessory.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = DuplicateAccessory.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

	elif category == "AVEng":
		if pn!=None:
			q = DuplicateAVEng.objects.filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif name!=None:
			q = DuplicateAVEng.objects.filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
			
		elif supplier!=None:
			q = DuplicateAVEng.objects.filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		elif region!=None:
			q = DuplicateAVEng.objects.filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)

		else:
			q = DuplicateAVEng.objects.filter(DateofEntry__range=[fromdate,todate])
			qs = read_frame(q)
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "Partnumber" : "No. of Duplicates"}
	
	table =  qs.pivot_table(index=['Supplier','ProductCategory','Region'], values=['Partnumber'],aggfunc=({'count'})).rename(columns=x)
	table.columns = table.columns.droplevel([-1])

	html_table = table.to_html()	
	return render(request, 'reports/duplicates/duplicates_table.html',{'html_table':html_table, 'q':q})
