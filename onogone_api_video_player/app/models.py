from django.conf import settings
from django.db import models
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver
from .helpers.VideoHelper import VideoHelper


# Create your models here.
class Video(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    file_1080p = models.CharField(max_length=255, null=True)
    file_720p = models.CharField(max_length=255, null=True)
    file_watermark = models.CharField(max_length=255, null=True)

    def upload_video_dir(self, filename):
        path = '{}/{}'.format(self.key, "video_original.mp4")
        return path
    file = models.FileField(upload_to=upload_video_dir)


@receiver(post_save, sender=Video)
def post_upload_video(sender, instance, created, **kwargs):
    path = settings.MEDIA_ROOT + '/'
    input = str(instance.file)
    if_modified = False

    if instance.file_watermark is None:
        output = str(instance.key) + "/video.mp4"
        VideoHelper.convert(path + input, path + output)
        instance.file_watermark = output
        if_modified = True

    if instance.file_1080p is None:
        output = str(instance.key) + "/video_1080_p.mp4"
        VideoHelper.convert(path + input, path + output, 1920, 1080)
        instance.file_1080p = output
        if_modified = True

    if instance.file_720p is None:
        output = str(instance.key) + "/video_720_p.mp4"
        VideoHelper.convert(path + input, path + output, 1280, 720)
        instance.file_720p = output
        if_modified = True

    if if_modified is True:
        instance.save()
