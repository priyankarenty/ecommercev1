from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
#from csvTool import handle_uploaded_file
from .forms import UploadFileForm
from products.models import Product
from .filters import ProductFilter
from django.http import JsonResponse
from django.views.generic import View
from controlcenter import Dashboard, widgets
from rest_framework.views import APIView
from rest_framework.response import Response


def home_page(request):
	context = {
"title" : "Home Page"
}
	return render(request,"home/home_page.html", context)


def filters(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'filters/product_list.html', {'filter': product_filter})
