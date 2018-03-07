#coding:utf-8
import  hashlib
def secret(data):
    container = hashlib.md5()
    container.update(data)
    result = container.hexdigest()
    return  result