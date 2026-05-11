#!/usr/bin/env bash
set -euo pipefail

echo "=========================================="
echo "Starting Django Portfolio Application"
echo "=========================================="

# Create required directories
echo "[1/5] Creating required directories..."
mkdir -p staticfiles media
mkdir -p static

# Run migrations
echo "[2/5] Running database migrations..."
python manage.py migrate --noinput

# Collect static files at runtime for extra safety
echo "[3/5] Collecting static files..."
python manage.py collectstatic --noinput --verbosity 1

# Verify staticfiles directory exists and has content
echo "[4/5] Verifying static files..."
if [ -d "staticfiles" ]; then
    COUNT=$(find staticfiles -type f | wc -l)
    echo "✓ Found $COUNT static files in staticfiles/"
else
    echo "⚠ Warning: staticfiles directory not found"
fi

# Create superuser if it doesn't exist
echo "[5/5] Ensuring superuser exists..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@portfolio.com', 'admin123')
    print("✓ Superuser 'admin' created")
else:
    print("✓ Superuser 'admin' already exists")
END

echo "=========================================="
echo "Starting gunicorn on port $PORT"
echo "=========================================="

# Start gunicorn with explicit static file serving
exec gunicorn portfolio.wsgi \
    --workers 1 \
    --bind 0.0.0.0:$PORT \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level debug
