from django.shortcuts import render, redirect
from django.views.generic import ListView
from products.models import Product
from ProductAccessory.models import ProductAccessory
from ProductAVEng.models import ProductAVEng
from django.db.models import Q
from itertools import chain
import urllib

class SearchProductView(ListView):
    template_name = "search/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        hard = Product.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query) | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query))
        hard_c = Product.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query)  | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query)).count()
        acc = ProductAccessory.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query)  | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query))
        acc_c = ProductAccessory.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query)  | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query)).count()
        av = ProductAVEng.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query) | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query))
        av_c = ProductAVEng.objects.filter(Q(Specifications__icontains=query) | Q(ProductName__icontains=query) | Q(Country__icontains=query) | Q(TotalPrice__icontains=query) | Q(Partnumber__icontains=query)  | Q(ProductName__icontains=query) | Q(ProductCategory__icontains=query) | Q(Supplier__icontains=query)).count()
      
        results = chain(hard,acc,av)
        if query is not None:
            return results
        return Product.objects.none()


