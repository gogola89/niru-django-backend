from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router and register viewsets
router = DefaultRouter()
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'issues', views.NewsletterIssueViewSet)

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),
    
    # Custom endpoints
    path('subscribe/', views.subscribe_newsletter, name='newsletter-subscribe'),
]