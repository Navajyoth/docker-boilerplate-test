# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20150416_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comments',
            field=models.CharField(max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.FileField(null=True, upload_to=b'images/clients', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='weekly_workout_schedule',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
