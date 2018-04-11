from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ProductFilter
from django.db.models import Q,F,Count, Max
from itertools import chain

import datetime


#----------------------- Hardware ----------------------------------------------
class HardwareView(ListView):

    template_name = "home/hardware.html"

    def get_queryset(self, *args, **kwargs):
    	request = self.request
    	return Product.objects.all()
    
def get_hardware(request):
    
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    
    category = "Hardware"
    # product_count = Product.objects.filter(ProductCategory__icontains="hardware").filter(DateofEntry=obj.DateofEntry).filter(PriceChange__isnull=False).count()
    return render(request,"home/hardware.html",{'table': table, 'category':category})


#----------------------- Hardware/Monitor ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor(request):

    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Monitor")
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Monitor")
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Monitor")
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Monitor")
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="Monitor")
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Monitor")
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="Monitor")
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="Monitor")
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Monitor")
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Monitor")
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="Monitor")
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="Monitor")
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="Monitor")
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    
    category = "Hardware"
    ProductType = "Monitor"
    product_count = Product.objects.filter(ProductType__icontains="monitor").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/hardware_2.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType})

#----------------------- Hardware/Desktop ----------------------------------------------
class DesktopView(ListView):

    template_name = "home/hardware/desktop.html"
    
def get_desktop(request):
    table = Product.objects.filter(ProductType__icontains="desktop")
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="desktop")
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="desktop")
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="desktop")
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="desktop")
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="desktop")
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="desktop")
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="desktop")
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="desktop")
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="desktop")
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="desktop")
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="desktop")
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="desktop")
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="desktop")
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)

    category = "Hardware"
    ProductType = "Desktop"
    # product_count = Product.objects.filter(ProductType__icontains="desktop").count()
    # table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/hardware_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType})

#----------------------- Hardware/Laptop ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop(request):
    
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Laptop")
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Laptop")
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Laptop")
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Laptop")
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="Laptop")
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Laptop")
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="Laptop")
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="Laptop")
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Laptop")
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Laptop")
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="Laptop")
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="Laptop")
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="Laptop")
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    category = "Hardware"
    ProductType = "Laptop"
    # product_count = Product.objects.filter(ProductType__icontains="Laptop").count()
    # table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/hardware_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType})


#----------------------- Accessories ---------------------------------------------
class AccessoriesView(ListView):

    template_name = "home/accessories.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_accessories(request):
    # table = ProductAccessory.objects.filter(ProductCategory__icontains="accessory")
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    category = "Accessory"
    product_count = ProductAccessory.objects.filter(ProductCategory__icontains="accessory").count()
    return render(request,"home/accessories.html",{'table': table, 'product_count': product_count, 'category':category})


#----------------------- AV Eng ----------------------------------------------
class AVEngView(ListView):

    template_name = "home/aveng.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_aveng(request):
    table = ProductAVEng.objects.filter(ProductCategory__icontains="AVEng")
    x1 = ProductAVEng.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAVEng.objects.none()
    x2 = ProductAVEng.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAVEng.objects.none()
    
    x3 = ProductAVEng.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAVEng.objects.none()
    
    x4 = ProductAVEng.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAVEng.objects.none()
    
    x5 = ProductAVEng.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAVEng.objects.none()
    
    x6 = ProductAVEng.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAVEng.objects.none()
    
    x7 = ProductAVEng.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAVEng.objects.none()

    x8 = ProductAVEng.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAVEng.objects.none()
    
    x9 = ProductAVEng.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAVEng.objects.none()
    x10 = ProductAVEng.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAVEng.objects.none()
    x11 = ProductAVEng.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAVEng.objects.none()
    x12 = ProductAVEng.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAVEng.objects.none()
    x13 = ProductAVEng.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAVEng.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    
    
    category = "AV Eng"
    product_count = ProductAVEng.objects.filter(ProductCategory__icontains="AVEng").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/aveng.html",{'table': table, 'product_count': product_count, 'category':category})


#----------------------- Supplier/Hardware/OEM ----------------------------------------------
class HardwareOEMView(ListView):

    template_name = "home/supplier.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_hardware_oem(request):
    table = Product.objects.filter(SupplierType__icontains="oem")

    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values().filter(SupplierType__icontains="oem")
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="oem")
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="oem")
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti").filter(SupplierType__icontains="oem")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="oem")
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="oem")
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="oem")
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="oem")
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="oem")
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="oem")
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="oem")
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="oem")
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="oem")
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="oem")
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="oem")
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    
    suppliertype = "OEM"
    producttype = "Hardware"
    product_count = Product.objects.filter(SupplierType__icontains="oem").count()
    # table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/supplier_h.html",{'table': table, 'product_count': product_count,'producttype':producttype, 'suppliertype':suppliertype})


#----------------------- Supplier/Accessory/OEM ----------------------------------------------
class AccessoryOEMView(ListView):

    template_name = "home/supplier.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return ProductAccessory.objects.all()
    
def get_accessory_oem(request):
    table = ProductAccessory.objects.filter(SupplierType__icontains="oem")
    suppliertype = "OEM"
    producttype = "Accessory"
    product_count = ProductAccessory.objects.filter(SupplierType__icontains="oem").count()
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values().filter(SupplierType__icontains="oem")
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(SupplierType__icontains="oem").filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="oem")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="oem").filter(SupplierType__icontains="oem")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="oem")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="oem")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="oem")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Dell").filter(SupplierType__icontains="oem").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="oem")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="oem")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="oem")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="oem")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="oem")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="oem")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="oem")
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="oem")
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="oem")
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    # table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/supplier_aa.html",{'table': table, 'product_count': product_count,'producttype':producttype, 'suppliertype':suppliertype})

#----------------------- Supplier/AVEng/OEM ----------------------------------------------
class AVEngOEMView(ListView):

    template_name = "home/supplier.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return ProductAVEng.objects.all()
    
def get_aveng_oem(request):
    table = ProductAVEng.objects.filter(SupplierType__icontains="oem")
    if x1:
        arkphiredate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="oem")
    else:
        arkphire =ProductAVEng.objects.none()
    x2 = ProductAVEng.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="oem")
    else:
        apple =ProductAVEng.objects.none()
    
    x3 = ProductAVEng.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="oem")
    else:
        amti =ProductAVEng.objects.none()
    
    x4 = ProductAVEng.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="oem")
    else:
        cdw=ProductAVEng.objects.none()
    
    x5 = ProductAVEng.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="oem")
    else:
        dyhl=ProductAVEng.objects.none()
    
    x6 = ProductAVEng.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="oem")
    else:
        dell=ProductAVEng.objects.none()
    
    x7 = ProductAVEng.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="oem")
    else:
        gadget=ProductAVEng.objects.none()

    x8 = ProductAVEng.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="oem")
    else:
        gownet=ProductAVEng.objects.none()
    
    x9 = ProductAVEng.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="oem")
    else:
        hp=ProductAVEng.objects.none()
    x10 = ProductAVEng.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="oem")
    else:
        lenovo=ProductAVEng.objects.none()
    x11 = ProductAVEng.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="oem")
    else:
        zones=ProductAVEng.objects.none()
    x12 = ProductAVEng.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAVEng.objects.filter(SupplierType__icontains="oem").filter(PriceChange__isnull=False).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="oem")
    else:
        moredirect=ProductAVEng.objects.none()
    x13 = ProductAVEng.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="oem")
    else:
        workplace=ProductAVEng.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    
    suppliertype = "OEM"
    producttype = "AV Eng"
    product_count = Product.objects.filter(SupplierType__icontains="oem").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    return render(request,"home/supplier_aa.html",{'table': table, 'product_count': product_count,'producttype':producttype, 'suppliertype':suppliertype})



