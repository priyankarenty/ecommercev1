from django.conf import settings
from controlcenter.views import controlcenter
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.urls import reverse_lazy
from django.contrib import admin
from reports.views import test
from ProductAccessory.views import ProductDetailAccessorySlugView
from ProductAVEng.views import ProductAVEngDetailSlugView
from homepage.views import AccessoriesView, HardwareView,AVEngView, get_hardware,get_accessories,get_aveng,get_monitor,get_desktop, get_laptop,get_hardware_oem,get_accessory_oem,get_aveng_oem,get_hardware_var,get_accessory_var,get_aveng_var, get_laptop_arkphire,get_laptop_apple,get_laptop_amti,get_laptop_dell,get_laptop_hp,get_laptop_cdw,get_laptop_hp,get_laptop_lenovo,get_laptop_zones,get_monitor_arkphire,get_monitor_amti,get_monitor_apple,get_monitor_cdw,get_monitor_dell,get_monitor_hp,get_monitor_lenovo,get_monitor_zones, get_desktop_arkphire,get_desktop_amti,get_desktop_apple,get_desktop_cdw, get_desktop_dell, get_desktop_hp,get_desktop_lenovo,get_desktop_zones,get_help_usermanual, get_help_faq, get_help_feedback,get_accessories_audio, get_accessories_power,get_accessories_memory, get_accessories_cable, get_accessories_misc, get_accessories_dock, get_accessories_phone, get_accessories_mouse,get_accessories_pv, get_accessories_graphic, get_accessories_keyboard, get_accessories_camera, get_accessories_sleeve,get_accessories_drive
from products.views import (ProductDetailView,product_detail_view, ProductDetailSlugView)
from .views import home_page,filters
from chartprice.views import weather_chart_view,price_form
from chartstock.views import stock_chart_view,stock_form
# from chartmis.views import mis_chart_view, mis_form,get_data, ChartData
# from chartmis.views import get_data, ChartData, HomeView,mis_form
from chartmis.views import mis_form,mis_chart_view

from catdownload.views import export_hardware_csv,export_accessory_csv,export_accessory_xlsx, export_aveng_csv,export_aveng_xlsx,export_hardware_xlsx
from depreciated.views import eol_form,eol_table
from duplicates.views import duplicates_form,duplicates_table
from leadtime.views import lta_form,lta_table
from pricevariance.views import pv_form,pv_table
from price_approved.views import pa_form,pa_table
from missinginfo.views import mi_form,mi_table
from newproducts.views import npa_form,npa_table

