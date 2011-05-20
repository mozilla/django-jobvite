from django.db import models


class Position(models.Model):
    job_id = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=100)
    requisition_id = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    job_type = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    date = models.CharField(max_length=100)
    detail_url = models.URLField()
    apply_url = models.URLField()
    description = models.TextField()
    brief_description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s" % (self.job_id, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('django_jobvite_position', (), {
            'job_id': self.job_id,
        })

    def to_dict(self):
        """Return the model as a dictionary keyed on ``job_id``."""
        fields = self._meta.fields
        position_dict = {self.job_id: {}}
        for field in fields:
            if field.primary_key:
                continue
            if field.name == 'job_id':
                continue
            position_dict[self.job_id][field.name] = getattr(self, field.name)
        return position_dict
