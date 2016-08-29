# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20150416_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='time_of_injury',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='client',
            name='wake_up_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feed',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
