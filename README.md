# NIRU Backend API

Django REST API backend for National Intelligence and Research University (NIRU) website.

## Setup Instructions

### 1. Virtual Environment
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Copy `.env.example` to `.env` and update values:
```bash
cp .env.example .env
```

### 4. Database Setup
```bash
# Run migrations
python manage.py migrate

# Seed initial data
python manage.py seed_data
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

## Project Structure
```
niru-backend/
├── config/                 # Project configuration
│   ├── settings/
│   │   ├── base.py        # Base settings
│   │   ├── dev.py         # Development settings
│   │   ├── staging.py     # Staging settings
│   │   └── prod.py        # Production settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                  # Core app with shared functionality
│   ├── models.py          # Base models, SiteSettings, PageHero
│   ├── views.py           # API views
│   ├── serializers.py     # API serializers
│   ├── api_urls.py        # API URL patterns
│   └── management/        # Management commands
├── static/                # Static files
├── media/                 # User uploads
├── fixtures/              # Data fixtures
├── docs/                  # Documentation
├── manage.py
├── .env                   # Environment variables (gitignored)
├── .env.example           # Environment template
└── requirements.txt
```

## API Endpoints

### Core API
- `GET /api/v1/page-hero/{page_identifier}/` - Get page hero information

## Development

The project uses `config.settings.dev` for development and `config.settings.prod` for production.

## Management Commands

- `python manage.py seed_data` - Seed the database with initial data

## Branching Strategy

- `main` - Production-ready code
- `staging` - Pre-production testing
- `dev` - Development branch
- Feature branches - Individual features/fixes

## Next Steps

See ROADMAP.md for the development plan. Currently on Sprint 1.