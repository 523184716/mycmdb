#coding:utf-8

import  paramiko
import os

def createconnect(ip,username,password,port,fun):
    """
    :param ip:
    :param username:
    :param password:
    :param port:
    上述参数用于创建一个ssh远程连接
    """
    result = {"state":"error","data":""}
    try:
        print "222"
        transport = paramiko.Transport((ip,port))
        transport.connect(username=username,password=password)
    except Exception as e:
        result["state"] = "error"
        result["data"] = str(e)
    else:
        fun(ip,username,password,port,transport)
        result["state"] = "success"
        result["data"] = transport
    return result

def putfile(ip,username,password,port,transport):
    """
    :param ip:
    :param username:
    :param password:
    :param port:
    :param transport:
    根据前面创建的传输通道来建立sftp连接传输文件
    """
    sourdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"clientfile")
    dstdir = "/opt/cmdb/"
    sftpconnect = paramiko.SFTPClient.from_transport(transport)
    try:
        sftpconnect.put(os.path.join(sourdir,"senddata.py"),os.path.join(dstdir,"senddata.py"))
        sftpconnect.put(os.path.join(sourdir, "datacollect.py"), os.path.join(dstdir, "datacollect.py"))
        sftpconnect.put(os.path.join(sourdir, "main.py"), os.path.join(dstdir, "main.py"))
    except Exception as e:
        print str(e)
    finally:
        transport.close()

def docommand(ip,username,password,port,transport):
    creatdir = "mkdir -p /opt/cmdb"
    test_command = "ls /opt"
    exec_command = "python /opt/cmdb/main.py"
    ssh = paramiko.SSHClient()
    ssh._transport = transport

    try:
        ssh.exec_command(creatdir)
        stdin,stdout,stderr = ssh.exec_command(test_command)
        if "cmdb" in stdout.read():
            createconnect(ip,username,password,port,putfile)
            ssh.exec_command(exec_command)
    except Exception as e:
        print str(e)
    finally:
        transport.close()



