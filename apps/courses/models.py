from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import CourseOrg, Teacher
from ckeditor_uploader.fields import RichTextUploadingField


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='讲师')
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name="课程机构")
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    notice = models.CharField(verbose_name="课程公告", max_length=300, default="")
    category = models.CharField(default="后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="老师告诉你")
    is_classics = models.BooleanField(default=False, verbose_name="是否经典")
    detail = RichTextUploadingField(verbose_name="课程详情")
    is_banner = models.BooleanField(default=False, verbose_name="是否广告位")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)

    # detail = UEditorField(verbose_name="课程详情", width=600, height=300, imagePath="courses/ueditor/images/",
    #                       filePath="courses/ueditor/files/", default="")

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def lesson_nums(self):
        return self.lesson_set.all().count()

    def show_image(self):
        from django.utils.safestring import mark_safe
        return mark_safe(f"<img src='{self.image.url}' width='{60}' height='{50}'>")

    show_image.short_description = "图片"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe(f"<a href='/course/{self.id}'>跳转</a>")

    go_to.short_description = "跳转"


class BannerCourse(Course):
    class Meta:
        verbose_name = "课程轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name="章节名")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    url = models.CharField(max_length=1000, verbose_name="访问地址")

    class Meta:
        verbose_name = '章节视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    file = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='下载地址', max_length=200)

    # 文件被传至`MEDIA_ROOT/course`目录，MEDIA_ROOT由你在settings文件中设置

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    tag = models.CharField(max_length=100, verbose_name="标签")

    class Meta:
        verbose_name = "课程标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag
