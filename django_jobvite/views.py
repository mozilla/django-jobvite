import json
import urllib

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound

from xml.etree import ElementTree


def test(request):
    uri = getattr(settings, 'JOBVITE_URI', None)
    if not uri:
        return HttpResponseNotFound()
    xml = urllib.urlopen(uri).read()
    et = ElementTree.fromstring(xml)
    jobs = dict([(job.find('id').text, job.find('title').text)
                 for job in et.findall('job')])
    content_type = settings.DEBUG and 'text/plain' or 'application/json'
    return HttpResponse(json.dumps(jobs), content_type=content_type)
