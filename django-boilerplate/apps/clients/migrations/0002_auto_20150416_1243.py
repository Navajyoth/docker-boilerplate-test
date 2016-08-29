# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='time_of_injury',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 43, 46, 777273, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='client',
            name='wake_up_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 43, 46, 777123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feed',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 43, 46, 778879, tzinfo=utc)),
        ),
    ]
