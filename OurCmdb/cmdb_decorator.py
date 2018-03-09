#coding:utf-8

from django.http import  HttpResponseRedirect
def check_login(fun):
    def wrapper(request,*args,**kwargs):
        c_username = request.COOKIES.get("username")
        s_username = request.session.get("username")
        is_login = request.session.get("is_login")
        if c_username and s_username and is_login and c_username==s_username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("login")
    return wrapper