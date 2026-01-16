from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'api'

urlpatterns = [
    # About API
    path('about/', include('api.v1.about.urls')),
    
    # Governance API
    path('governance/', include('api.v1.governance.urls')),
    
    # Academics API
    path('academics/', include('api.v1.academics.urls')),
    
    # Library API
    path('library/', include('api.v1.library.urls')),
    
    # Student Life API
    path('student-life/', include('api.v1.student_life.urls')),
]