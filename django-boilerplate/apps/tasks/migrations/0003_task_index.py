# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150417_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='index',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
