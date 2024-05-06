from django.db import models

class TimelineEvent(models.Model):
    year = models.IntegerField()
    description = models.TextField()