from django.contrib import admin

from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag, BannerCourse
from import_export.admin import ImportExportActionModelAdmin


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    exclude = ["add_time"]


class CourseResourceInline(admin.StackedInline):
    model = CourseResource
    style = "tab"
    extra = 1


@admin.register(Course)
class CourseAdmin(ImportExportActionModelAdmin):
    list_display = ['name', 'desc', 'show_image', 'go_to', 'detail', 'degree', 'learn_times', 'students',
                    'is_banner']  # 设置页面可以展示的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']  # 搜索条件设置
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']  # 设置过滤选项
    list_editable = ["degree", "desc"]  # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    readonly_fields = ['add_time']
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']
    readonly_fields = ['add_time']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    readonly_fields = ['add_time']


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']
    readonly_fields = ['add_time']


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ['course', 'tag', 'add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'add_time']
    readonly_fields = ['add_time']


@admin.register(BannerCourse)
class BannerCourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'show_image', 'go_to', 'detail', 'degree', 'learn_times', 'students', 'is_banner']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']  # 设置过滤选项
    list_editable = ["degree", "desc"]
    readonly_fields = ['add_time']
    exclude = ['fav_nums']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(is_banner=True)
        return qs
