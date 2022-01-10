from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 因为organization这些app都可能import BaseModel，所以放在User app，在最底层是合适的
class BaseModel(models.Model):
    add_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')  # auto_now:每当对象被保存时将字段设为当前日期，常用于保存最后修改时间。

    class Meta:  # 抽象基类
        abstract = True


class UserProfile(AbstractUser):
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )  # 第一个元素表示存在数据库内真实的值，第二个表示页面上显示的具体内容。

    nick_name = models.CharField(max_length=50, verbose_name='昵称', default="")  # 非必填
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=GENDER_CHOICE)
    address = models.CharField(max_length=100, verbose_name='地址', default="")
    # mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号码')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    image = models.ImageField(upload_to='head_image/%Y/%m', default='default.jpg', verbose_name="用户头像")

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def unread_nums(self):
        return self.usermessage_set.filter(has_read=False).count()  # 未读消息数量

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        return self.username  # 是django中的必填字段

