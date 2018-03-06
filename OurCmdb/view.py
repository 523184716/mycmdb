#coding:utf-8
from django.shortcuts import  render
from UserManage.forms import UserRegister

def base(request):
    userregister = UserRegister()
    # print userregister
    return  render(request,"cmdbweb/Base/base.html",locals())