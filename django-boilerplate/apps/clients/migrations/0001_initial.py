# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
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
                ('photo', models.FileField(upload_to=b'images/clients', blank=True)),
                ('height', models.CharField(max_length=7)),
                ('weight', models.CharField(max_length=7)),
                ('bloodtype', models.CharField(max_length=5)),
                ('occupation', models.CharField(max_length=30)),
                ('goal_weight', models.CharField(max_length=7)),
                ('goal_achieved', models.BooleanField(default=False)),
                ('wake_up_time', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 42, 53, 899967, tzinfo=utc))),
                ('bed_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sit_more_than_30hrs_per_week', models.BooleanField(default=False)),
                ('constant_back_pain', models.BooleanField(default=False)),
                ('currently_pregnant', models.BooleanField(default=False)),
                ('weekly_workout_schedule', models.CharField(max_length=25)),
                ('time_of_injury', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 42, 53, 900110, tzinfo=utc))),
                ('comments', models.CharField(max_length=512)),
                ('trainer', models.ForeignKey(related_name='clients', to='trainers.Trainer')),
                ('user', models.OneToOneField(related_name='client_profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=512)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 12, 42, 53, 901753, tzinfo=utc))),
                ('client', models.ForeignKey(related_name='feeds', to='clients.Client')),
            ],
        ),
    ]
