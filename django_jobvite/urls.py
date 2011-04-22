from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^positions/$', 'django_jobvite.views.positions',
        name='django_jobvite_positions'),
)
