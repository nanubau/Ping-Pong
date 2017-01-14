from django.conf.urls import patterns, url

urlpatterns = patterns('refree.views',
    url(r'^$', 'register', name='register'),
    url(r'^register/$', 'register', name='register'),     #Registration API
)