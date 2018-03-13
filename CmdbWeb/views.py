# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

def asset(request):
    return  render(request,'cmdbweb/asset_list.html',locals())
# Create your views here.
