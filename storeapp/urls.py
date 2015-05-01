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
    url(r'^admin/login/$', views.adminLogin, name='admin_login'),
    url(r'^admin/logout/$', views.adminLogout),
    url(r'^admin/dashboard/$', views.adminDashBoard, name='admin_dash_board'),
)
