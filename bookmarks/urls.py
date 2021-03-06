from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','links.views.index'),
    (r'^home/$', 'links.views.index'),
    (r'^view/(\d+)/up/$', 'links.views.view', {'up': 1}),
    (r'^category/([^/]+)/$', 'links.views.category'),
    (r'^current/(\d+)/$', 'links.views.current'),
    (r'^contact/$', 'links.views.contact'),
    (r'^contact/thanks/$', 'links.views.thanks'),
                       
    # Examples:
    # url(r'^$', 'bookmarks.views.home', name='home'),
    # url(r'^bookmarks/', include('bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))



#  (r'^category/([A-Za-z]+)/$', 'links.views.category'),
