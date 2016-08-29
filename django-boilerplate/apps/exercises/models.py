from django.db import models

# Create your models here.


class Exercise(models.Model):

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    video = models.FileField(
        upload_to='exercises/videos', null=True, blank=True)
    picture = models.FileField(
        upload_to='exercises/images', null=True, blank=True)
    song = models.FileField(upload_to='exercises/songs', null=True, blank=True)

    def __str__(self):
        return self.name
