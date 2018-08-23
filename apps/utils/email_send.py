# -*- coding: utf-8 -*-
__author__ = 'xurui'
__date__ = '2018/4/19 0019 19:25'


from random import Random
from django.core.mail import send_mail
from django.shortcuts import render
from users.models import EmailVerifyRecord
from MxOnline3.settings import EMAIL_FROM

def send_register_email(email, send_type = 'register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code =random_str(6)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = "MX在线网注册激活链接"
        email_body = "请点击下面的激活链接你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status= send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = "MX在线网密码重置链接"
        email_body = "请点击下面的激活链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'update_email':
        email_title = "MX在线网邮箱修改验证码"
        email_body = "你的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(randomlength):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):#字符串的字母个数
        str += chars[random.randint(0, length)]
    return str