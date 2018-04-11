from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.http import JsonResponse
from django.views.generic import View
from controlcenter import Dashboard, widgets
from rest_framework.views import APIView
from rest_framework.response import Response
from chartit import DataPool, Chart

def stock_form(request):
  return render(request,'charts/stockchart/stock.html')

def stock_chart_view(request):
  category = request.POST.get('category')
  part = request.POST.get('partnumber')

  if category == "Hardware":
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': Product.objects.filter(Partnumber__icontains=part)},
              'terms': [
                'DateofEntry',
                'StockLeadTime']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'DateofEntry':[ 
                    'StockLeadTime']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Stock Lead Time Fluctuation Trend'},
               'xAxis': {
                    'title': {
                       'text': 'Date of Entry'}}})

  elif category == "Accessory":
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': ProductAccessory.objects.filter(Partnumber__icontains=part)},
              'terms': [
                'DateofEntry',
                'StockLeadTime']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'DateofEntry':[ 
                    'StockLeadTime']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Stock Lead Time Fluctuation Trend'},
               'xAxis': {
                    'title': {
                       'text': 'Date of Entry'}}})
  
  elif category == "AVEng":
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': ProductAVEng.objects.filter(Partnumber__icontains=part)},
              'terms': [
                'DateofEntry',
                'StockLeadTime']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'DateofEntry':[ 
                    'StockLeadTime']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Stock Lead Time Fluctuation Trend'},
               'xAxis': {
                    'title': {
                       'text': 'Date of Entry'}}})

  return render(request,'charts/stockchart/stockchart.html',{'weatherchart': cht})