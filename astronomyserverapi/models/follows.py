from django.db import models
from datetime import datetime


class Follow(models.Model):
    follower = models.ForeignKey("siteUser", on_delete=models.CASCADE, related_name="person_follower")
    person_followed = models.ForeignKey("siteUser", on_delete=models.CASCADE)