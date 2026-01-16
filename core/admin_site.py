from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class NIRUAdminSite(AdminSite):
    site_header = 'NIRU Administration'
    site_title = 'NIRU Admin Portal'
    index_title = 'Welcome to NIRU Admin Portal'
    site_url = '/'


# Create an instance of the custom admin site
niru_admin = NIRUAdminSite(name='niru_admin')

# Unregister the default admin and register our custom one
# This will be done in the apps.py or urls.py