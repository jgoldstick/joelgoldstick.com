from django.db import models
from django.contrib import admin
from markdown import markdown
from markdown.extensions import codehilite
import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=250, help_text="250 Characters Max")
    slug = models.SlugField(
        unique=True, help_text="Suggested value generated from title. Must be unique."
    )
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "slug", "description", "id"]


admin.site.register(Category, CategoryAdmin)


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, "Live"),
        (DRAFT_STATUS, "Draft"),
        (HIDDEN_STATUS, "Hidden"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        unique_for_date="pub_date",
        help_text="Suggested value generated from title. Must be unique.",
    )
    excerpt = models.TextField(blank=True)
    excerpt_html = models.TextField(editable=False, blank=True)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    # pub_date = models.DateTimeField(default=datetime.datetime.now)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    categories = models.ManyToManyField(Category)

    def save(self, force_insert=False, force_update=False):
        # self.body_html = markdown(self.body, extensions=['codehilite', 'headerid'])
        self.body_html = markdown(
            self.body,
            output_format="html5",
            extensions=[
                "codehilite",
            ],
        )
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt, extensions=["codehilite"])
        super(Entry, self).save(force_insert, force_update)
        # super(Entry, self).save()

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print("/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug))
        return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    """
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('views.entry.detail',
                       args=[str(self.pub_date.strftime("%Y/%b/%d").lower()),
                             str(self.slug)])
    """


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "status", "pub_date", "modified_date", "id"]


admin.site.register(Entry, EntryAdmin)

"""
class Link(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    url = models.URLField(unique=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    # tags = TagField()
    enable_comments = models.BooleanField(default=False)
    post_elsewhere = models.BooleanField(default=False)
"""
