from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    ad_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    views = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title
