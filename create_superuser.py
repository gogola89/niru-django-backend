import os
import django
from django.contrib.auth import get_user_model

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

# Setup Django
django.setup()

# Create superuser
User = get_user_model()
username = 'admin'
email = 'admin@niru.ac.ke'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser "{username}" created successfully!')
else:
    print(f'Superuser "{username}" already exists.')