from django.db import models

from apps.account.base import UserProfileBase
from apps.trainers.models import Trainer
from django.utils import timezone


BLOOD_GRP = (
    (0, "--"),
    (1, "A+"),
    (2, "B+"),
    (3, "AB+"),
    (4, "O+"),
    (5, "A-"),
    (6, "B-"),
    (7, "AB-"),
    (8, "O-"),
    (9, "Others"),
)


class Client(UserProfileBase):
    photo = models.FileField(upload_to='images/clients', null=True, blank=True)
    trainer = models.ForeignKey(Trainer, related_name='clients')
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    bloodtype = models.PositiveSmallIntegerField(
        choices=BLOOD_GRP, default=0, verbose_name="blood group")
    occupation = models.CharField(max_length=30)
    goal_weight = models.CharField(max_length=10)
    goal_achieved = models.BooleanField(default=False)
    wake_up_time = models.DateTimeField(default=timezone.now, blank=True)
    bed_time = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    sit_more_than_30hrs_per_week = models.BooleanField(default=False)
    constant_back_pain = models.BooleanField(default=False)
    currently_pregnant = models.BooleanField(default=False)
    weekly_workout_schedule = models.CharField(max_length=25, blank=True)
    time_of_injury = models.DateTimeField(default=timezone.now)
    medical_remarks = models.CharField(max_length=512, blank=True)

    @property
    def blood_type(self):
        num, text = BLOOD_GRP[self.bloodtype]
        return text

    def __str__(self):
        return self.email


