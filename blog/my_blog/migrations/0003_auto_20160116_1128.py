# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20160114_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='link',
            name='enable_comments',
        ),
        migrations.RemoveField(
            model_name='link',
            name='post_elsewhere',
        ),
        migrations.RemoveField(
            model_name='link',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='link',
            name='slug',
        ),
        migrations.AddField(
            model_name='link',
            name='categories',
            field=models.ManyToManyField(to='my_blog.Category'),
        ),
    ]
