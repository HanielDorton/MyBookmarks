from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','links.views.index'),
    (r'^home/$', 'links.views.index'),
    (r'^view/(\d+)/up/$', 'links.views.view', {'up': 1}),
    (r'^category/([A-Za-z]+)/$', 'links.views.category'),
    (r'^current/(\d+)/', 'links.views.current'),
    # Examples:
    # url(r'^$', 'bookmarks.views.home', name='home'),
    # url(r'^bookmarks/', include('bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
