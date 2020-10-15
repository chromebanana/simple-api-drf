from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=500, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.url)