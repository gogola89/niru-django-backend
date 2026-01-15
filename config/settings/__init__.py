"""
Main settings file that delegates to environment-specific settings
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from decouple import config, Csv

# Load environment variables from .env file
# The .env file should be in the project root (one level up from this directory)
project_root = Path(__file__).resolve().parent.parent
dotenv_path = project_root / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)
else:
    # Try to load from current working directory as fallback
    load_dotenv()

# Determine which settings module to use based on environment variable
ENVIRONMENT = config('DJANGO_ENV', default='dev')

if ENVIRONMENT == 'prod':
    from .prod import *
elif ENVIRONMENT == 'staging':
    from .staging import *
else:
    from .dev import *