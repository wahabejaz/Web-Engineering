#!/usr/bin/env bash
set -euo pipefail

# Create necessary directories
echo "Creating required directories..."
mkdir -p staticfiles
mkdir -p static

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
python -m pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files with verbose output
echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity 2 --no-color

# Verify staticfiles directory
if [ -d "staticfiles" ]; then
    echo "✓ Static files collected successfully"
    ls -la staticfiles/ | head -20
else
    echo "⚠ Warning: staticfiles directory not found"
fi

echo "Build completed successfully!"
