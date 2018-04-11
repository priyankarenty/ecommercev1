from django.conf.urls import url
from . import views

from .views import (
        AccessoriesView, HardwareView, AVEng,
        )

urlpatterns = [
    url(r'^$', AccessoriesView.as_view(), name='query'),
    url(r'^$', HardwareView.as_view(), name='query'),
    url(r'^$', AVEng.as_view(), name='query'),
    # url(r'^$', FilterProductView.as_view(), name='search'),
]
