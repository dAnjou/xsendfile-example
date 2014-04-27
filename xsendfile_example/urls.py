from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', 'xsendfile_example.views.serve_file', name='serve_file'),
)
