from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from analytics.views import AnalyticsView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', AnalyticsView.as_view(), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#static
#WARNING: dev only
if settings.DEV_STATIC:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                            url(r'', include('django.contrib.staticfiles.urls')),
                            )
