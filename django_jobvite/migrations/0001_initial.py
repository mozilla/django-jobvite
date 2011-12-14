# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('django_jobvite_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('django_jobvite', ['Category'])

        # Adding model 'Position'
        db.create_table('django_jobvite_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('requisition_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_jobvite.Category'], null=True, blank=True)),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('detail_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('apply_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('brief_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('django_jobvite', ['Position'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('django_jobvite_category')

        # Deleting model 'Position'
        db.delete_table('django_jobvite_position')


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
            'requisition_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_jobvite']
