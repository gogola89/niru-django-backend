from django.urls import path
from . import views

app_name = 'about_api'

urlpatterns = [
    # About page
    path('about/', views.AboutPageDetailView.as_view(), name='about-detail'),
    
    # Core values
    path('core-values/', views.CoreValueListView.as_view(), name='core-values-list'),
    
    # VC message
    path('vc-message/', views.ViceChancellorMessageDetailView.as_view(), name='vc-message-detail'),
    
    # Combined endpoint
    path('about-full/', views.about_page_with_relations, name='about-full'),
]