from django.urls import path
from . import views

app_name = 'library_api'

urlpatterns = [
    # Library page
    path('library-page/', views.LibraryPageDetailView.as_view(), name='library-page-detail'),
    
    # Librarian message
    path('librarian-message/', views.LibrarianMessageDetailView.as_view(), name='librarian-message-detail'),
    
    # E-resources
    path('e-resources/', views.EResourceListView.as_view(), name='e-resources-list'),
    
    # Library policies
    path('policies/', views.LibraryPolicyListView.as_view(), name='policies-list'),
    
    # Combined endpoint
    path('library-resources/', views.library_resources, name='library-resources'),
]