from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^sitemap\.xml$', 'apps.sitemap.views.SitemapXML'),
)
