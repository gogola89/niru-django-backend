from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router and register viewsets
router = DefaultRouter()
router.register(r'categories', views.NewsCategoryViewSet)
router.register(r'articles', views.NewsArticleViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'issues', views.NewsletterIssueViewSet)
router.register(r'contact-submissions', views.ContactSubmissionViewSet)
router.register(r'contact-settings', views.ContactSettingsViewSet)

urlpatterns = [
    # Include all router-generated URLs
    path('', include(router.urls)),

    # Custom endpoints
    path('newsletter/subscribe/', views.subscribe_newsletter, name='newsletter-subscribe'),
    path('contact/submit/', views.submit_contact_form, name='contact-submit'),
]