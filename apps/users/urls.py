from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from apps.users.views import UserInfoView, MyMessageView, UploadImageView, ChangePwdView, ChangeMobileView
from apps.users.views import MyFavOrgView, MyFavTeacherView, MyFavCourseView

app_name = 'users'

urlpatterns = [
    re_path(r'^info/$', UserInfoView.as_view(), name="info"),
    re_path(r'^messages/$', MyMessageView.as_view(), name="messages"),

    re_path(r'^mycourse/$',
            login_required(TemplateView.as_view(template_name="usercenter-mycourse.html"), login_url="/login/"),
            {"current_page": "mycourse"}, name="mycourse"),
    re_path(r'^myfavorg/$', MyFavOrgView.as_view(), name="myfavorg"),
    re_path(r'^myfav_teacher/$', MyFavTeacherView.as_view(), name="myfav_teachers"),
    re_path(r'^myfav_course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 修改个人信息
    re_path(r'^image/upload/$', UploadImageView.as_view(), name="image"),
    re_path(r'^update/pwd/$', ChangePwdView.as_view(), name="update_pwd"),
    re_path(r'^update/mobile/$', ChangeMobileView.as_view(), name="update_mobile"),

]
