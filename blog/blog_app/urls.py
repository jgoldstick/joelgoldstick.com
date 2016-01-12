from django.conf.urls import patterns, url, include
from blog_app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    url(r'^$', views.entries_index, name="index"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entry_detail),
    url(r'^categories/$', views.category_list),
    url(r'^categories/(?P<category>\w+)/$', views.entries_by_category),
    url(r'^contact/$', views.contact),
    url(r'^feed/latest/$', views.LatestEntriesFeed()),
    url(r'^cbv/list/$', views.EntryList.as_view()),
    url(r'^cbv/create/$', login_required(views.EntryCreate.as_view())),
    url(r'^cbv/update/(?P<pk>\d+)/$', login_required(views.EntryUpdate.as_view())),
    url(r'^cbv/delete$', views.EntryList.as_view()),
]
