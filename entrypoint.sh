#!/bin/sh

echo "Running migrations..."
python manage.py migrate --noinput

echo "Checking for superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

client_group, _ = Group.objects.get_or_create(name="Client")
lawyer_group, _ = Group.objects.get_or_create(name="Lawyer")

if not User.objects.filter(username="admin").exists():
    print("Creating superuser...")
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
else:
    print("Superuser already exists.")

if not User.objects.filter(username="client_user").exists():
    print("Creating client user...")
    client_user = User.objects.create_user(
        username="client_user", 
        first_name="John", 
        last_name="Doe",
        email="client@example.com",
        phone_number='90876543210',
        role="Client", 
        password="clientpassword"
        )
    client_user.groups.add(client_group)
    client_user.save()
else:
    print("Client user already exists.")

if not User.objects.filter(username="lawyer_user").exists():
    print("Creating lawyer user...")
    lawyer_user = User.objects.create_user(
        username="lawyer_user", 
        first_name="Jane", 
        last_name="Doe",
        email="lawyer@example.com",
        phone_number='10234567890',
        role="Lawyer",
        password="lawyerpassword"
    )
    lawyer_user.groups.add(lawyer_group)
    lawyer_user.save()
else:
    print("Lawyer user already exists.")

EOF

echo "Starting Gunicorn..."
exec "$@"
