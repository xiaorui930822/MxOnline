# -*- coding: utf-8 -*-
__author__ = 'xurui'
__date__ = '2018/5/27 0027 19:54'

from django.urls import path, re_path

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailView, \
    UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView


app_name = "users"

urlpatterns = [
    # 用户信息
    path('info/', UserinfoView.as_view(), name='user_info'),
    # re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),
    # 用户修改头像
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),
    # 用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd'),
    # 发送邮箱验证码
    path('sendemail_code/', SendEmailView.as_view(), name='sendemail_code'),

    # 修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    path('mycourse/', MyCourseView.as_view(), name='mycourse'),

    # 我的收藏-机构
    path('myfav/org/', MyFavOrgView.as_view(), name='myfav_org'),

    # 我的收藏-教师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name='myfav_teacher'),

    # 我的收藏-课程
    path('myfav/course/', MyFavCourseView.as_view(), name='myfav_course'),

    # 我的消息
    path('mymessage/', MyMessageView.as_view(), name='mymessage'),
]
