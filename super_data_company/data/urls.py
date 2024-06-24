from django.urls import path
from .views import FileUploadView, query_data

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload_file'),
    path('query/', query_data, name='query_data'),
]
