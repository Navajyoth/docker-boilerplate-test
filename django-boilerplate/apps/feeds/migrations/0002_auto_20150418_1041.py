# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='date',
        ),
        migrations.AddField(
            model_name='feed',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
