from django.conf.urls import patterns, url, include
from blog_app import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns("",
    url(r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'user_app/login.html',}),
)

