import os
import django
from django.test import RequestFactory
from django.conf import settings

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

# Setup Django
django.setup()

# Test the API endpoint
from core.views import page_hero_detail
from core.models import PageHero
from django.contrib.auth.models import User

# Create a test request factory
factory = RequestFactory()

# Create a test PageHero object
test_hero = PageHero.objects.create(
    page_identifier='home',
    title='National Intelligence and Research University',
    subtitle='Premier Science and Research-Intensive African University',
    background_image='heroes/test-home-hero.jpg',  # This won't actually exist but is fine for testing
    overlay_opacity=50,
    is_active=True
)

print(f"Created test PageHero: {test_hero}")

# Test the API endpoint
request = factory.get('/api/v1/page-hero/home/')
request.user = User.objects.first()  # Get the first user (the admin we created)

# Call the API view function
response = page_hero_detail(request, 'home')
print(f"API Response Status: {response.status_code}")
print(f"API Response Data: {response.data}")

# Clean up
test_hero.delete()
print("Test completed successfully!")