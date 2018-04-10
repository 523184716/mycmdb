from django.conf.urls import  url
from views import  *

urlpatterns = [
    url(r'^asset',asset,name="asset"),
    url(r'^getasset/(\d+)$',getasset,name="getasset"),
    url(r'^authdata/$',servicerlogindata,name="authdata"),
    url(r'^postasset$',postasset,name="postasset"),
    url(r'^addeqip/$',addeqip,name="addeqip"),
    url(r'^terminal/(\d+)$',terminal,name="terminal"),
    url(r'^get_auth_obj/$',get_auth_obj,name="get_auth_obj")
]