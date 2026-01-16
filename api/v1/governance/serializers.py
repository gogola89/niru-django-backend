from rest_framework import serializers
from apps.governance.models import Chancellor, BoardMember, GovernanceBody


class BoardMemberSerializer(serializers.ModelSerializer):
    """
    Serializer for BoardMember model
    """
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = BoardMember
        fields = [
            'id', 'name', 'position', 'photo_url', 'bio', 'board_type',
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


class ChancellorSerializer(serializers.ModelSerializer):
    """
    Serializer for Chancellor model
    """
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Chancellor
        fields = [
            'id', 'name', 'title', 'credentials', 'photo_url', 'description',
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


class GovernanceBodySerializer(serializers.ModelSerializer):
    """
    Serializer for GovernanceBody model
    """
    image_url = serializers.SerializerMethodField()
    members = BoardMemberSerializer(many=True, read_only=True)

    class Meta:
        model = GovernanceBody
        fields = [
            'id', 'name', 'description', 'image_url', 'display_order', 'members',
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