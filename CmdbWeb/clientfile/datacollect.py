#coding:utf-8

import os
import psutil
import uuid

ip = "192.192.1.34"

def systype():
    """
    根据系统类型来获取系统名字以及系统版本
    :return:
    """
    result = {"hostname":"","sys_type":"","sys_version":""}
    if os.name == "nt":
        import _winreg
        result["sys_type"] = "windows"
        result["hostname"] = os.getenv("computername")
        try:
            reg_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion")
            sys_version = _winreg.QueryValueEx(reg_key, "ProductName")[0]
        except Exception as e:
            result["sys_version"] = str(e)
        else:
            result["sys_version"] = sys_version
    elif os.name == "posix":
        result["sys_type"] = "linux"
        result["hostname"] = os.popen("hostname").read()
        if os.path.isfile("/etc/redhat-release"):
            result["sys_version"] = os.popen("cat /etc/redhat-release").read()
        else:
            result["sys_version"] = os.popen("cat /proc/version").read()
    else:
        result["hostname"] = "unix or mac"
        result["sys_type"] = "unix or mac"
        result["sys_version"] = "uknow"
    return result

class Getsysdata:
    """
    系统静态数据采集
    """
    def __init__(self):
        self.result = {}
        self.ip = ip
    def get_ip(self):
        return self.ip

    def get_hostname(self):
        hostname = systype()["hostname"].replace("\n","")
        return  hostname

    def get_sys_type(self):
        sys_type = systype()["sys_type"].replace("\n","")
        return sys_type

    def get_sys_version(self):
        sys_version = systype()["sys_version"].replace("\n","")
        return  sys_version

    def get_cpu_count(self):
        cpu = psutil.cpu_count()
        return  str(cpu)

    def get_memory(self):
        memory = str(psutil.virtual_memory().total / 1024 / 1024) + "M"
        return  str(memory)

    def get_disk(self):
        """
        循环几个主要挂载点获取每个点的大小
        :return:
        """
        result = {}
        disk = psutil.disk_partitions()
        for partition in disk:
            point = partition.mountpoint
            result[point] = str(psutil.disk_usage(point).total /1024/1024)+"M"
        return result

    def get_mac(self):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        result = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        return result

    def mergedata(self):
        """
        getsysdata.__dict__：获取类的所有方法
        callable(value)：过滤可用方法，在上自定义条件来获取自定义的方法
        value(self)：方法实例化
        :return:
        """
        allfunction = Getsysdata.__dict__
        for key,value in allfunction.items():
            if "get_" in key and callable(value):
                name = key.replace("get_","")
                self.result[name] = value(self)
        return self.result

if __name__ == "__main__":
    data = systype()
    print data
    data = Getsysdata()
    disk = data.mergedata()
    print disk