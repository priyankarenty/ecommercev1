from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):
    
    class Meta:
        model = Product
        
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['__str__','slug']
	resource_class = ProductResource

	class Meta:
		model = Product


admin.site.register(Product,ProductAdmin)




