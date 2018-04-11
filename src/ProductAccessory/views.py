#from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404
# from .tables import ProductTable
from django_tables2 import RequestConfig
from .models import ProductAccessory



class ProductDetailAccessorySlugView(DetailView):
	queryset = ProductAccessory.objects.all()
	template_name = "home/deep/detail_ac.html"

	

# ----------------------------Product Detail View ----------------------------
class ProductAccessoryDetailView(DetailView):

	template_name = "products/detail_ac.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductAccessoryDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = ProductAccessory.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist")
		return instance

def product_accessory_detail_view(request,pk=None,*args,**kwargs):
	instance = ProductAccessory.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")
		context = {
		'object': instance
		}
	return render(request, "deep/detail_ac.html", context)


# ----------------------------Product Comparison View ----------------------------
class ProductAccessoryDetailView(DetailView):

	template_name = "products/comparison.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = ProductAccessory.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesn't exist")
		return instance

def product_detail_view(request,pk=None,*args,**kwargs):
	instance = ProductAccessory.objects.get_by_id(pk)
	selected_values = request.POST.getlist('qs')
	if instance is None:
		raise Http404("Product doesn't exist")
		context = {
		'object': instance
		}
	return render(request, "deep/detail_ac.html", context)
