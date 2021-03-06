# Generated by Django 3.1.2 on 2020-10-18 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="250 Characters Max", max_length=250),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Suggested value generated from title. Must be unique.",
                        unique=True,
                    ),
                ),
                ("description", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("description", models.TextField(blank=True)),
                ("description_html", models.TextField(blank=True)),
                ("url", models.URLField(unique=True)),
                ("pub_date", models.DateTimeField(default=datetime.datetime.now)),
                ("slug", models.SlugField(unique_for_date="pub_date")),
                ("enable_comments", models.BooleanField(default=False)),
                ("post_elsewhere", models.BooleanField(default=False)),
                (
                    "posted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Suggested value generated from title. Must be unique.",
                        unique_for_date="pub_date",
                    ),
                ),
                ("excerpt", models.TextField(blank=True)),
                ("excerpt_html", models.TextField(blank=True, editable=False)),
                ("body", models.TextField()),
                ("body_html", models.TextField(blank=True, editable=False)),
                ("pub_date", models.DateTimeField(default=datetime.datetime.now)),
                ("modified_date", models.DateTimeField(default=datetime.datetime.now)),
                ("featured", models.BooleanField(default=False)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Live"), (2, "Draft"), (3, "Hidden")], default=1
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("categories", models.ManyToManyField(to="blog_app.Category")),
            ],
            options={
                "verbose_name_plural": "Entries",
                "ordering": ["-pub_date"],
            },
        ),
    ]
