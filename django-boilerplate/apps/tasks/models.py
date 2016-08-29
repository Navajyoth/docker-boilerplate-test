from django.db import models
from django.utils import timezone

# Create your models here.
from apps.clients.models import Client
from apps.exercises.models import Exercise


class Task(models.Model):

    client = models.ForeignKey(Client, related_name='tasks')
    date = models.DateField(default=timezone.now)
    count = models.PositiveSmallIntegerField(default=0)
    comment = models.CharField(max_length=256)
    exercise = models.ForeignKey(Exercise, related_name='tasks')
    index = models.PositiveSmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        task_list = self.client.tasks.filter(date=self.date)
        if len(task_list) > 1:
            self.index = len(task_list)
        else:
            self.index = 1
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        string = [
            str(self.index),
            self.client.name,
            self.exercise.name,
            str(self.date)
        ]
        return '-'.join(string)
