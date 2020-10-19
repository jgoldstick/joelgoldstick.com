# Generated by Django 3.1.2 on 2020-10-19 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_auto_20201019_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(default='jcg', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to='blog_app.Category'),
        ),
        migrations.AddField(
            model_name='entry',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.IntegerField(choices=[(1, 'Live'), (2, 'Draft'), (3, 'Hidden')], default=1),
        ),
        migrations.AddField(
            model_name='link',
            name='enable_comments',
            field=models.BooleanField(default=False),
        ),
    ]
