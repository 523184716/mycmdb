# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from template_forms import AssetForm
from models import EquipmentDetail
from django.views.decorators.csrf import csrf_exempt
data_list = [{'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'OS X Yosemite', 'mac': '00:0c:25:cd:6b:e4', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.0', 'hostname': 'local_0', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:24:cd:6b:e3', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.1', 'hostname': 'local_1', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X El Capitan', 'mac': '00:0c:27:cd:2b:e1', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.2', 'hostname': 'local_2', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'win98', 'mac': '00:0c:26:cd:3b:e6', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.3', 'hostname': 'local_3', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'OpenSUSE', 'mac': '00:0c:26:cd:3b:e8', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.4', 'hostname': 'local_4', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:23:cd:5b:e4', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.5', 'hostname': 'local_5', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'Fedora', 'mac': '00:0c:26:cd:2b:e7', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.6', 'hostname': 'local_6', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win98', 'mac': '00:0c:25:cd:1b:e9', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.7', 'hostname': 'local_7', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'Linux ', 'mac': '00:0c:22:cd:2b:e4', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.8', 'hostname': 'local_8', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'RHEL', 'mac': '00:0c:21:cd:8b:e5', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.9', 'hostname': 'local_9', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'CentOS ', 'mac': '00:0c:29:cd:8b:e7', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.10', 'hostname': 'local_10', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:23:cd:5b:e7', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.11', 'hostname': 'local_11', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win10', 'mac': '00:0c:23:cd:4b:e3', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.12', 'hostname': 'local_12', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'OS X Mountain Lion', 'mac': '00:0c:25:cd:4b:e2', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.13', 'hostname': 'local_13', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'Fedora', 'mac': '00:0c:29:cd:7b:e3', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.14', 'hostname': 'local_14', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:23:cd:9b:e2', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.15', 'hostname': 'local_15', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'win98', 'mac': '00:0c:22:cd:4b:e4', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.16', 'hostname': 'local_16', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'Linux ', 'mac': '00:0c:27:cd:4b:e7', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.17', 'hostname': 'local_17', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'OpenSUSE', 'mac': '00:0c:23:cd:5b:e4', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.18', 'hostname': 'local_18', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:27:cd:1b:e6', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.19', 'hostname': 'local_19', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Mavericks', 'mac': '00:0c:26:cd:9b:e5', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.20', 'hostname': 'local_20', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'CentOS ', 'mac': '00:0c:26:cd:6b:e7', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.21', 'hostname': 'local_21', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'OpenSUSE', 'mac': '00:0c:25:cd:9b:e8', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.22', 'hostname': 'local_22', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Mavericks', 'mac': '00:0c:28:cd:7b:e6', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.23', 'hostname': 'local_23', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'macOS Sierra', 'mac': '00:0c:21:cd:7b:e7', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.24', 'hostname': 'local_24', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'Ubuntu', 'mac': '00:0c:29:cd:9b:e8', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.25', 'hostname': 'local_25', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'Fedora', 'mac': '00:0c:26:cd:4b:e4', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.26', 'hostname': 'local_26', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Yosemite', 'mac': '00:0c:25:cd:8b:e9', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.27', 'hostname': 'local_27', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win98', 'mac': '00:0c:25:cd:2b:e8', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.28', 'hostname': 'local_28', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Mountain Lion', 'mac': '00:0c:26:cd:7b:e9', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.29', 'hostname': 'local_29', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win8', 'mac': '00:0c:21:cd:4b:e8', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.30', 'hostname': 'local_30', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Yosemite', 'mac': '00:0c:23:cd:2b:e5', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.31', 'hostname': 'local_31', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:26:cd:9b:e4', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.32', 'hostname': 'local_32', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'OS X Yosemite', 'mac': '00:0c:22:cd:7b:e3', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.33', 'hostname': 'local_33', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'OS X Yosemite', 'mac': '00:0c:24:cd:1b:e7', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.34', 'hostname': 'local_34', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'macOS Sierra', 'mac': '00:0c:27:cd:5b:e1', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.35', 'hostname': 'local_35', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win98', 'mac': '00:0c:25:cd:1b:e4', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.36', 'hostname': 'local_36', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'Ubuntu', 'mac': '00:0c:22:cd:9b:e6', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.37', 'hostname': 'local_37', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Mavericks', 'mac': '00:0c:28:cd:4b:e7', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.38', 'hostname': 'local_38', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win2000', 'mac': '00:0c:28:cd:7b:e2', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.39', 'hostname': 'local_39', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'OS X Mountain Lion', 'mac': '00:0c:26:cd:5b:e9', 'cpu_count': 3, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.40', 'hostname': 'local_40', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'Ubuntu', 'mac': '00:0c:22:cd:1b:e3', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.41', 'hostname': 'local_41', 'sys_type': 'Linux'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'OS X Mountain Lion', 'mac': '00:0c:21:cd:6b:e2', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 4G', 'ip': '192.168.1.42', 'hostname': 'local_42', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'win8', 'mac': '00:0c:23:cd:1b:e8', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 32G', 'ip': '192.168.1.43', 'hostname': 'local_43', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win xp', 'mac': '00:0c:26:cd:4b:e3', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.44', 'hostname': 'local_44', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 600GB SAS 10K 2.5', 'sys_version': 'OS X Mavericks', 'mac': '00:0c:25:cd:3b:e7', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.45', 'hostname': 'local_45', 'sys_type': 'Mac'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win8', 'mac': '00:0c:25:cd:3b:e9', 'cpu_count': 4, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.46', 'hostname': 'local_46', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'win2000', 'mac': '00:0c:23:cd:1b:e8', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 16G', 'ip': '192.168.1.47', 'hostname': 'local_47', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 200GB SAS 10K 2.5', 'sys_version': 'win8', 'mac': '00:0c:21:cd:5b:e2', 'cpu_count': 1, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.48', 'hostname': 'local_48', 'sys_type': 'Windows'}, {'disk': 'SEAGATE 400GB SAS 10K 2.5', 'sys_version': 'macOS Sierra', 'mac': '00:0c:21:cd:1b:e6', 'cpu_count': 2, 'memory': 'SAMSUNG DDR4 2400T DDR3 8G', 'ip': '192.168.1.49', 'hostname': 'local_49', 'sys_type': 'Mac'}]

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
    get_page=divmod(len(data_list),per_page_num)
    if get_page[1] == 0:
        total_page = get_page[0]
    else:
        total_page = get_page[1]
    if pagenum <= 3:
        Prange = range(1,6)
    elif pagenum+ 2>= total_page:
        Prange = range(total_page-4,total_page+1)
    else:
        Prange = range(pagenum-2,pagenum+3)
    data = data_list[start:end]
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

@csrf_exempt
def postasset(request):
    """
    requestdata：获取post提交的数据
    """
    result = {"state":"error","data":""}
    if request.method == "POST":
        requestdata = result.POST
        try:
            EquipmentDetail.objects.create(**requestdata)
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