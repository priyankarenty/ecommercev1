from django.conf.urls import url

from .views import (
	# compare_update,
	compare_home, compare_home_accessory, compare_home_aveng,)


urlpatterns = [
				url(r'^hardware/$', compare_home, name='home'),
				url(r'^accessory/$', compare_home_accessory, name='accessory'),
				url(r'^aveng/$', compare_home_aveng, name='aveng'),
				
# url(r'^compare/$', compare_update, name='update'),
]
