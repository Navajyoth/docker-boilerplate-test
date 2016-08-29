from django.db import models
from django.utils import timezone

from apps.clients.models import Client


class Feed(models.Model):

    client = models.ForeignKey(Client, related_name='feeds')
    message = models.CharField(max_length=512)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.client.name + ' --> ' + str(self.datetime)
