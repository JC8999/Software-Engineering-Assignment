#!/bin/sh

echo "Running migrations..."
python manage.py migrate --noinput

echo "Checking for superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    print("Creating superuser...")
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
else:
    print("Superuser already exists.")
EOF

echo "Starting server..."
exec "$@"
