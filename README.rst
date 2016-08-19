==============
django-jobvite
==============

django-jobvite is a `Django`_ application that provides a friendly interface to
Jobvite.

.. note: 

As of Aug 2016 this app works fine with Jobvite but it's *no longer used or maintained* by Mozilla.

.. _Django: http://www.djangoproject.com/

Installation
------------
Fetch django-jobvite::

  pip install -e git://github.com/mozilla/django-jobvite

Add ``django_jobvite`` to ``INSTALLED_APPS`` in ``settings.py``: ::

   INSTALLED_APPS = (
       ...
       'django_jobvite',
       ...
   )

Configure ``urls.py``: ::

   urlpatterns = patterns('',
       (r'^jobvite/', include('django_jobvite.urls')),
       ...
   )

Additionally, you'll need to specify the URI to the Jobvite XML file: ::

    JOBVITE_URI = 'http://www.jobvite.com/CompanyJobs/Xml.aspx?c=XXXXX'

Use
---
Once installed and configured, you can query jobvite positions and obtain
results in JSON, keyed by jobvite ID. Any GET parameters will be used as
filter parameters. Example JSON: ::

    {
        'fxoOfv': {
            'title': 'Software Developer',
            'category': 'Engineering',
            'description': '...',
            'brief_description': '...',
            'job_type': 'Full-Time',
            'requisition_id': 1234,
            'apply_url': 'http://....',
            'detail_url': 'http://...',
            'location': 'Toronto, ON, Canada',
            'date': '4/21/2011'
        }
    }


Database Migrations
-------------------
django_jobvite supports both South and Django 1.7+ migrations. Support for South will end when Django 1.4 reaches its end of life, around October 2015.



License
-------
This software is licensed under the BSD License. For more
information, read the file ``LICENSE``.
