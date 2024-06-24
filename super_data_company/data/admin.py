from django.contrib import admin

from .models import FileDataRecord, FileDataUpload


@admin.register(FileDataRecord)
class FileDataRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_type', 'data')
    list_filter = ('data_type',)
    search_fields = ('upload', 'data_type')


@admin.register(FileDataUpload)
class FileDataUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'uploaded_at')
    list_filter = ('uploaded_at',)

    def short_url(self, obj):
        return obj.file.url

    short_url.short_description = 'File URL'