#----------------------- Supplier/Hardware/VAR ----------------------------------------------
class HardwareVarView(ListView):

    template_name = "home/supplier/var.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_hardware_var(request):
    table = Product.objects.filter(SupplierType__icontains="var")

    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="var")
    else:
        arkphire =Product.objects.none()
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="var")
    else:
        apple =Product.objects.none()
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="var")
    else:
        amti =Product.objects.none()
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="var")
    else:
        cdw=Product.objects.none()
    
    x5 = Product.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dyhl = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="var")
    else:
        dyhl=Product.objects.none()
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="var")
    else:
        dell=Product.objects.none()
    
    x7 = Product.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gadget = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="var")
    else:
        gadget=Product.objects.none()

    x8 = Product.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gownet = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="var")
    else:
        gownet=Product.objects.none()
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="var")
    else:
        hp=Product.objects.none()
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="var")
    else:
        lenovo=Product.objects.none()
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="var")
    else:
        zones=Product.objects.none()
    x12 = Product.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        moredirect = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="var")
    else:
        moredirect=Product.objects.none()
    x13 = Product.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        workplace = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="var")
    else:
        workplace=Product.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    

    producttype = "Hardware"
    suppliertype = "VAR"
    product_count = Product.objects.filter(SupplierType__icontains="var").count()
    return render(request,"home/supplier_h.html",{'table': table, 'product_count': product_count, 'producttype': producttype,'suppliertype':suppliertype})


#----------------------- Supplier/Accessory/VAR ----------------------------------------------
class AccessoryVarView(ListView):

    template_name = "home/supplier/var.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return ProductAccessory.objects.all()
    
def get_accessory_var(request):
    table = ProductAccessory.objects.filter(SupplierType__icontains="var")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="var")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="var")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="var")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="var")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="var")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="var")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="var")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="var")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="var")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="var")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="var")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="var")
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="var")
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)
    




    producttype = "Accessory"
    suppliertype = "VAR"
    product_count = ProductAccessory.objects.filter(SupplierType__icontains="var").count()
    return render(request,"home/supplier_aa.html",{'table': table, 'product_count': product_count, 'producttype': producttype,'suppliertype':suppliertype})


#----------------------- Supplier/AVEng/VAR ----------------------------------------------
class AVEngVarView(ListView):

    template_name = "home/supplier/var.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return ProductAVEng.objects.all()
    
def get_aveng_var(request):
    table = ProductAVEng.objects.filter(SupplierType__icontains="var")
    
    x1 = ProductAVEng.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        arkphire = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(SupplierType__icontains="var")
    else:
        arkphire =ProductAVEng.objects.none()
    x2 = ProductAVEng.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        apple = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(SupplierType__icontains="var")
    else:
        apple =ProductAVEng.objects.none()
    
    x3 = ProductAVEng.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        amti = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(SupplierType__icontains="var")
    else:
        amti =ProductAVEng.objects.none()
    
    x4 = ProductAVEng.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        cdw = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(SupplierType__icontains="var")
    else:
        cdw=ProductAVEng.objects.none()
    
    x5 = ProductAVEng.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dyhl = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(SupplierType__icontains="var")
    else:
        dyhl=ProductAVEng.objects.none()
    
    x6 = ProductAVEng.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        dell = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(SupplierType__icontains="var")
    else:
        dell=ProductAVEng.objects.none()
    
    x7 = ProductAVEng.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gadget = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(SupplierType__icontains="var")
    else:
        gadget=ProductAVEng.objects.none()

    x8 = ProductAVEng.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        gownet = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(SupplierType__icontains="var")
    else:
        gownet=ProductAVEng.objects.none()
    
    x9 = ProductAVEng.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        hp = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(SupplierType__icontains="var")
    else:
        hp=ProductAVEng.objects.none()
    x10 = ProductAVEng.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        lenovo = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(SupplierType__icontains="var")
    else:
        lenovo=ProductAVEng.objects.none()
    x11 = ProductAVEng.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        zones = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(SupplierType__icontains="var")
    else:
        zones=ProductAVEng.objects.none()
    x12 = ProductAVEng.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        moredirect = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(SupplierType__icontains="var")
    else:
        moredirect=ProductAVEng.objects.none()
    x13 = ProductAVEng.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(SupplierType__icontains="var")
        workplace = ProductAVEng.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(SupplierType__icontains="var")
    else:
        workplace=ProductAVEng.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones)

    producttype = "AV Eng"
    suppliertype = "VAR"
    product_count = ProductAVEng.objects.filter(SupplierType__icontains="var").count()
    return render(request,"home/supplier_aa.html",{'table': table, 'product_count': product_count, 'producttype': producttype,'suppliertype':suppliertype})


