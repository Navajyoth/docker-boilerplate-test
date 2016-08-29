# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_remove_client_bloodtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='bloodtype',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'blood group', choices=[(0, b'--'), (1, b'A+'), (2, b'B+'), (3, b'AB+'), (4, b'O+'), (5, b'A-'), (6, b'B-'), (7, b'AB-'), (8, b'O-'), (9, b'Others')]),
        ),
    ]
