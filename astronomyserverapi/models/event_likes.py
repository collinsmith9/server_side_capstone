from django.db import models


class EventLikes(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)