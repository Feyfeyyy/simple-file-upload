from django.db import models


class FileDataUpload(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="upload/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "File Data Upload"
        verbose_name_plural = "File Data Uploads"

    def __str__(self):
        return self.file.name


class FileDataRecord(models.Model):
    id = models.AutoField(primary_key=True)
    upload = models.ForeignKey(FileDataUpload, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50)
    data = models.JSONField()

    class Meta:
        verbose_name = "File Data Record"
        verbose_name_plural = "File Data Records"

    def __str__(self):
        return self.data_type
