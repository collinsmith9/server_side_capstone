from django.db import models


class Event(models.Model):
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    seen_from = models.CharField(max_length=100)
    event_type = models.ForeignKey("eventType", on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    event_pic = models.ImageField(
        upload_to='eventimages', height_field=None,
        width_field=None, max_length=None, null=True)