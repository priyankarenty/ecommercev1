from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import ProductAccessory

class ProductAccessoryResource(resources.ModelResource):
    
    class Meta:
        model = ProductAccessory
        
class ProductAccessoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['__str__','slug']
	resource_class = ProductAccessoryResource

	class Meta:
		model = ProductAccessory

    

admin.site.register(ProductAccessory,ProductAccessoryAdmin)

 
