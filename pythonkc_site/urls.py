# -*- coding: utf-8 -*-


from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.decorators.cache import cache_page
from pythonkc_site.views import PythonKCHome

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', cache_page(60 * 5)(PythonKCHome.as_view()), name='home'),

    # Examples:
    # url(r'^$', 'pythonkc_site.views.home', name='home'),
    # url(r'^pythonkc_site/', include('pythonkc_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


