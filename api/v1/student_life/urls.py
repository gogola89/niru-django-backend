from django.urls import path
from . import views

app_name = 'student_life_api'

urlpatterns = [
    # Services
    path('services/', views.ServiceListView.as_view(), name='services-list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),

    # Facilities
    path('facilities/', views.FacilityListView.as_view(), name='facilities-list'),

    # Recreation facilities
    path('recreation-facilities/', views.RecreationFacilityListView.as_view(), name='recreation-facilities-list'),
    path('recreation-facilities/<int:pk>/', views.RecreationFacilityDetailView.as_view(), name='recreation-facility-detail'),

    # Combined endpoint
    path('student-services-facilities/', views.student_services_and_facilities, name='student-services-facilities'),
]