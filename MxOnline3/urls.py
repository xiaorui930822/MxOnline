"""MxOnline3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.views.generic import TemplateView
from django.views.static import serve

from MxOnline3.settings import MEDIA_ROOT
from users import views
from organization.views import OrgView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('captcha', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', views.ActiveUserView.as_view(), name="user_active"),  # Django2.0写法
    path('forget/', views.ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', views.ResetView.as_view(), name="reset_pwd"),  # Django2.0写法
    path('modify_pwd/', views.ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构url配置
    path('org/', include('organization.urls', namespace='org')),
    # 课程url配置
    path('course/', include('courses.urls', namespace='course')),
    # 配置上传文件的访问处理函数
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    path('users/', include('users.urls', namespace='users')),

    # 富文本编辑器url
    path('ueditor/', include('DjangoUeditor.urls')),

]

# 全局404页面配置
hander404 = 'users.views.page_not_found'
hander500 = 'users.views.page_error'
