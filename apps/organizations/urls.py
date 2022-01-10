from django.urls import re_path
from apps.organizations.views import OrgView, OrgHomeView, TeacherListView, AddAskView, OrgTeacherView, OrgCourseView
from apps.organizations.views import OrgDescView, TeacherDetailView


urlpatterns = [

    re_path(r'^list/$', OrgView.as_view(), name="list"),
    re_path(r'^add_ask/$', AddAskView.as_view(), name="add_ask"),
    re_path(r'^(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    re_path(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name="teacher"),
    re_path(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    re_path(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),

    # 讲师列表页
    re_path(r'^teachers/$', TeacherListView.as_view(), name="teachers"),
    re_path(r'^teachers/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),
]