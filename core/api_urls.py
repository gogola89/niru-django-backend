from django.urls import path, include
from . import views

urlpatterns = [
    path('page-hero/<str:page_identifier>/', views.page_hero_detail, name='page-hero-detail'),
]