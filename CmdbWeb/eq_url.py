from django.conf.urls import  url
from views import  *

urlpatterns = [
    url(r'^asset',asset,name="asset"),
    url(r'^getasset/(\d+)$',getasset,name="getasset"),
    url(r'^authdata/$',servicerlogindata,name="authdata"),
    url(r'^postasset$',postasset,name="postasset"),
    url(r'^addeqip/$',addeqip,name="addeqip")
]