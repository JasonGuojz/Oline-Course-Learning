# Generated by Django 3.2.7 on 2021-12-06 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_alter_coursecomments_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '课程轮播图', 'verbose_name_plural': '课程轮播图'},
        ),
    ]