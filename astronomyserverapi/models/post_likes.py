from django.db import models


class PostLikes(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)