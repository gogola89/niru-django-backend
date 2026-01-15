from rest_framework import serializers
from .models import PageHero


class PageHeroSerializer(serializers.ModelSerializer):
    background_image_url = serializers.SerializerMethodField()

    class Meta:
        model = PageHero
        fields = [
            'page_identifier', 'title', 'subtitle', 
            'background_image_url', 'overlay_opacity', 
            'is_active', 'created_at', 'updated_at'
        ]

    def get_background_image_url(self, obj):
        request = self.context.get('request')
        if obj.background_image and hasattr(obj.background_image, 'url'):
            if request:
                try:
                    return request.build_absolute_uri(obj.background_image.url)
                except Exception:
                    # Fallback if request host is not properly configured
                    from django.conf import settings
                    return f"{settings.ALLOWED_HOSTS[0] if settings.ALLOWED_HOSTS else 'http://localhost:8000'}{obj.background_image.url}"
            else:
                # Fallback to MEDIA_URL if request is not available
                from django.conf import settings
                return f"http://localhost:8000{obj.background_image.url}"
        return None