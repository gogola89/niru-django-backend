from django.urls import path
from . import views

app_name = 'academics_api'

urlpatterns = [
    # Programmes
    path('programmes/', views.ProgrammeListView.as_view(), name='programmes-list'),
    path('programmes/<slug:slug>/', views.ProgrammeDetailView.as_view(), name='programme-detail'),
    path('programmes/<slug:slug>/details/', views.programme_details_with_requirements, name='programme-details'),

    # Programme highlights
    path('programme-highlights/', views.ProgrammeHighlightListView.as_view(), name='programme-highlights-list'),

    # Admission requirements
    path('admission-requirements/', views.AdmissionRequirementListView.as_view(), name='admission-requirements-list'),

    # Featured programmes
    path('featured-programmes/', views.featured_programmes, name='featured-programmes'),
]