#----------------------- Hardware/Laptop/Arkphire ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_arkphire.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_arkphire(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="Arkphire")
    
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop")
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Laptop")
    else:
        arkphire =Product.objects.none()
    
    table = arkphire
    
    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="Arkphire").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "Arkphire"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Laptop/AMTI ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_amti.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_amti(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="AMTI")
    
  
    x1 = Product.objects.filter(Supplier__icontains="AMTI").values()
    if x1:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop")
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Laptop")
    else:
        amti =Product.objects.none()
    
    table = amti
    
    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="AMTI").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "AMTI"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Laptop/Apple ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_apple.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_apple(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="Apple")
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="Apple")
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="Apple")
    else:
        apple =Product.objects.none()
    
    
    table = apple
    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="apple").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "Apple"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



#----------------------- Hardware/Laptop/CDW ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_cdw.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_cdw(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="cdw")
    
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="cdw")
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="cdw")
    else:
        cdw=Product.objects.none()
 
    table = cdw

    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="cdw").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "CDW"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Laptop/Dell ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_dell.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_dell(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="dell")
    
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="dell")
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="dell")
    else:
        dell=Product.objects.none()
  
    table = dell

    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="dell").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "Dell"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



#----------------------- Hardware/Laptop/HP ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_hp.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_hp(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="hp")
  
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="hp")
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="hp")
    else:
        hp=Product.objects.none()
    
    
    table = hp
    
    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="hp").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "HP"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})




#----------------------- Hardware/Laptop/Lenovo ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_lenovo.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_lenovo(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="lenovo")
    
    
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="lenovo")
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="lenovo")
    else:
        lenovo=Product.objects.none()
    
    table = lenovo

    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="lenovo").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "Lenovo"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Laptop/Zones ----------------------------------------------
class LaptopView(ListView):

    template_name = "home/hardware/laptop/laptop_zones.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_laptop_zones(request):
    table = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="zones")   
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="zones")
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="Laptop").filter(Supplier__icontains="zones")
    else:
        zones=Product.objects.none()
    table = zones
    product_count = Product.objects.filter(ProductType__icontains="Laptop").filter(Supplier__icontains="zones").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Laptop"
    supplier = "Zones"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



#----------------------- Hardware/Monitor/Arkphire ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_arkphire.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_arkphire(request):
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Arkphire")
    
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Arkphire")
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Arkphire")
    else:
        arkphire =Product.objects.none()
    
    table = arkphire
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Arkphire").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "Arkphire"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Monitor/AMTI ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_amti.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_amti(request):
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="amti")
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="amti")
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="amti")
    else:
        amti =Product.objects.none()
    table = amti
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="amti").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "AMTI"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

#----------------------- Hardware/Monitor/Apple ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_apple.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_apple(request):
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Apple")
 
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Apple")
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Apple")
    else:
        apple =Product.objects.none()
 
    table = apple
    
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="Apple").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "Apple"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


#----------------------- Hardware/Monitor/CDW ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_cdw.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_cdw(request):
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="cdw")
    
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="cdw")
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="cdw")
    else:
        cdw=Product.objects.none()
    table = cdw
    
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="cdw").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "CDW"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


#----------------------- Hardware/Monitor/DELL ----------------------------------------------
class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_dell.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_dell(request):
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="dell")
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="dell")
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="dell")
    else:
        dell=Product.objects.none()
    
    table = dell
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="dell").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "Dell"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


#----------------------- Hardware/Monitor/HP ----------------------------------------------

class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_hp.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_hp(request):

    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="hp")
 
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="hp")
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="hp")
    else:
        hp=Product.objects.none()
    
    table = hp

    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="hp").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "HP"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


# ----------------------- Hardware/Monitor/Lenovo ----------------------------------------------

class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_lenovo.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_lenovo(request):
    
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="lenovo")
    
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="lenovo")
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Monitor").filter(Supplier__icontains="lenovo")
    else:
        lenovo=Product.objects.none()
    
    
    table = lenovo
    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="lenovo").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "Lenovo"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



