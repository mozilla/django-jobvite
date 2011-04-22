import urllib2
from xml.etree import ElementTree

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from django_jobvite.models import Position


field_map = {
    'id': 'job_id', 'title': 'title', 'requisitionid': 'requisition_id',
    'category': 'category', 'jobtype': 'job_type', 'location': 'location',
    'date': 'date', 'detail-url': 'detail_url', 'apply-url': 'apply_url',
    'description': 'description', 'briefdescription': 'brief_description',
}


class Command(BaseCommand):
    help = 'Fetch job listings from Jobvite'

    def _get_jobvite_xml(self):
        uri = getattr(settings, 'JOBVITE_URI', None)
        if not uri:
            raise CommandError('No Jobvite URI set')
        content = urllib2.urlopen(uri).read()
        return content

    def _parse_jobvite_xml(self, content):
        jobs = {}
        et = ElementTree.fromstring(content)
        job_elements = et.findall('job')
        for element in job_elements:
            job_id = element.find('id').text
            jobs[job_id] = {}
            for element_name, field_name in field_map.iteritems():
                value = element.find(element_name).text
                jobs[job_id][field_name] = value
        return jobs

    def handle(self, *args, **options):
        content = self._get_jobvite_xml()
        parsed = self._parse_jobvite_xml(content)
        for job_id, fields in parsed.iteritems():
            position, created = Position.objects.get_or_create(job_id=job_id)
            for k, v in fields.iteritems():
                setattr(position, k, v)
            position.save()
        print "Synced %d jobs" % (len(parsed.keys()),)
