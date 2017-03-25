"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog.views import get_blogs, get_detail
from blog.views import mm
from blog.views import zs
from blog.views import toutiao
from blog.views import resume

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_blogs, name='blog_get_blogs'),
    url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
    url(r'^mm/$',mm),
    url(r'^zs/$',zs),
    url(r'^toutiao/$', toutiao),
    url(r'^resume/$', resume),
    #url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
]
