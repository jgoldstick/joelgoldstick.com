from django.contrib import admin, admindocs
from django.urls import path, include
from . import views

admin.autodiscover()

urlpatterns = [

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', views.blog),
    path('blog/', include('blog_app.urls')),
]
