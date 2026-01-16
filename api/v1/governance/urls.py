from django.urls import path
from . import views

app_name = 'governance_api'

urlpatterns = [
    # Chancellor
    path('chancellor/', views.ChancellorDetailView.as_view(), name='chancellor-detail'),
    
    # Board members
    path('board-members/', views.BoardMemberListView.as_view(), name='board-members-list'),
    
    # Governance bodies
    path('governance-bodies/', views.GovernanceBodyListView.as_view(), name='governance-bodies-list'),
    path('governance-bodies/<int:pk>/', views.GovernanceBodyDetailView.as_view(), name='governance-body-detail'),
    
    # Combined endpoint
    path('governance-structure/', views.governance_structure, name='governance-structure'),
]