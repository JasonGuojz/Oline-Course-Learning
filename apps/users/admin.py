from django.contrib import admin

from apps.users.models import UserProfile

# 在任何一个app的目录下新建一个admin.py, 添加如下代码即可修改管理后台的名称和标题
admin.site.site_header = '数据管理(家桢)'  # 设置header
admin.site.site_title = '数据管理(家桢)'  # 设置title
admin.site.index_title = '数据管理(家桢)'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
