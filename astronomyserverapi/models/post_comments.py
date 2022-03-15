from django.db import models

class PostComments(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)