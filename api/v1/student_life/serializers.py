from rest_framework import serializers
from apps.student_life.models import Service, Facility, RecreationFacility


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Service model
    """
    image_url = serializers.SerializerMethodField()
    image_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'image_url', 'image_thumbnail_url', 'description', 'order',
            'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            else:
                return obj.image.url
        return None

    def get_image_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.image_thumbnail and hasattr(obj.image_thumbnail, 'url'):
            if request:
                return request.build_absolute_uri(obj.image_thumbnail.url)
            else:
                return obj.image_thumbnail.url
        return None


class FacilitySerializer(serializers.ModelSerializer):
    """
    Serializer for Facility model
    """
    image_url = serializers.SerializerMethodField()
    image_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Facility
        fields = [
            'id', 'name', 'image_url', 'image_thumbnail_url', 'description', 'category',
            'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            else:
                return obj.image.url
        return None

    def get_image_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.image_thumbnail and hasattr(obj.image_thumbnail, 'url'):
            if request:
                return request.build_absolute_uri(obj.image_thumbnail.url)
            else:
                return obj.image_thumbnail.url
        return None


class RecreationFacilitySerializer(FacilitySerializer):
    """
    Serializer for RecreationFacility model (extends Facility)
    """
    class Meta(FacilitySerializer.Meta):
        model = RecreationFacility
        fields = FacilitySerializer.Meta.fields + [
            'capacity', 'availability', 'equipment_available', 'rules_regulations'
        ]