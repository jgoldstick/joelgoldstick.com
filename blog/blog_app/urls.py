#from django.conf.urls import patterns, url, include
from django.urls import path, re_path
from blog_app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^$', views.entries_index, name="index"),
    path('', views.entries_index, name="index"),
    re_path(r'(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entry_detail),
    path('<int:year>/<str:month>/<int:day>/<str:slug>', views.entry_detail),
    #url(r'^categories/$', views.category_list),
    path('categories/', views.category_list),
    #url(r'^categories/(?P<category>\w+)/$', views.entries_by_category),
    path('categories/<str:category>', views.entries_by_category),
    #url(r'^contact/$', views.contact),
    #url(r'^contact/$', views.contact),
    path('feed/latest/', views.LatestEntriesFeed()),
    #url(r'^feed/latest/$', views.LatestEntriesFeed()),
    #url(r'^cbv/list/$', views.EntryList.as_view()),
    path('contact/', views.contact),
    path('cbv/list/', views.EntryList.as_view()),
    #url(r'^cbv/create/$', login_required(views.EntryCreate.as_view())),
    path('cbv/create/', login_required(views.EntryCreate.as_view())),
    #url(r'^cbv/update/(?P<pk>\d+)/$', login_required(views.EntryUpdate.as_view())),
    path('cbv/update/<int:pk>)/', login_required(views.EntryUpdate.as_view())),
    #url(r'^cbv/delete$', views.EntryList.as_view()),
    path('cbv/delete', views.EntryList.as_view()),
]
