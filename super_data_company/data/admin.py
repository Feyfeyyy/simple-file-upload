from django.contrib import admin

from .models import FileDataRecord, FileDataUpload


@admin.register(FileDataRecord)
class FileDataRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "data_type", "data")
    list_filter = ("data_type",)
    search_fields = ("upload", "data_type")


@admin.register(FileDataUpload)
class FileDataUploadAdmin(admin.ModelAdmin):
    list_display = ("id", "short_url", "uploaded_at")
    list_filter = ("uploaded_at",)

    # TODO: This is a hack to get the file URL to display in the admin
    #  Ideally, we should use a custom widget for the file field
    #  Need to create logic to shorten the URL
    def short_url(self, obj):
        return obj.file.url

    short_url.short_description = "File URL"
