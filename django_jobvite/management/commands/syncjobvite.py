import urllib2
from xml.etree import ElementTree

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from django_jobvite.models import Position

# map jobvite XML element names to field names used in model.
field_map = {
    'id': 'job_id', 'title': 'title', 'requisitionid': 'requisition_id',
    'category': 'category', 'jobtype': 'job_type', 'location': 'location',
    'date': 'date', 'detail-url': 'detail_url', 'apply-url': 'apply_url',
    'description': 'description', 'briefdescription': 'brief_description',
}


class Command(BaseCommand):
    help = 'Fetch job listings from Jobvite'

    def _get_jobvite_xml(self):
        """Fetch XML from Jobvite."""
        uri = getattr(settings, 'JOBVITE_URI', None)
        if not uri:
            raise CommandError('No Jobvite URI set')
        content = urllib2.urlopen(uri).read()
        return content

    def _parse_jobvite_xml(self, content):
        """Given XML as a string, return a dictionary keyed on job id."""
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

    def _remove_deleted_positions(self, job_ids):
        """
        Delete positions that are not in the list ``job_ids``.
        Returns the number deleted.
        """
        if len(job_ids) == 0:
            # something must be wrong if we get ZERO jobs.
            # Let's not wipe the db in case its bad data.
            return 0
        positions = Position.objects.exclude(job_id__in=job_ids)
        deleted = len(positions)
        positions.delete()
        return deleted

    def handle(self, *args, **options):
        """
        Sync positions in Jobvite. Updates existing positions, creates new ones
        if necessary and deletes expired or removed positions.
        """
        content = self._get_jobvite_xml()
        parsed = self._parse_jobvite_xml(content)
        stats = dict(added=0, deleted=0)
        for job_id, fields in parsed.iteritems():
            try:
                position = Position.objects.get(job_id=job_id)
            except Position.DoesNotExist:
                position = Position(job_id=job_id)
                stats['added'] += 1
            for k, v in fields.iteritems():
                setattr(position, k, v)
            position.save()
        job_ids = parsed.keys()
        stats['deleted'] = self._remove_deleted_positions(job_ids)
        print "Synced: %d" % (len(job_ids),)
        print "Added: %d" % (stats['added'],)
        print "Removed: %d" % (stats['deleted'],)
