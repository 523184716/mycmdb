#coding:utf-8

from datacollect import Getsysdata
from  senddata import Postdata
url = "http://192.192.1.34:8022/equip/postasset"

data = Getsysdata()
sendData = data.mergedata()

sender = Postdata(url,sendData)
sender.get_request()
response = sender.get_response()
print(response)