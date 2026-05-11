#!/usr/bin/env bash
set -euo pipefail

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
python -m pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --verbosity 2

echo "Build completed successfully!"
