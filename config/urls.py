"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Django Summernote
    path('summernote/', include('django_summernote.urls')),

    # API Routes - combining core and app-specific APIs
    path('api/v1/', include([
        # Core API routes
        path('', include('core.api_urls')),

        # App-specific API routes
        path('about/', include('api.v1.about.urls')),
        path('governance/', include('api.v1.governance.urls')),
        path('academics/', include('api.v1.academics.urls')),
        path('library/', include('api.v1.library.urls')),
        path('student-life/', include('api.v1.student_life.urls')),
    ])),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
