from django.shortcuts import render
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.db.models import Q,Avg
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import numpy as np
import datetime
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource,WheelZoomTool, PanTool, BoxZoomTool, ResetTool, TapTool,  HoverTool,LabelSet,DatetimeTickFormatter,SingleIntervalTicker






def mis_form(request):
  return render(request,'charts/mischart/mis.html')

def mis_chart_view(request):
    supplier = request.POST.get('supplier')
    region = request.POST.get('region')
    category = request.POST.get('category')
    fromdate = request.POST.get('fromdate')
    todate = request.POST.get('todate')


    q = Product.objects.filter(Region=region).filter(Supplier=supplier).filter(DateofEntry__range=[fromdate,todate])
    data = read_frame(q)
    if category == "Hardware":
      q = Product.objects.filter(Region=region).filter(Supplier=supplier).filter(DateofEntry__range=[fromdate,todate])
        
    elif category == "Accessory":
      q = ProductAccessory.objects.filter(Region=region).filter(Supplier=supplier).filter(DateofEntry__range=[fromdate,todate])
    
    elif category == "AVEng":
      q = ProductAVEng.objects.filter(Region=region).filter(Supplier=supplier).filter(DateofEntry__range=[fromdate,todate])
      

    qs2 = read_frame(q)

    source = ColumnDataSource(data=data)
    qs2['MissingInfo'] = qs2.apply(lambda x: x.isnull().sum(), axis='columns')
    
    qs2['Total'] = qs2.apply(lambda x: x.count(), axis='columns')
    qs2['CompleteData'] = qs2['Total'] - qs2['MissingInfo']



    table = qs2.groupby('DateofEntry', as_index=False)[['CompleteData']].sum()
    table1 = qs2.groupby('DateofEntry', as_index=False)[['Total']].sum()
    table = pd.merge(table,table1, left_index=True, right_index=True)
    table['CompleteData%'] = ((table.CompleteData/table.Total) * 100).round(1)
    table = table.drop(['DateofEntry_y','Total'], axis=1)
    
    x = {"DateofEntry_x": "DateofEntry"}
    table= table.rename(columns=x)
    
    table = table[['CompleteData','DateofEntry','CompleteData%']]
    cols = table.columns.tolist()
    print(table)
    displaytable1= table.drop('CompleteData%', 1)
    displaytable = displaytable1.to_html()
    print(displaytable1)
    
    data = table.to_dict(orient='list')
    table['CompleteData%'] = table['CompleteData%'].astype(str)

    y=table['CompleteData%']
    z=table['DateofEntry']
    hover = HoverTool(tooltips=[('Album_name', '@album_name')])

    source = ColumnDataSource(dict(x=z,y=y))
    print(z)

    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
    plot = figure(x_axis_type='datetime',y_range=(0, 100),plot_width=1000, y_axis_label = "Completion %",x_axis_label = "Date of Entry", tools=TOOLS)
    plot.yaxis.ticker = SingleIntervalTicker(interval=10, num_minor_ticks=10)
    plot.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
    labels = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-13.5, y_offset=0, text_font_size='13pt',source=source, render_mode='canvas')
    # plot.vbar(source=source, x='x', top='y',bottom=0,width=3.0,color="firebrick")
    plot.line(z, y, line_width=3.0,color="firebrick")
    plot.xaxis.axis_label_text_font_size = "18pt"
    plot.xaxis.major_label_text_font_size = "11pt"
    plot.yaxis.axis_label_text_font_size = "18pt"
    plot.yaxis.major_label_text_font_size = "11pt"
    plot.add_layout(labels)

    tickers = pd.to_datetime(table.index.values).astype(int) / 10**6
   
    script, div = components(plot, CDN)
    return render(request, "charts/mischart/mischart.html", {"script": script, "div": div,"supplier":supplier,"region":region,"category":category,"fromdate":fromdate,"todate":todate,"q":q})
 