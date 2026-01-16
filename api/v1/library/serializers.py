from rest_framework import serializers
from apps.library.models import LibraryPage, LibrarianMessage, EResource, LibraryPolicy


class EResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for EResource model
    """
    icon_url = serializers.SerializerMethodField()
    icon_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = EResource
        fields = [
            'id', 'name', 'description', 'url', 'icon_url', 'icon_thumbnail_url', 'category',
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


class LibraryPolicySerializer(serializers.ModelSerializer):
    """
    Serializer for LibraryPolicy model
    """
    document_url = serializers.SerializerMethodField()

    class Meta:
        model = LibraryPolicy
        fields = [
            'id', 'title', 'description', 'document_url',
            'created_at', 'updated_at'
        ]

    def get_document_url(self, obj):
        request = self.context.get('request')
        if obj.document_file and hasattr(obj.document_file, 'url'):
            if request:
                return request.build_absolute_uri(obj.document_file.url)
            else:
                return obj.document_file.url
        return None


class LibrarianMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for LibrarianMessage model
    """
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = LibrarianMessage
        fields = [
            'id', 'name', 'title', 'photo_url', 'message',
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


class LibraryPageSerializer(serializers.ModelSerializer):
    """
    Serializer for LibraryPage model
    """
    class Meta:
        model = LibraryPage
        fields = [
            'id', 'mission', 'vision', 'objectives', 'quality_statement',
            'value_1_title', 'value_1_description',
            'value_2_title', 'value_2_description',
            'value_3_title', 'value_3_description',
            'value_4_title', 'value_4_description',
            'created_at', 'updated_at'
        ]