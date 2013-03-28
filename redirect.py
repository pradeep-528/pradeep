from django.conf.urls.defaults import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^some-url/$', RedirectView.as_view(url='/redirect-url/'), name='some_redirect'),
)
