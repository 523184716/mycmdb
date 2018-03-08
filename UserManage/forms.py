#coding:utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.forms import  ValidationError
from models import UserManage
import  re
class UserRegister(forms.Form):
    username = forms.CharField(max_length=32,min_length=5,
               label="用户名",
               widget=forms.TextInput({"class":"form-control","placeholder":"用户名"})
               )
    password = forms.CharField(max_length=64,min_length=6,
               label="密码",
               widget=forms.PasswordInput({"class":"form-control","placeholder":"密码"})
               )
    confirm_password = forms.CharField(max_length=64, min_length=6,
                               label="确认密码",
                               widget=forms.PasswordInput({"class": "form-control", "placeholder": "确认密码"})
                               )
    email = forms.CharField(max_length=32,min_length=6,
                label="邮箱",
                widget=forms.TextInput({"class":"form-control","placeholder":"邮箱"})
                )
    phone = forms.CharField(max_length=16,min_length=7,
                label="手机号码",
                widget=forms.TextInput({"class":"form-control","placeholder":"手机号码"})
                )
    photo = forms.ImageField(label="用户头像")

    def clean_user(self):
        user = self.cleaned_data.get("user")
        try:
            db_user = UserManage.objects.get(user=user)
        except:
            return user
        else:
            return ValidationError("用户名已存在")

    def clean_passwd(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if str(password).isdigit():
            raise  ValidationError("密码必须存在特殊字符")
        elif str(password).isalnum():
            raise ValidationError("密码必须存在特殊字符")
        elif password != confirm_password:
            raise ValidationError("两次输入的密码不一致，请确认")
        else:
            return password

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        try:
            phone = UserManage.objects.get(phone=phone)
        except:
            return phone
        else:
            raise ValidationError("此号码已注册")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        result = re.match(r"\w+@\w+.[a-zA-Z]{2,5}",email)
        if result:
            return email
        else:
            raise ValidationError("邮箱格式不符合规则")