# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EquipmentDetail(models.Model):
    hostname = models.CharField(max_length=64,verbose_name="主机名字")
    ip = models.GenericIPAddressField(verbose_name="IP地址")
    mac = models.CharField(max_length=64,verbose_name="机器Mac地址")
    sys_type = models.CharField(max_length=32,verbose_name="操作系统类型")
    sys_version = models.CharField(max_length=32,verbose_name="操作系统版本")
    cpu_count = models.IntegerField(verbose_name="cpu个数")
    disk = models.CharField(max_length=32,verbose_name="硬盘大小")
    memory = models.CharField(max_length=32,verbose_name="内存大小")

    def __unicode__(self):
        return  self.hostname

class Servicer(models.Model):
    ip = models.GenericIPAddressField(verbose_name="服务器地址")
    username = models.CharField(max_length=32,verbose_name="登录用户名")
    password = models.CharField(max_length=64,verbose_name="登录密码")
    port = models.IntegerField(max_length=5,verbose_name="登录端口")

    def __unicode__(self):
        return self.ip
