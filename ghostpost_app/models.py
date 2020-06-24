from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    is_boast = models.BooleanField(default=True, blank=True)
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission = models.DateTimeField(default=timezone.now)

    @property
    def total_votes(self):
        return self.up_votes - self.down_votes

    def __str__(self):
        return self.post