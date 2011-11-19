# -*- coding: utf-8 -*-


from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('',
    url(r'^/?$', 'pythonkc_site.views.home', name='home'),
    url(r'^meetups/past/?$', 'pythonkc_site.views.past_meetups', 
        name='past-meetups'),
)
