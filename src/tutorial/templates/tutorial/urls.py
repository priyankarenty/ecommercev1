from django.conf.urls import url
from django.contrib import admin

from tutorial.views import people

urlpatterns = [
    
    url(r'^$', people.asView())
]