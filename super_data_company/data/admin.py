from django.contrib import admin

from .models import FileDataRecord, FileDataUpload

admin.site.register(FileDataUpload)
admin.site.register(FileDataRecord)