# ----------------------- Hardware/Monitor/Zones ----------------------------------------------

class MonitorView(ListView):

    template_name = "home/hardware/monitor/monitor_zones.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_monitor_zones(request):
    
    table = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="zones")
    
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=Product.objects.none()
    
    table = zones
    


    product_count = Product.objects.filter(ProductType__icontains="Monitor").filter(Supplier__icontains="zones").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Monitor"
    supplier = "Zones"
    return render(request,"home/hardware_2_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

# ----------------------- Hardware/Desktop/Arkphire ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_arkphire.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_arkphire(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Arkphire")
    x1 = Product.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Arkphire")
        arkphire = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Arkphire")
    else:
        arkphire =Product.objects.none()
    
    
    table = arkphire
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Arkphire").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "Arkphire"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

# ----------------------- Hardware/Desktop/Apple ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_apple.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_apple(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Apple")
    
    x2 = Product.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Apple")
        apple = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Apple")
    else:
        apple =Product.objects.none()
    
    
    
    table = apple
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="Apple").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "Apple"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



# ----------------------- Hardware/Desktop/AMTI ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_amti.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_amti(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="amti")
    
    
    x3 = Product.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="amti")
        amti = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="amti")
    else:
        amti =Product.objects.none()
    
    table = amti
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="amti").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "AMTI"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


# ----------------------- Hardware/Desktop/CDW ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_cdw.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_cdw(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="cdw")
    
    x4 = Product.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="cdw")
        cdw = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="cdw")
    else:
        cdw=Product.objects.none()

    table = cdw

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="cdw").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "CDW"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


# ----------------------- Hardware/Desktop/Dell ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_dell.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_dell(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="dell")
    
    x6 = Product.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="dell")
        dell = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="dell")
    else:
        dell=Product.objects.none()
    
    
    table = dell
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="dell").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "Dell"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})


# ----------------------- Hardware/Desktop/HP----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_hp.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_hp(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="hp")
    
    
    x9 = Product.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="hp")
        hp = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="hp")
    else:
        hp=Product.objects.none()
    
    table = hp
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="hp").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "HP"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

# ----------------------- Hardware/Desktop/Zones ----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_zones.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_zones(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="zones")
    
    x11 = Product.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="zones")
        zones = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="zones")
    else:
        zones=Product.objects.none()
    
    table = zones
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="zones").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "Zones"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})

# ----------------------- Hardware/Desktop/Lenovo----------------------------------------------

class DesktopView(ListView):

    template_name = "home/hardware/desktop/desktop_lenovo.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def get_desktop_lenovo(request):
    
    table = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="lenovo")
    x10 = Product.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="lenovo")
        lenovo = Product.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Desktop").filter(Supplier__icontains="lenovo")
    else:
        lenovo=Product.objects.none()
    table = lenovo
    

    product_count = Product.objects.filter(ProductType__icontains="Desktop").filter(Supplier__icontains="lenovo").count()
    table_filter = ProductFilter(request.GET, queryset=table)
    category = "Hardware"
    ProductType = "Desktop"
    supplier = "Lenovo"
    return render(request,"home/hardware_1_1.html",{'table': table, 'product_count': product_count,'category':category,'ProductType':ProductType,'supplier':supplier})



# ----------------------- Help/User Manual ----------------------------------------------
    
def get_help_usermanual(request):
    return render(request,"home/help/usermanual.html")


# ----------------------- Help/FAQ ----------------------------------------------
    
def get_help_faq(request):
    return render(request,"home/help/faq.html")

# ----------------------- Help/Feedback ----------------------------------------------
    
def get_help_feedback(request):
    return render(request,"home/help/feedback.html")

# ----------------------- Accessories/Audio ----------------------------------------------
    
def get_accessories_audio(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="Audio")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="Audio")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="Audio")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="Audio")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="Audio")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="Audio")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="Audio")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="Audio")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="Audio")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="Audio")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="Audio")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="Audio")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="Audio")
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="Audio")
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="Audio")
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    category = "Accessory"
    ProductType = "Audio"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Audio").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})

# ----------------------- Accessories/Misc ----------------------------------------------
    
