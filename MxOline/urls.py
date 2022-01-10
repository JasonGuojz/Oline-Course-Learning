"""MxOline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from .settings import MEDIA_ROOT
from .settings import STATIC_ROOT

from apps.users.views import LoginView, LogoutView, RegisterView, DynamicLoginView, SendSmsView
from apps.operations.views import IndexView
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),  # 反向解析和命名空间，通过这个name参数，可以反向解析URL、反向URL匹配、反向URL查询或者简单的URL反查。
    path('', IndexView.as_view(), name="index"),
    path('register/', RegisterView.as_view(), name="register"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('captcha/', include('captcha.urls')),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),

    # 配置上传文件的访问url
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 机构相关页面
    re_path(r'^org/', include(('apps.organizations.urls', "organizations"), namespace="org")),

    # 公开课相关页面
    re_path(r'^course/', include(('apps.courses.urls', "courses"), namespace="course")),

    # 用户相关操作
    re_path(r'^op/', include(('apps.operations.urls', "operations"), namespace="op")),

    # 个人中心
    re_path(r'^users/', include(('apps.users.urls', "users"), namespace="users")),

    # ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
