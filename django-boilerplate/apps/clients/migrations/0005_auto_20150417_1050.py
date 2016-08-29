# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20150417_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bed_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='wake_up_time',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
