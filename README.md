# Django Portfolio Website

A responsive Django portfolio website built with Django 5.2 and Jazzmin admin styling. This project showcases personal profile, projects, and contact functionality, and is configured for local development as well as production deployment with WhiteNoise and Gunicorn.

## Features

- Home page with project listings and introductory content
- Project detail page for each portfolio item
- Search results page for project discovery
- About page and contact functionality
- Media file support for profile images, project images, and resume uploads
- Jazzmin-powered admin dashboard for easy management
- Static asset handling via WhiteNoise
- SQLite default development database with optional MySQL/PostgreSQL support

## Technology Stack

- Python
- Django 5.2
- Django Jazzmin
- WhiteNoise
- Gunicorn
- Pillow
- PyMySQL / psycopg2-binary

## Repository Structure

- `core/` - main Django app containing models, views, URLs, and templates
- `portfolio/` - Django project configuration, settings, and URL routing
- `templates/` - global templates used by the site
- `static/` - CSS, JavaScript, and image assets
- `media/` - uploaded media files for profile and projects
- `requirements.txt` - Python dependencies

## Getting Started

### Prerequisites

- Python 3.11+ (recommended)
- pip
- virtualenv or equivalent environment manager

### Installation

1. Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd "Web Engineering/portfolio"
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows Command Prompt
venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Environment Configuration

This project reads several variables from the environment:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_DB_ENGINE`
- `DJANGO_DB_NAME`
- `DJANGO_DB_USER`
- `DJANGO_DB_PASSWORD`
- `DJANGO_DB_HOST`
- `DJANGO_DB_PORT`
- `DJANGO_LOG_LEVEL`

For production, set `DJANGO_DEBUG` to `False` and configure your database engine/credentials accordingly.

## Deployment

This project includes configuration for deployment targets using:

- `build.sh`
- `start.sh`
- `Procfile`
- `render.yaml`

WhiteNoise is already configured for static file serving in production.

## Admin Panel

Access the Django admin at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser account created during setup to manage projects, profile content, and site data.

## Notes

- Media files are served from `/media/` during development.
- Static files are collected into `staticfiles/` for production use.
- The project is configured to use SQLite by default but supports MySQL/PostgreSQL through environment variables.

## License

This repository does not include a license file. Add a `LICENSE` if you want to publish or share this project publicly.
