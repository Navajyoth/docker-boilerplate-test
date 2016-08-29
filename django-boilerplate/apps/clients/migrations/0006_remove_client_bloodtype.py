# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20150417_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='bloodtype',
        ),
    ]
