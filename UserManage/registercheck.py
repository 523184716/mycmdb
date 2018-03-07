#coding:utf-8

from models import UserManage
import  re

#手机号校验函数
def valid_phone(phone):
    try:
        phone = UserManage.objects.get(phone=phone)
    except:
        return phone
    else:
        return "此号码已注册"

#用户校验函数
def valid_user(user):
    try:
        db_user = UserManage.objects.get(user=user)
    except:
        return user
    else:
        return "用户名已存在"

#邮箱校验函数
def valid_email(email):
    result = re.match(r"\w+@\w+.[a-zA-Z]{2,5}", email)
    print result
    if result:
        return email
    else:
        return "邮箱格式不符合规则"

#密码校验函数
def valid_password(*args):
    password = args[0]
    confirm_password = args[1]
    if str(password).isdigit():
        return "密码必须存在特殊字符"
    elif str(password).isalnum():
        return "密码必须存在特殊字符"
    elif password != confirm_password:
        return "两次输入的密码不一致，请确认"
    else:
        return password