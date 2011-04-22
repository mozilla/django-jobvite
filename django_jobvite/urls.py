from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^positions/(?P<job_id>[\w]+)/$', 'django_jobvite.views.position',
        name='django_jobvite_position'),
    url(r'^positions/$', 'django_jobvite.views.positions',
        name='django_jobvite_positions'),
)
