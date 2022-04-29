from django.db import models
from django.utils import timezone


class TheFolder(models.Model):
    folder_name = models.CharField(max_length=255, null=True)
    parent_folder = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name='sub_folders')

    def __str__(self):
        return self.folder_name


class TheFile(models.Model):
    filename = models.CharField(max_length=255, null=True)
    file = models.FileField(null=True, max_length=255, upload_to='uploads/')
    parent_folder = models.ForeignKey(TheFolder, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now)
