from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^v2/', include('pagseguro.api.urls')),
)
