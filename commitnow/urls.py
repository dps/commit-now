from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'', include('commit.urls', namespace='commit')),
    url(r'^admin/', include(admin.site.urls)),
)
