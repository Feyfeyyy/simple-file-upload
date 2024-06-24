#!/bin/sh

# Apply database migrations
poetry run python super_data_company/manage.py makemigrations
poetry run python super_data_company/manage.py migrate

# Create superuser if it doesn't exist
if [ ! -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
  poetry run python super_data_company/manage.py shell <<EOF
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '$DJANGO_SUPERUSER_PASSWORD')
EOF
fi

# Start server
poetry run python super_data_company/manage.py runserver 0.0.0.0:8000
