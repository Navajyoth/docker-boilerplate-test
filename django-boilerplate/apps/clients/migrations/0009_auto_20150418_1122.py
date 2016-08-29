# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20150418_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.CharField(max_length=10),
        ),
    ]
