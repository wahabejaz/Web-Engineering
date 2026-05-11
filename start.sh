#!/usr/bin/env bash
set -euo pipefail

echo "Starting Django application..."

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Ensuring superuser exists..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@portfolio.com', 'admin123')
    print("Superuser 'admin' created.")
else:
    print("Superuser 'admin' already exists.")
END

echo "Starting gunicorn..."
# Start gunicorn
gunicorn portfolio.wsgi --workers 1 --bind 0.0.0.0:$PORT --timeout 120 --access-logfile - --error-logfile -
