from django.http import JsonResponse
from django.views.generic.edit import FormView

from .forms import FileUploadForm
from .models import FileDataRecord, FileDataUpload
from .parser.constuctor import get_constructor


class FileUploadView(FormView):
    template_name = "upload.html"
    form_class = FileUploadForm
    success_url = "/data/upload/"  # Redirect to the same page after successful upload

    def form_valid(self, form):
        file = form.cleaned_data["file"]
        file_name = file.name

        try:
            parser = get_constructor(file_name)
            data = parser.parse(file)
        except ValueError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        upload = FileDataUpload.objects.create(file=file)
        for record in data:
            FileDataRecord.objects.create(
                upload=upload, data_type=file_name.split(".")[-1], data=record
            )

        return JsonResponse(
            {"status": "success", "message": "File uploaded successfully"}, status=201
        )

    def form_invalid(self, form):
        return JsonResponse(
            {
                "status": "error",
                "message": "Unable to upload file, please see errors",
                "errors": form.errors,
            },
            status=400,
        )


def query_data(request):
    data_type = request.GET.get("type")
    if data_type:
        records = FileDataRecord.objects.filter(data_type=data_type)
    else:
        records = FileDataRecord.objects.all()

    data = [
        {
            "data": record.data,
            "file_name": record.upload.file.name,
            "file_id": record.upload.id,
        }
        for record in records
    ]

    if not records.exists():
        return JsonResponse(
            {"status": "error", "message": "No matching records found"}, status=404
        )

    response_data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": data,
    }

    return JsonResponse(response_data, safe=False, status=200)
