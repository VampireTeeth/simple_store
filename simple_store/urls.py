from django.conf.urls import patterns, include, url
from storeapp import urls as store_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^store/', include(store_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
