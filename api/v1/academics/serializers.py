from rest_framework import serializers
from apps.academics.models import Programme, ProgrammeHighlight, AdmissionRequirement


class ProgrammeHighlightSerializer(serializers.ModelSerializer):
    """
    Serializer for ProgrammeHighlight model
    """
    icon_url = serializers.SerializerMethodField()
    icon_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = ProgrammeHighlight
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


class AdmissionRequirementSerializer(serializers.ModelSerializer):
    """
    Serializer for AdmissionRequirement model
    """
    class Meta:
        model = AdmissionRequirement
        fields = [
            'id', 'requirement',
            'created_at', 'updated_at'
        ]


class ProgrammeSerializer(serializers.ModelSerializer):
    """
    Serializer for Programme model
    """
    highlights = ProgrammeHighlightSerializer(many=True, read_only=True)
    admission_reqs = AdmissionRequirementSerializer(many=True, read_only=True)

    class Meta:
        model = Programme
        fields = [
            'id', 'name', 'code', 'slug', 'description', 'duration', 'mode',
            'tagline', 'full_description', 'admission_requirements_description', 'application_note',
            'is_featured', 'highlights', 'admission_reqs',
            'created_at', 'updated_at'
        ]