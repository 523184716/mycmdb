#coding:utf-8

from  django import  forms
from django.forms import  fields
class AssetForm(forms.Form):
    hostname = forms.CharField(required=True,
                             error_messages={
                                 "required":"主机名不能为空"
                             })
    ip = forms.GenericIPAddressField(required=True,
                                     error_messages={
                                        "required":"IP地址不能为空",
                                         "GenericIPAddressField":"IP地址格式不对"
                                     })
    mac = forms.CharField(required=True,max_length=64,min_length=12,
                          error_messages={
                              "required":"MAC地址不能为空",
                              "max_length":"MAC长度不能超过64位",
                              "min_length":"MAC长度不能小于12位"
                          })
    cpu = forms.IntegerField(required=True,max_value=1000,
                             error_messages={
                                 "required":"CPU个数不能为空",
                                 "IntegerField":"CPU个数必须为整数",
                                 "max_value":"CPU最大值不能超过1000"
                             })
    memory = forms.CharField(required=True,max_length=32,
                             error_messages={
                                 "required":"MEMORY不能为空",
                                 "max_length":"MEMORY长度不能超过32位"
                             })
    disk = forms.CharField(required=True, max_length=32,
                             error_messages={
                                 "required": "DISK不能为空",
                                 "max_length": "DISK长度不能超过32位"
                             })
    sys_type = forms.CharField(required=True, max_length=32,
                             error_messages={
                                 "required": "操作系统类型不能为空",
                                 "max_length": "操作系统类型长度不能超过32位"
                             })
    sys_version = forms.CharField(required=True, max_length=32,
                             error_messages={
                                 "required": "操作系统版本不能为空",
                                 "max_length": "操作系统版本长度不能超过32位"
                             })
    remarks = forms.CharField(required=False,widget=forms.Textarea)