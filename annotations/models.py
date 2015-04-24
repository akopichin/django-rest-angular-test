from django.db import models
from django.contrib.auth.models import User

import time

# Create your models here.

class Annotation(models.Model):
    user = models.ForeignKey(User, blank=True, null=False)
    start_time = models.IntegerField(blank=False, null=False, default=0)
    end_time = models.IntegerField(blank=False, null=False, default=0)
    text = models.TextField()

    def save(self, *args, **kwargs):
        super(Annotation, self).save(*args, **kwargs)

    class Meta:
        ordering = ('start_time',)
