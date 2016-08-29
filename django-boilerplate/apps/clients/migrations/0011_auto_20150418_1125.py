# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20150418_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='goal_weight',
            field=models.CharField(max_length=10),
        ),
    ]
