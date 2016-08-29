# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20150418_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=512)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(related_name='feeds', to='clients.Client')),
            ],
        ),
    ]
