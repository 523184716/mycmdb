#coding:utf-8
from django.shortcuts import  render,render_to_response,HttpResponse,redirect
from UserManage.forms import UserRegister
from UserManage.registercheck import *
from django.core.exceptions import ValidationError
from django.http import JsonResponse , HttpResponseRedirect
from PIL import  Image
from datasecret import secretdata
from UserManage import  create_images
from io import  BytesIO

def base(request):
    userregister = UserRegister()
    # print userregister
    return  render(request,"cmdbweb/Base/base.html",locals())

def index(request):
    userregister = UserRegister()
    # print userregister
    return render(request, "cmdbweb/Base/base.html", locals())

def login(request):
    if request.method == "POST":
        login_data = request.POST
        username = login_data["username"]
        password = login_data["password"]
        print username
        print password
        try:
            #判断用户是否存在
            check_user = UserList.objects.get(username=username)
            # check_user = UserList.objects.filter(username=username).count()
            print check_user
        except Exception as e:
            return HttpResponseRedirect("login")
        else:
            print check_user.password
            #用户存在的情况下判断密码是否正确
            if check_user.password == secretdata(password):
                print "ceshi2"
                #都OK的情况下跳转至首页并添加cookie至地址中，设置session
                response_url = HttpResponseRedirect("index")
                response_url.set_cookie("username",username)
                request.session["username"]=username
                request.session["is_login"]=True
                token = request.COOKIES.get("token")
                if token:
                    return response_url
                else:
                    return HttpResponseRedirect("login")
            else:
                return HttpResponseRedirect("login")
    else:
        #直接post之前得先get获取token
        response = render(request, "cmdbweb/login.html")
        response.set_cookie("token", "hello")
        return  response

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

#用户注册
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
            UserList.objects.create(**clean_data)
            res["state"]="success"

        else:
            res["data"]=data_check.errors
    else:
        res["data"]="request method must be post"
    return JsonResponse(res)

def create_code_img(request):
    f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片
    # 调用check_code生成照片和验证码
    img, code = create_images.Create_image()
    request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
    # print request.session["check_code"]
    img.save(f,'PNG') #生成的图片放置于开辟的内存中
    # print f.getvalue()
    return HttpResponse(f.getvalue())  #将内存的数据读取出来，并以HttpResponse返回