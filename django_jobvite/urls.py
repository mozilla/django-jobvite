from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^test/', 'django_jobvite.views.test', name='jobvite_test'),
)
