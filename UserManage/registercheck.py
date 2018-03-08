#coding:utf-8

from models import UserManage
import  re

#手机号校验函数
def valid_phone(phone):
    phone_count = UserManage.objects.filter(phone=phone).count()
    if phone_count:
        return "此号码已注册"
    elif len(str(phone)) < 7:

        return "手机号码不对"
    elif len(str(phone)) > 16:

        return "手机号码不对"
    else:
        return  phone

#用户校验函数
def valid_user(user):
    db_user = UserManage.objects.filter(username=user).count()
    if db_user:
        return "用户名已 存在"
    elif  len(user) < 5:
        return "用户长度在5-32位"
    elif len(user) > 32:
        return "用户长度在5-32位"
    else:
        return user
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
        return "密码长度不能小于6,并且得存在特殊字符"
    elif str(password).isalnum():
        return "密码长度不能小于6,并且得存在特殊字符"
    elif password != confirm_password:
        return "两次输入的密码不一致，请确认"
    elif len(password) < 6:
        return "密码长度不能小于6,并且得存在特殊字符"
    else:
        return password