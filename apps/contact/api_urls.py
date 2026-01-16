from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router and register viewsets
router = DefaultRouter()
router.register(r'submissions', views.ContactSubmissionViewSet)
router.register(r'settings', views.ContactSettingsViewSet)

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),
    
    # Custom endpoints
    path('submit/', views.submit_contact_form, name='contact-submit'),
]