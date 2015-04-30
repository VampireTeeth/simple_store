from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.catalog, name='catalog'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^cart/remove/$', views.removeFromCart),
    url(r'^cart/checkout/$', views.checkout),
    url(r'^cart/checkout/complete/$', views.completeOrder),
)
