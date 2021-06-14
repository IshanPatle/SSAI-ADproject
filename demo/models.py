from django.db import models

# Create your models here.

class Task(models.Model):
    video_url = models.CharField(max_length=200)
    ad_url1 = models.CharField(max_length=200, null=True)
    ad_insertPoints1 = models.IntegerField(default=None, null=True)

    ad_url2 = models.CharField(max_length=200, null=True)
    ad_insertPoints2 = models.IntegerField(default=None, null=True)
    final_video = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

