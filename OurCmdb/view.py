#coding:utf-8
from django.shortcuts import  render,render_to_response
from UserManage.forms import UserRegister
from UserManage.registercheck import *
from django.core.exceptions import ValidationError
from django.http import JsonResponse
def base(request):
    userregister = UserRegister()
    # print userregister
    return  render(request,"cmdbweb/Base/base.html",locals())

def login(request):
    return  render_to_response("cmdbweb/login.html")

#校验手机号码，根据校验函数的返回值来判断
def phone_check(request):
    res = {"state":"error","data":""}
    if request.method == "GET":
        phone = request.GET["phone"]
        result = valid_phone(phone)
        if phone == result:
            res["state"]="success"
        else:
            res["data"]=result
    else:
        res["data"]="requst method must be get!"
    return JsonResponse(res)

#校验用户名
def user_check(request):
    res = {"state":"error","data":""}
    if request.method == "GET":
        user = request.GET["user"]
        result = valid_user(user)
        if user == result:
            res["state"]="success"
        else:
            res["data"]=result
    else:
        res["data"]="requst method must be get!"
    return JsonResponse(res)

#校验密码
def password_check(request):
    res = {"state": "error", "data": ""}
    if request.method == "GET":
        password = request.GET["password"]
        confirm_password = request.GET["confirm_password"]
        result = valid_password(password,confirm_password)
        if password == result:
            res["state"] = "success"
        else:
            res["data"] = result
    else:
        res["data"] = "requst method must be get!"
    print res
    return JsonResponse(res)

#校验邮箱
def email_check(request):
    res = {"state": "error", "data": ""}
    if request.method == "GET":
        email = request.GET["email"]
        result = valid_email(email)
        if email == result:
            res["state"] = "success"
        else:
            res["data"] = result
    else:
        res["data"] = "requst method must be get!"
    return JsonResponse(res)

def register(request):
    if request.method == "POST":
        register_content = request.POST
        print register_content