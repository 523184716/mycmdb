from django.conf.urls import  url
from views import  *

urlpatterns = [
    url(r'^asset',asset,name="asset"),
    url(r'^getasset/(\d+)$',getasset,name="getasset"),
]