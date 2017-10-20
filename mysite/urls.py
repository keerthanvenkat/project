from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')), 
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^address/',include('address.urls')), # address app
    #url(r'^hello', 'blog.views.hello_world', name='hello'),
    #url(r'^test/', 'blog.views.test_html', name='testhello'),
    #url(r'^address/','blog.views.address',name='addresss'),
    #url(r'^address1/','blog.views.address1',name='address1'),

]
if settings.DEBUG:  # when DEBUG is set to TRUE
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns