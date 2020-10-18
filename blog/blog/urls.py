from django.contrib import admin, admindocs
from django.urls import path, include
from . import views

admin.autodiscover()

urlpatterns = [

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #path('admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    #url(r'^$', views.blog),
    path('', views.blog),
    #url(r'^blog/', include('blog_app.urls')),
    path('blog/', include('blog_app.urls')),
    # url(r'^blog/', include('my_blog.urls')) ,
]
