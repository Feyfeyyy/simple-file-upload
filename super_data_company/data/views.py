import csv
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import FormView
from .forms import FileUploadForm
from .models import FileDataUpload, FileDataRecord


class FileUploadView(FormView):
    template_name = 'upload.html'
    form_class = FileUploadForm
    success_url = '/data/upload/'  # Redirect to the same page after successful upload

    def form_valid(self, form):
        file = form.cleaned_data['file']

        if file.name.endswith('.csv'):
            data_type = 'csv'
            data = list(csv.DictReader(file.read().decode('utf-8').splitlines()))
        elif file.name.endswith('.json'):
            data_type = 'json'
            data = json.load(file)
        else:
            return JsonResponse({'status': 'error', 'message': 'Unsupported file type'}, status=400)

        upload = FileDataUpload.objects.create(file=file)
        for record in data:
            FileDataRecord.objects.create(upload=upload, data_type=data_type, data=record)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully'}, status=201)

    def form_invalid(self, form):
        return JsonResponse(
            {'status': 'error', 'message': 'Unable to upload file, please see errors', 'errors': form.errors},
            status=400)


def query_data(request):
    data_type = request.GET.get('type')
    if data_type:
        records = FileDataRecord.objects.filter(data_type=data_type)
    else:
        records = FileDataRecord.objects.all()

    data = [{'data': record.data,
             'file_name': record.upload.file.name,
             'file_id': record.upload.id} for record in records]

    if not records.exists():
        return JsonResponse({
            'status': 'error',
            'message': 'No matching records found'
        }, status=404)

    response_data = {
        'status': 'success',
        'message': 'Data retrieved successfully',
        'data': data
    }

    return JsonResponse(response_data, safe=False, status=200)
