from rest_framework import serializers
from apps.contact.models import ContactSubmission, ContactSettings


class ContactSubmissionSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactSubmission model
    """
    class Meta:
        model = ContactSubmission
        fields = [
            'id', 'name', 'email', 'phone', 'subject', 'message', 'ip_address',
            'is_read', 'replied_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ContactSettingsSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactSettings model
    """
    class Meta:
        model = ContactSettings
        fields = [
            'id', 'recipient_emails', 'auto_reply_enabled', 'auto_reply_subject',
            'auto_reply_message', 'success_message', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']