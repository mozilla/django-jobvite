try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
    
urlpatterns = patterns('',
    url(r'^positions/$', 'django_jobvite.views.positions',
        name='django_jobvite_positions'),
    url(r'^positions/(?P<job_id>[\w]+)/$', 'django_jobvite.views.positions',
        name='django_jobvite_positions'),
    url(r'^categories/$', 'django_jobvite.views.categories',
        name='django_jobvite_categories'),
    url(r'^categories/(?P<category_id>[\w-]+)/$',
        'django_jobvite.views.categories',
        name='django_jobvite_categories'),
)
