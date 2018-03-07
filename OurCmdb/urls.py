"""OurCmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from view import  *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',base,name="base"),
    url(r'^login$',login,name="login"),
    url(r'^phone_check',phone_check,name="phone_check"),
    url(r'^user_check',user_check,name="user_check"),
    url(r'^password_check',password_check,name="password_check"),
    url(r'^email_check',email_check,name='email_check'),
    url(r'^register$',register,name="register")
]
