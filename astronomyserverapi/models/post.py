from django.db import models


class Post(models.Model):
    user = models.ForeignKey("siteUser", on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    categories = models.ManyToManyField("Category", through="PostCategories", related_name="thepostcategories")
    post_pic = models.ImageField(
        upload_to='postimages', height_field=None,
        width_field=None, max_length=None, null=True)


