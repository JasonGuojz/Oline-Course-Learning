from django.urls import re_path

from apps.courses.views import CourseListView, CourseDetailView, CourseLessonView, CourseCommentsView, VideoView

urlpatterns = [
    re_path(r'^list/$', CourseListView.as_view(), name="list"),
    re_path(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
    re_path(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name="lesson"),
    re_path(r'^(?P<course_id>\d+)/comments/$', CourseCommentsView.as_view(), name="comments"),
    re_path(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)$', VideoView.as_view(), name="video"),
]