def get_accessories_misc(request):
    table = ProductAccessory.objects.filter(ProductType__icontains="audio")
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="audio")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="audio")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="audio")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="audio")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="audio")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="audio")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="audio")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="audio")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="audio")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="audio")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="audio")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="audio")
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="audio")
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="audio")
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 

    category = "Accessory"
    ProductType = "Miscellaneous"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Audio").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})

# ----------------------- Accessories/Power ----------------------------------------------
    
def get_accessories_power(request):
    table = ProductAccessory.objects.filter(ProductType__icontains="power")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="power")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="power")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="power")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="power")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="power")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="power")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="power")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power").filter(ProductType__icontains="power")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="power")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="power")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="power")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="power")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate).filter(ProductType__icontains="power")
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="power")
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate).filter(ProductType__icontains="power")
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 

    category = "Accessory"
    ProductType = "Power"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Power").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})

# ----------------------- Accessories/Memory ----------------------------------------------
    
def get_accessories_memory(request):
    table = ProductAccessory.objects.filter(ProductType__icontains="memory")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate).filter(ProductType__icontains="memory")
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate).filter(ProductType__icontains="memory")
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate).filter(ProductType__icontains="memory")
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate).filter(ProductType__icontains="memory")
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate).filter(ProductType__icontains="memory")
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate).filter(ProductType__icontains="memory")
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate).filter(ProductType__icontains="memory")
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate).filter(ProductType__icontains="memory")
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate).filter(ProductType__icontains="memory")
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate).filter(ProductType__icontains="memory")
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry.filter(ProductType__icontains="memory")
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate).filter(ProductType__icontains="memory")
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    category = "Accessory"
    ProductType = "Memory"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Memory").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})


# ----------------------- Accessories/Cable ----------------------------------------------
    
def get_accessories_cable(request):
    table = ProductAccessory.objects.filter(ProductType__icontains="cable")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 

    category = "Accessory"
    ProductType = "Cable"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Cable").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})


# ----------------------- Accessories/Dock ----------------------------------------------
    
def get_accessories_dock(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="dock")
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 


    category = "Accessory"
    ProductType = "Dock"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="dock").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})



# ----------------------- Accessories/Phone ----------------------------------------------
    
def get_accessories_phone(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="phone")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 

    category = "Accessory"
    ProductType = "Phone"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="phone").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})




# ----------------------- Accessories/Mouse----------------------------------------------
    
def get_accessories_mouse(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="mouse")

    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 


    category = "Accessory"
    ProductType = "Mouse"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Mouse").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})




# ----------------------- Accessories/Privacy Fitler----------------------------------------------
    
def get_accessories_pv(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="PrivacyFilter")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 


    category = "Accessory"
    ProductType = "Privacy Filter"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="PrivacyFilter").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})



# ----------------------- Accessories/Graphic----------------------------------------------
    
def get_accessories_graphic(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="graphic")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 




    category = "Accessory"
    ProductType = "Graphic"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Graphic").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})




# ----------------------- Accessories/keyboard----------------------------------------------
    
def get_accessories_keyboard(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="keyboard")
    
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 



    category = "Accessory"
    ProductType = "Keyboard"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="keyboard").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})


# ----------------------- Accessories/Camera----------------------------------------------
    
def get_accessories_camera(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="camera")
   

    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 


    category = "Accessory"
    ProductType = "Camera"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Camera").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})



# ----------------------- Accessories/sleeve----------------------------------------------
    
def get_accessories_sleeve(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="sleeve")
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 

    category = "Accessory"
    ProductType = "Sleeve"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="sleeve").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})



# ----------------------- Accessories/drive----------------------------------------------
    
