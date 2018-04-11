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
from bokeh.plotting import figure
from bokeh.resources import CDN
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import numpy as np
import datetime
from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource,WheelZoomTool, PanTool, BoxZoomTool, ResetTool, TapTool,  HoverTool,LabelSet,DatetimeTickFormatter


def price_form(request):
  return render(request,'charts/price.html')

def weather_chart_view(request):
  category = request.POST.get('category')
  partnumber = request.POST.get('partnumber')
  fromdate = request.POST.get('fromdate')
  todate = request.POST.get('todate')
  # productname= Product.objects.values_list('ProductName', flat=True).get(Partnumber__icontains=partnumber)
  # currency = Product.objects.values_list('Currency', flat=True).get(Partnumber__icontains=partnumber)

  # if category=="Hardware":
  #   productname= Product.objects.values("ProductName").get(Partnumber__icontains=partnumber).distinct().order_by()
  #   currency = Product.objects.values("Currency").get(Partnumber__icontains=partnumber).distinct().order_by()
  # elif category=="Accessory":
  #   productname= ProductAccessory.objects.values_list("ProductName", flat=True).filter(Partnumber__icontains=partnumber).distinct().filter(ProductName=ProductName)
  #   currency = ProductAccessory.objects.values_list("Currency", flat=True).filter(Partnumber__icontains=partnumber).distinct().filter(Currency=Currency)
  # elif category == "AVEng":
  #   productname= ProductAVEng.objects.values_list('ProductName', flat=True).get(Partnumber__icontains=partnumber).distinct().order_by()
  #   currency = ProductAVEng.objects.values_list('Currency', flat=True).get(Partnumber__icontains=partnumber).distinct().order_by()

  q = Product.objects.filter(Partnumber__icontains=partnumber).filter(DateofEntry__range=[fromdate,todate])

  if category == "Hardware":
    q = Product.objects.filter(Partnumber__icontains=partnumber).filter(DateofEntry__range=[fromdate,todate])
  elif category == "Accessory":
    q = ProductAccessory.objects.filter(Partnumber__icontains=partnumber).filter(DateofEntry__range=[fromdate,todate])
  elif category == "AVEng":
    q = ProductAVEng.objects.filter(Partnumber__icontains=partnumber).filter(DateofEntry__range=[fromdate,todate])

  df = read_frame(q)

  data = df.groupby('DateofEntry', as_index=False)[['TotalPrice','Currency']].max()

  print(data)
  
  y=data['TotalPrice']
  x=data['DateofEntry']
  i = data['Currency']
  
  # hover = HoverTool(tooltips=[('Currency', '@Currency')])

  source = ColumnDataSource(dict(x=x,y=y))

  print(x)
  TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
  plot = figure(x_axis_type='datetime',plot_width=1000, y_axis_label = "Total Price",x_axis_label = "Date of Entry", plot_height=600, tools=TOOLS, toolbar_location='below')
  plot.xaxis.formatter=DatetimeTickFormatter(
      hours=["%d %B %Y"],
      days=["%d %B %Y"],
      months=["%d %B %Y"],
      years=["%d %B %Y"],
  )

  labels = LabelSet(x='x', y='y', text='y', level='glyph',
      x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')
  
  plot.line(x, y, line_width=3.0,color="firebrick")
  plot.xaxis.axis_label_text_font_size = "18pt"
  plot.xaxis.major_label_text_font_size = "11pt"
  plot.yaxis.axis_label_text_font_size = "18pt"
  plot.yaxis.major_label_text_font_size = "11pt"
  plot.add_layout(labels)

  hover = plot.select(HoverTool).tooltips = [("Currency", "@Currency"),]


  # df.groupby('TotalPrice').apply(pct_change)
  data['l'] = data.TotalPrice.diff()
  data['j'] = np.where(data['l']>0, 'increase', 'decrease')

  print(data)
  script, div = components(plot, CDN)
  return render(request, "charts/pricechart.html", {"script": script, "div": div,"partnumber":partnumber,"fromdate":fromdate,"todate":todate,"q":q})




  # if category == "Hardware":
  #   weatherdata = \
  #       DataPool(
  #          series=
  #           [{'options': {
  #              'source': Product.objects.filter(Partnumber__icontains=partnumber)},
  #             'terms': [
  #               'DateofEntry',
  #               'TotalPrice']}
  #            ])

  #   #Step 2: Create the Chart object
  #   cht = Chart(
  #           datasource = weatherdata,
  #           series_options =
  #             [{'options':{
  #                 'type': 'line',
  #                 'stacking': False},
  #               'terms':{
  #                 'DateofEntry':[ 
  #                   'TotalPrice']
  #                 }}],
  #           chart_options =
  #             {'title': {
  #                  'text': 'Price Fluctuation Trend'},
  #              'xAxis': {
  #                   'title': {
  #                      'text': 'Date of Entry'}}})

  # elif category == "Accessory":
  #   weatherdata = \
  #       DataPool(
  #          series=
  #           [{'options': {
  #              'source': ProductAccessory.objects.filter(Partnumber__icontains=partnumber)},
  #             'terms': [
  #               'DateofEntry',
  #               'TotalPrice']}
  #            ])

  #   #Step 2: Create the Chart object
  #   cht = Chart(
  #           datasource = weatherdata,
  #           series_options =
  #             [{'options':{
  #                 'type': 'line',
  #                 'stacking': False},
  #               'terms':{
  #                 'DateofEntry':[ 
  #                   'TotalPrice']
  #                 }}],
  #           chart_options =
  #             {'title': {
  #                  'text': 'Price Fluctuation Trend'},
  #              'xAxis': {
  #                   'title': {
  #                      'text': 'Date of Entry'}}})
  
  # elif category == "AVEng":
  #   weatherdata = \
  #       DataPool(
  #          series=
  #           [{'options': {
  #              'source': ProductAVEng.objects.filter(Partnumber__icontains=partnumber)},
  #             'terms': [
  #               'DateofEntry',
  #               'TotalPrice']}
  #            ])

  #   #Step 2: Create the Chart object
  #   cht = Chart(
  #           datasource = weatherdata,
  #           series_options =
  #             [{'options':{
  #                 'type': 'line',
  #                 'stacking': False},
  #               'terms':{
  #                 'DateofEntry':[ 
  #                   'TotalPrice']
  #                 }}],
  #           chart_options =
  #             {'title': {
  #                  'text': 'Price Fluctuation Trend'},
  #              'xAxis': {
  #                   'title': {
  #                      'text': 'Date of Entry'}}})
  # return render(request,'charts/pricechart.html',{'weatherchart': cht})