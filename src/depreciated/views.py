from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import Q,Avg
import csv
from itertools import chain
import requests


def eol_form(requests):
	# context={"form":form}
	return render(requests, 'reports/eol/eol_form.html')

def eol_table(request):
	pn = request.POST.get('partnumber')
	name = request.POST.get('productname')
	region =request.POST.getlist('region')
	category = request.POST.get('category')
	supplier = request.POST.get('supplier')
	fromdate = request.POST.get('fromdate')
	todate = request.POST.get('todate')

	qs = Product.pdobjects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	q = Product.objects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
	
	if category == "Hardware":
		if pn!=None:
			qs = Product.pdobjects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q = Product.objects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
		elif name!=None:
			qs = Product.pdobjects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q = Product.objects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			
		elif supplier!=None:
			qs = Product.pdobjects.filter(EoLStatus=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])
			q = Product.objects.filter(EoLStatus=True).filter(Supplier__iexact=supplier).filter(DateofEntry__range=[fromdate,todate])

		elif region!=None:
			qs = Product.pdobjects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q = Product.objects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])

		else:
			qs = Product.pdobjects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])
			q = Product.objects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])

	elif category == "Accessory":
		if pn!=None:
			qs = ProductAccessory.pdobjects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAccessory.objects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
		elif name!=None:
			qs = ProductAccessory.pdobjects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAccessory.objects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			
		elif region!=None:
			qs = ProductAccessory.pdobjects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAccessory.objects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			
		elif supplier!=None:
			qs = ProductAccessory.pdobjects.filter(EoLStatus=True).filter(Supplier__icontains=supplier).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAccessory.objects.filter(EoLStatus=True).filter(Supplier__icontains=supplier).filter(DateofEntry__range=[fromdate,todate])
			
		else:
			qs = ProductAccessory.pdobjects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAccessory.objects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])

	elif category == "AVEng":
		if pn!=None:
			qs = ProductAVEng.pdobjects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAVEng.objects.filter(EoLStatus=True).filter(Partnumber__iexact=pn).filter(DateofEntry__range=[fromdate,todate])
			
		elif name!=None:
			qs = ProductAVEng.pdobjects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAVEng.objects.filter(EoLStatus=True).filter(ProductName__icontains=name).filter(DateofEntry__range=[fromdate,todate])
			
		elif region!=None:
			qs = ProductAVEng.pdobjects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAVEng.objects.filter(EoLStatus=True).filter(Region__in=region).filter(DateofEntry__range=[fromdate,todate])
			
		elif supplier!=None:
			qs = ProductAVEng.pdobjects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate]).filter(Supplier__icontains=supplier)
			q = ProductAVEng.objects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate]).filter(Supplier__icontains=supplier)
			
		else:
			qs = ProductAVEng.pdobjects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])
			q = ProductAVEng.objects.filter(EoLStatus=True).filter(DateofEntry__range=[fromdate,todate])
	x = {"Supplier": "Supplier", "ProductCategory": "ProductCategory", "Region":"Region", "count" : "No. of EoL Products"}
	table = qs.to_pivot_table(values='EoLStatus', rows=['Region','ProductCategory','Supplier'],aggfunc=({'count'})).rename(columns=x)
	
	html_table = table.to_html()

	if category == "Hardware":
		template = "reports/eol/eol_table_h.html"
	elif category == "Accessory":
		template = "reports/eol/eol_table_a.html"
	elif category == "AVEng":
		template = "reports/eol/eol_table_a.html"

	return render(request, template,{'html_table':html_table,'q':q})