urlpatterns = [
    url(r'^$', home_page),
    url(r'^products/hardware/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),
    url(r'^products/accessory/(?P<slug>[\w-]+)/$',ProductDetailAccessorySlugView.as_view()),
    url(r'^products/aveng/(?P<slug>[\w-]+)/$',ProductAVEngDetailSlugView.as_view()),
    url(r'^products/(?P<pk>\d+)/$', product_detail_view),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include("search.urls", namespace="search")),
    url(r'^filters/$', filters),
    url(r'^people/', include('tutorial.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^admin/dashboard/', controlcenter.urls),
    url(r'^hardware/', get_hardware),
    url(r'^accessories/', get_accessories),
    url(r'^aveng/', get_aveng),
    url(r'^monitor/', get_monitor),
    url(r'^desktop/', get_desktop),
    url(r'^laptop/', get_laptop),
    url(r'^hardware_oem/', get_hardware_oem),
    url(r'^accessory_oem/', get_accessory_oem),
    url(r'^aveng_oem/', get_aveng_oem),
    url(r'^hardware_var/', get_hardware_var),
    url(r'^accessory_var/', get_accessory_var),
    url(r'^aveng_var/', get_aveng_var),
    url(r'^laptop_arkphire/', get_laptop_arkphire),
    url(r'^laptop_amti/', get_laptop_amti),
    url(r'^laptop_apple/', get_laptop_apple),
    url(r'^laptop_cdw/', get_laptop_cdw),
    url(r'^laptop_dell/', get_laptop_dell),
    url(r'^laptop_hp/', get_laptop_hp),
    url(r'^laptop_lenovo/', get_laptop_lenovo),
    url(r'^laptop_zones/', get_laptop_zones),
    url(r'^monitor_arkphire/', get_monitor_arkphire),
    url(r'^monitor_amti/', get_monitor_amti),
    url(r'^monitor_apple/', get_monitor_apple),
    url(r'^monitor_cdw/', get_monitor_cdw),
    url(r'^monitor_dell/', get_monitor_dell),
    url(r'^monitor_hp/', get_monitor_hp),
    url(r'^monitor_lenovo/', get_monitor_lenovo),
    url(r'^monitor_zones/', get_monitor_zones),
    url(r'^desktop_arkphire/', get_desktop_arkphire),
    url(r'^desktop_amti/', get_desktop_amti),
    url(r'^desktop_apple/', get_desktop_apple),
    url(r'^desktop_cdw/', get_desktop_cdw),
    url(r'^desktop_dell/', get_desktop_dell),
    url(r'^desktop_hp/', get_desktop_hp),
    url(r'^desktop_lenovo/', get_desktop_lenovo),
    url(r'^desktop_zones/', get_desktop_zones),
    url(r'^usermanual/', get_help_usermanual),
    url(r'^faq/', get_help_faq),
    url(r'^audio/', get_accessories_audio),
    url(r'^power/', get_accessories_power),
    url(r'^memory/', get_accessories_memory),
    url(r'^cable/', get_accessories_cable),
    url(r'^misc/', get_accessories_misc),
    url(r'^dock/', get_accessories_dock),
    url(r'^phone/', get_accessories_phone),
    url(r'^mouse/', get_accessories_mouse),
    url(r'^privacyfilter/', get_accessories_pv),
    url(r'^graphic/', get_accessories_graphic),
    url(r'^keyboard/', get_accessories_keyboard),
    url(r'^camera/', get_accessories_camera),
    url(r'^sleeve/', get_accessories_sleeve),
    url(r'^drive/', get_accessories_drive),
    url(r'^export_hardware_csv/', export_hardware_csv),
    url(r'^export_hardware_xlsx/', export_hardware_xlsx),
    url(r'^export_accessory_csv/', export_accessory_csv),
    url(r'^export_accessory_xlsx/', export_accessory_xlsx),
    url(r'^export_aveng_csv/', export_aveng_csv),
    url(r'^export_aveng_xlsx/', export_aveng_xlsx),
    url(r'^price/', price_form),
    url(r'^pricechart/$', weather_chart_view),
    url(r'^stock/', stock_form),
    url(r'^stockchart/$', stock_chart_view),
    url(r'^mis/', mis_form),
    url(r'^mischart/$', mis_chart_view, name='mis_chart_view'),
    # url(r'^api/data/$', get_data, name='api-data'),
    # url(r'^api/chart/data/$', ChartData.as_view()),

    # url(r'^price/', price_form),
# REPORTS - EOL
    url(r'^eol_form/$', eol_form),
    url(r'^eol_table/$', eol_table),
    # url(r'^eol_report/$', eol_report),

# REPORTS - DUPLICATES
    url(r'^duplicates_form/$', duplicates_form),
    url(r'^duplicates_table/$', duplicates_table),
    # url(r'^duplicates_report/$', duplicates_report),

# REPORTS - LEADTIME/AVAILABILITY
    url(r'^lta_form/$', lta_form),
    url(r'^lta_table/$', lta_table),

# REPORTS - PRICE VARIANCE
    url(r'^pv_form/$', pv_form),
    url(r'^pv_table/$', pv_table),

# REPORTS - PRICE APPROVED
    url(r'^pa_form/$', pa_form),
    url(r'^pa_table/$', pa_table),

# REPORTS - MISSING INFO
    url(r'^mi_form/$', mi_form),
    url(r'^mi_table/$', mi_table),
# REPORTS - NEW PRODUCTS ADDED
    url(r'^npa_form/$', npa_form),
    url(r'^npa_table/$', npa_table),



    url(r'^compare/', include("compare.urls", namespace="compare_product")),
    # url(r'^catdownload/', include("catdownload.urls", namespace="exports")),
    ]


if settings.DEBUG:
    urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
