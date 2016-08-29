# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20150418_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='comments',
            new_name='medical_remarks',
        ),
    ]
