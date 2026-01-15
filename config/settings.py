"""
Main settings file that delegates to environment-specific settings
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Determine which settings module to use based on environment variable
ENVIRONMENT = os.getenv('DJANGO_ENV', 'dev')  # Default to development

if ENVIRONMENT == 'prod':
    from .settings.prod import *
elif ENVIRONMENT == 'staging':
    from .settings.staging import *
else:
    from .settings.dev import *