def get_accessories_drive(request):
    
    table = ProductAccessory.objects.filter(ProductType__icontains="drive")
    x1 = ProductAccessory.objects.filter(Supplier__icontains="Arkphire").values()
    if x1:
        arkphiredate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").latest("DateofEntry").DateofEntry
        arkphire = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Arkphire").filter(DateofEntry=arkphiredate) 
    else:
        arkphire =ProductAccessory.objects.none()
    x2 = ProductAccessory.objects.values().filter(Supplier__icontains="Apple")
    if x2:
        appledate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").latest("DateofEntry").DateofEntry
        apple = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Apple").filter(DateofEntry=appledate)
    else:
        apple =ProductAccessory.objects.none()
    
    x3 = ProductAccessory.objects.values().filter(Supplier__icontains="amti")
    if x3:
        amtidate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").latest("DateofEntry").DateofEntry
        amti = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="AMTI").filter(DateofEntry=amtidate)
    else:
        amti =ProductAccessory.objects.none()
    
    x4 = ProductAccessory.objects.values().filter(Supplier__icontains="cdw")
    if x4:
        cdwdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").latest("DateofEntry").DateofEntry
        cdw = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="CDW").filter(DateofEntry=cdwdate)
    else:
        cdw=ProductAccessory.objects.none()
    
    x5 = ProductAccessory.objects.values().filter(Supplier__icontains="dyhl")
    if x5:
        dyhldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").latest("DateofEntry").DateofEntry
        dyhl = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="dyhl").filter(DateofEntry=dyhldate)
    else:
        dyhl=ProductAccessory.objects.none()
    
    x6 = ProductAccessory.objects.values().filter(Supplier__icontains="dell")
    if x6:
        delldate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").latest("DateofEntry").DateofEntry
        dell = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Dell").filter(DateofEntry=delldate)
    else:
        dell=ProductAccessory.objects.none()
    
    x7 = ProductAccessory.objects.values().filter(Supplier__icontains="gadget")
    if x7:
        gadgetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").latest("DateofEntry").DateofEntry
        gadget = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gadget").filter(DateofEntry=gadgetdate)
    else:
        gadget=ProductAccessory.objects.none()

    x8 = ProductAccessory.objects.values().filter(Supplier__icontains="gownet")
    if x8:
        gownetdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").latest("DateofEntry").DateofEntry
        gownet = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="gownet").filter(DateofEntry=gownetdate)
    else:
        gownet=ProductAccessory.objects.none()
    
    x9 = ProductAccessory.objects.values().filter(Supplier__icontains="hp")
    if x9:
        hpdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").latest("DateofEntry").DateofEntry
        hp = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="HP").filter(DateofEntry=hpdate)
    else:
        hp=ProductAccessory.objects.none()
    x10 = ProductAccessory.objects.values().filter(Supplier__icontains="Lenovo")
    if x10:
        lenovodate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").latest("DateofEntry").DateofEntry
        lenovo = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Lenovo").filter(DateofEntry=lenovodate)
    else:
        lenovo=ProductAccessory.objects.none()
    x11 = ProductAccessory.objects.values().filter(Supplier__icontains="Zones")
    if x11:
        zonesdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").latest("DateofEntry").DateofEntry
        zones = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="Zones").filter(DateofEntry=zonesdate)
    else:
        zones=ProductAccessory.objects.none()
    x12 = ProductAccessory.objects.values().filter(Supplier__icontains="moredirect")
    if x12:
        moredirectdate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").latest("DateofEntry").DateofEntry
        moredirect = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="moredirect").filter(DateofEntry=moredirectdate)
    else:
        moredirect=ProductAccessory.objects.none()
    x13 = ProductAccessory.objects.values().filter(Supplier__icontains="workplace")
    if x13:
        workplacedate = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").latest("DateofEntry").DateofEntry
        workplace = ProductAccessory.objects.filter(PriceChange__isnull=False).filter(Q(PriceApproved=False)|Q(PriceApproved__isnull=True)).filter(Supplier__icontains="workplace").filter(DateofEntry=workplacedate)
    else:
        workplace=ProductAccessory.objects.none()
    
    table = chain(arkphire,apple,amti,cdw,dell,dyhl,gadget,gownet,hp,lenovo,moredirect,workplace,zones) 
    category = "Accessory"
    ProductType = "Drive"
    product_count = ProductAccessory.objects.filter(ProductType__icontains="Drive").count()
    return render(request,"home/a_sub.html",{'table': table, 'product_count': product_count, "category":category, 'ProductType':ProductType})