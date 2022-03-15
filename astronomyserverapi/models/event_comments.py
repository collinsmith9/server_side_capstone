from django.db import models

class EventComments(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
