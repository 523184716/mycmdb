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
