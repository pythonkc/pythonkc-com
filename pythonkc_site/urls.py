from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.views.decorators.cache import cache_page
from pythonkc_site.views import PythonKCComingSoon
from pythonkc_site.views import PythonKCHome

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^/?$', cache_page(60*60*24)(PythonKCComingSoon.as_view())),
    url(r'^demo/?$', cache_page(60 * 5)(PythonKCHome.as_view())),

    # Examples:
    # url(r'^$', 'pythonkc_site.views.home', name='home'),
    # url(r'^pythonkc_site/', include('pythonkc_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


