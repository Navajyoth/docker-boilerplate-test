# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20150418_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='weight',
            field=models.CharField(max_length=10),
        ),
    ]
