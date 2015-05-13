# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Position.location_filter'
        db.add_column('django_jobvite_position', 'location_filter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Position.location_filter'
        db.delete_column('django_jobvite_position', 'location_filter')


    models = {
        'django_jobvite.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'django_jobvite.position': {
            'Meta': {'object_name': 'Position'},
            'apply_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'brief_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_jobvite.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'location_filter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'requisition_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_jobvite']