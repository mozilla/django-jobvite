==============
django-jobvite
==============

django-jobvite is a `Django`_ application that provides a friendly interface to 
Jobvite.

.. _Django: http://www.djangoproject.com/

Not much here right now, just proofing the concept first. Stay tuned.

Installation
------------

To use ``django_jobvite`` to ``INSTALLED_APPS`` in ``settings.py``: ::

   INSTALLED_APPS = (
       ...
       'django_jobvite',
       ...
   )

Additionally, you'll need to specify the URI to the Jobvite XML file: ::

    JOBVITE_URI = 'http://www.jobvite.com/CompanyJobs/Xml.aspx?c=XXXXX'

License
-------
This software is licensed under the [MPL/GPL/LGPL tri-license][MPL]. For more
information, read the file ``LICENSE``.

[MPL]: http://www.mozilla.org/MPL/
