from django.db import models


class EventType(models.Model):
    event_type = models.CharField(max_length=50)