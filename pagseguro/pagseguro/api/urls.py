from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^checkout$', 'pagseguro.api.views.checkout', name='checkout'),
)
