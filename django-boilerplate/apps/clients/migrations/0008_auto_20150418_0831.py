# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_client_bloodtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='client',
        ),
        migrations.DeleteModel(
            name='Feed',
        ),
    ]
