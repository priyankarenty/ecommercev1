#from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404
# from .tables import ProductTable
from django_tables2 import RequestConfig
from .models import Product




# ----------------------------Product Detail Slug View ----------------------------

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "home/deep/detail.html"


# ----------------------------Product Detail View ----------------------------
class ProductDetailView(DetailView):
#	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist")
		return instance

def product_detail_view(request,pk=None,*args,**kwargs):
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")
		context = {
		'object': instance
		}
	return render(request, "deep/detail.html", context)


# ----------------------------Product Comparison View ----------------------------
class ProductDetailView(DetailView):
#	queryset = Product.objects.all()
	template_name = "products/comparison.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist")
		return instance

def product_detail_view(request,pk=None,*args,**kwargs):
	instance = Product.objects.get_by_id(pk)
	selected_values = request.POST.getlist('qs')
	if instance is None:
		raise Http404("Product doesn't exist")
		context = {
		'object': instance
		}
	return render(request, "deep/detail.html", context)
