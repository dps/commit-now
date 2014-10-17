# This file defines the URL schema for the site.

from django.conf.urls import patterns, url

from commit import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^commit$', views.commit, name='commit'),
	url(r'^savecommit$', views.savecommit, name='savecommit'),
)
