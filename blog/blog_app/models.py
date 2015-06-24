from django.db import models
from django.contrib import admin
from markdown import markdown
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250, help_text="250 Characters Max")
    slug = models.SlugField(unique=True,
        help_text="Suggested value generated from title. Must be unique.")
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='pub_date',
            help_text="Suggested value generated from title. Must be unique.")
    excerpt = models.TextField(blank=True)
    excerpt_html = models.TextField(editable=False, blank=True)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    modified_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    categories = models.ManyToManyField(Category)
    # tags = TagField()

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body, ['codehilite', 'headerid'])
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt, ['codehilite'])
        super(Entry, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(),
                                 self.slug)


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'status', 'pub_date']

admin.site.register(Entry, EntryAdmin)


class Link(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    url = models.URLField(unique=True)
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    # tags = TagField()
    enable_comments = models.BooleanField(default=False)
    post_elsewhere = models.BooleanField(default=False)
