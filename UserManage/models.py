# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManage(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=128,verbose_name="用户密码")
    email = models.EmailField(verbose_name="用户邮箱")
    phone = models.CharField(max_length=32,verbose_name="用户手机号码")
    photo = models.ImageField(upload_to="",verbose_name="用户图片")

    def __unicode__(self):
        return  self.username

class UserPerssion(models.Model):
    user_id = models.IntegerField(verbose_name="用户ID")
    perssion_id = models.IntegerField(verbose_name="权限ID")

class GroupManage(models.Model):
    groupname = models.CharField(max_length=32,verbose_name="组名字")

    def __unicode__(self):
        return  self.groupname

class UserGroup(models.Model):
    user_id = models.IntegerField(verbose_name="用户ID")
    group_id = models.IntegerField(verbose_name="组ID")


class PerssionDetail(models.Model):
    obj_id = models.IntegerField(verbose_name="操作对象ID")
    opera_name = models.CharField(max_length=32,verbose_name="操作类别")
    description = models.CharField(max_length=128,verbose_name="详情描述")

    def __unicode__(self):
        return  self.opera_name

class GroupPerssion(models.Model):
    group_id = models.IntegerField(verbose_name="组ID")
    perssion_id = models.IntegerField(verbose_name="权限ID")