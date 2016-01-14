from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, admindocs

#import blog_app
import my_blog
admin.autodiscover()

urlpatterns = [

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^blog/', include('blog_app.urls')) ,
    url(r'^blog/', include('my_blog.urls')) ,
]

