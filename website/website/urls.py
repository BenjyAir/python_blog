"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^detail/(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'^category/$', 'blog.views.category', name='category'),
    url(r'^tag/$', 'blog.views.tag', name='tag'),
    url(r'^archive/$', 'blog.views.archive', name='archive'),
    url(r'^reading/$', 'blog.views.reading', name='reading'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
]
