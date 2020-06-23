from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    boast = models.BooleanField(default=True)
    roast = models.BooleanField(default=True)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    submission = models.DateTimeField(timezone.now)