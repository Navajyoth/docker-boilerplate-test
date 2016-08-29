# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('mobile', models.CharField(blank=True, max_length=64, null=True, validators=[django.core.validators.RegexValidator(b'^\\d{10}$', 'Enter a valid phone number.', b'invalid')])),
                ('gender', models.PositiveSmallIntegerField(default=0, verbose_name=b'Gender', choices=[(0, b'--'), (1, b'Male'), (2, b'Female'), (3, b'Other')])),
                ('dob', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'TRAINING SINCE')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo', models.FileField(upload_to=b'images/trainers', blank=True)),
                ('monthly_rate', models.PositiveSmallIntegerField(blank=True)),
                ('month_rate_3', models.PositiveSmallIntegerField(blank=True)),
                ('month_rate_6', models.PositiveSmallIntegerField(blank=True)),
                ('month_rate_12', models.PositiveSmallIntegerField(blank=True)),
                ('user', models.OneToOneField(related_name='trainer_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
