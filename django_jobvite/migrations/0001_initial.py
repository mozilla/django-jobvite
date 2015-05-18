# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_id', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=100)),
                ('requisition_id', models.PositiveIntegerField()),
                ('job_type', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=150, null=True, blank=True)),
                ('date', models.CharField(max_length=100)),
                ('detail_url', models.URLField()),
                ('apply_url', models.URLField()),
                ('description', models.TextField()),
                ('brief_description', models.TextField(null=True, blank=True)),
                ('location_filter', models.CharField(default=b'', max_length=255, blank=True)),
                ('category', models.ForeignKey(blank=True, to='django_jobvite.Category', null=True)),
            ],
        ),
    ]
