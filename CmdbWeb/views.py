# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from template_forms import AssetForm
from models import EquipmentDetail
from django.views.decorators.csrf import csrf_exempt
from sshconnect import createconnect,docommand
from clientfile import datacollect
import  os
import  hmac,hashlib
import  json
import  time
from ansible.playbook.play import  Play
def asset(request):
    obj = AssetForm()
    return  render(request,'cmdbweb/asset_list.html',locals())
# Create your views here.

def getasset(request,pagenum):
    """
    per_page_num：每页显示的数据量
    total_page：数据总共有多少页
    data：当前页显示的数据
    Prange：前端只展示五个页码
    :return:
    """
    per_page_num = request.session.get("per_page_num",5)
    pagenum = int(pagenum)
    start = (pagenum-1) * per_page_num
    end = pagenum * per_page_num
    getdata = EquipmentDetail.objects.all()
    #获取总页数
    get_page=divmod(len(getdata),per_page_num)
    if get_page[1] == 0:
        total_page = get_page[0]
    else:
        total_page = get_page[0] + 1
    #获取展示到前端的页码
    if total_page < 5:
        Prange = range(1,total_page+1)
    elif pagenum <= 3:
        Prange = range(1,6)
    elif pagenum+ 2>= total_page:
        Prange = range(total_page-4,total_page+1)
    else:
        Prange = range(pagenum-2,pagenum+3)

    #数据库获取的是obj对象，json序列化有问题，得先循环获取
    data_result = getdata[start:end]
    data = []
    for obj in data_result:
        dicts = {
            "id":obj.id,
            "hostname":obj.hostname,
            "ip":obj.ip,
            "mac":obj.mac,
            "cpu_count":obj.cpu_count,
            "memory":obj.memory,
            "disk":obj.disk,
            "sys_type":obj.sys_type,
            "sys_version":obj.sys_version
        }
        data.append(dicts)
    result ={"data":data,"Prange":Prange,"total_page":total_page,"current_page":pagenum}
    return JsonResponse(result)

def pagenum(request):
    """
    url_path：获取设置每页显示的数量后重定向到数据的开始页
    per_page_num：获取每页显示的数据量并加入到session
    :param request:
    :return:
    """
    try:
        url_path = request.GET["url_path"]
        per_page_num = request.GET["data"]
    except:
        request.session["per_page_num"] = 5
    else:
        request.session["per_page_num"] = per_page_num
    return HttpResponseRedirect(url_path)

#接收采集的静态服务器数据
@csrf_exempt
def postasset(request):
    """
    requestdata：获取post提交的数据
    """
    result = {"state":"error","data":""}
    if request.method == "POST":
        #获取到的数据是Unicode编码，数据不是很美观，取出做了重组
        adddata = {}
        requestdata = request.POST
        adddata["hostname"] = requestdata["hostname"]
        adddata["ip"] = requestdata["ip"]
        adddata["cpu_count"] = requestdata["cpu_count"]
        adddata["sys_version"] = requestdata["sys_version"]
        adddata["mac"] = requestdata["mac"]
        adddata["memory"] = requestdata["memory"]
        adddata["disk"] = requestdata["disk"][1:-1].replace("'","")
        adddata["sys_type"] = requestdata["sys_type"]
        try:
            EquipmentDetail.objects.create(**adddata)
        except Exception as e:
            result["data"] = str(e)
        else:
            result["state"] = "success"
            result["data"] = "your data is saved"
    else:
        result["data"] = "request method must be post"
    return JsonResponse(result)

def servicerlogindata(request):
    if request.method == "POST":
        pass
    else:
        return  render(request,'cmdbweb/service_list.html',locals())

#接收设备信息，下发采集配置文件并执行
def addeqip(request):
    result = {"state":"error","data":""}
    if request.method == "POST":
        requestdata = request.POST
        print requestdata
        ip = requestdata.get("ip","")
        username = requestdata.get("username","")
        password = requestdata.get("password","")
        port = requestdata.get("port","")
        if not port:
            port = 22
        else:
            port = int(port)
        print ip,username,password
        if ip and username and password:
            #datacollect.ip = ip
            dstipdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cmdb/datacollect.py")
            os.system("sed -i 's/ip = .*/ip = \"{}\"/' {}".format(ip, dstipdir))
            createresult = createconnect(ip,username,password,port,docommand)
            if createresult["state"] == "success":
                result["state"] = "success"
                result["data"] = "success"
        else:
            result["data"] = "ip and username password is not be null"
    else:
        result["data"] = "request method must be post"
    return JsonResponse(result)

def terminal(request,id):
    id = int(id)
    print id
    dstdata = EquipmentDetail.objects.get(id = id)
    dstip = dstdata.ip

    port = 22
    user = "root"
    return  render(request,"cmdbweb/terminal.html",locals())

def create_signature(secret,*parts):
    hash = hmac.new(secret,digestmod = hashlib.sha1)
    for parts in parts:
        hash.update(str(parts))
    return hash.hexdigest()

def get_auth_obj(request):
    user = request.user.username
    gateone_server = "https://10.36.8.222"

    secret = "MGFiNmU5YmQ5ZTRhNDdiMjkzNjI0MzRlY2UxYzk0MGFhZ"
    print type(str(secret))
    api_key = "YWNkYjYxOTdjMGFhNGZmM2E5MjI3OThiMTAyMDU0OGViZ"

    authobj = {
        'api_key': api_key,
        'upn': "gateone",
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(str(secret), digestmod=hashlib.sha1)
    print my_hash
    my_hash.update(authobj['api_key'] + authobj['upn'] + authobj['timestamp'])

    authobj['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authobj}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)
