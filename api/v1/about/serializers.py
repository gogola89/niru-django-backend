from rest_framework import serializers
from apps.about.models import AboutPage, CoreValue, ViceChancellorMessage


class CoreValueSerializer(serializers.ModelSerializer):
    """
    Serializer for CoreValue model
    """
    icon_url = serializers.SerializerMethodField()
    icon_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = CoreValue
        fields = [
            'id', 'title', 'description', 'icon_url', 'icon_thumbnail_url',
            'created_at', 'updated_at'
        ]

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.icon and hasattr(obj.icon, 'url'):
            if request:
                return request.build_absolute_uri(obj.icon.url)
            else:
                return obj.icon.url
        return None

    def get_icon_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.icon_thumbnail and hasattr(obj.icon_thumbnail, 'url'):
            if request:
                return request.build_absolute_uri(obj.icon_thumbnail.url)
            else:
                return obj.icon_thumbnail.url
        return None


class ViceChancellorMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for ViceChancellorMessage model
    """
    photo_url = serializers.SerializerMethodField()
    signature_url = serializers.SerializerMethodField()

    class Meta:
        model = ViceChancellorMessage
        fields = [
            'id', 'name', 'title', 'message', 'photo_url', 'signature_url',
            'created_at', 'updated_at'
        ]

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo and hasattr(obj.photo, 'url'):
            if request:
                return request.build_absolute_uri(obj.photo.url)
            else:
                return obj.photo.url
        return None

    def get_signature_url(self, obj):
        request = self.context.get('request')
        if obj.signature and hasattr(obj.signature, 'url'):
            if request:
                return request.build_absolute_uri(obj.signature.url)
            else:
                return obj.signature.url
        return None


class AboutPageSerializer(serializers.ModelSerializer):
    """
    Serializer for AboutPage model
    """
    class Meta:
        model = AboutPage
        fields = [
            'id', 'mission', 'vision', 'history',
            'created_at', 'updated_at'
        ]