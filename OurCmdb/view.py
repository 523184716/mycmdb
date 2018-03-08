#coding:utf-8
from django.shortcuts import  render,render_to_response,HttpResponse
from UserManage.forms import UserRegister
from UserManage.registercheck import *
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from PIL import  Image
from datasecret import secretdata

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
        print result
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
    res = {"state":"error","data":""}
    if request.method == "POST":
        #提交的数据进行校验，没有图片和文件的话直接一个就行
        data_check = UserRegister(request.POST,request.FILES)
        if data_check.is_valid():
            clean_data =  data_check.cleaned_data
            #设置图片要保存的路径及名字
            image_name = "static/image/"+clean_data["photo"].name
            #打开图片
            img = Image.open(clean_data["photo"])
            #保存图片至对应的位置
            img.save(image_name)
            #更改图片保存至数据库的值(一个文件存放的链接)
            clean_data["photo"]=image_name
            #密码更换为加密之后的数据
            clean_data["password"]=secretdata(clean_data["password"])
            del  clean_data["confirm_password"]
            #添加至数据库
            UserManage.objects.create(**clean_data)
            res["state"]="success"

        else:
            res["data"]=data_check.errors
    else:
        res["data"]="request method must be post"
    return JsonResponse(res)