# Generated by Django 3.2.7 on 2021-11-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20211123_1405'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='dsc',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.courseorg', verbose_name='课程机构'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否广告位'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_classics',
            field=models.BooleanField(default=False, verbose_name='是否经典'),
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
    ]