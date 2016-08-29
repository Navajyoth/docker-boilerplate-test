# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('video', models.FileField(null=True, upload_to=b'exercises/videos', blank=True)),
                ('picture', models.FileField(null=True, upload_to=b'exercises/images', blank=True)),
                ('song', models.FileField(null=True, upload_to=b'exercises/songs', blank=True)),
            ],
        ),
    ]
