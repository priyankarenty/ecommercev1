from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import ProductAVEng

class ProductAVEngResource(resources.ModelResource):
    
    class Meta:
        model = ProductAVEng
        
class ProductAVEngAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['__str__','slug']
	resource_class = ProductAVEngResource

	class Meta:
		model = ProductAVEng

# class AccessoryResource(resources.ModelResource):
    
#     class Meta:
#         model = Accessory

# class AccessoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
# 	list_display = ['__str__','slug']
# 	resource_class = AccessoryResource

# 	class Meta:
# 		model = Accessory
    

admin.site.register(ProductAVEng,ProductAVEngAdmin)
# admin.site.register(Accessory, AccessoryAdmin)



from django.contrib import admin

# Register your models here.
