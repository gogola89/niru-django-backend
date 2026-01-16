from rest_framework import serializers
from apps.newsletter.models import Subscriber, NewsletterIssue


class SubscriberSerializer(serializers.ModelSerializer):
    """
    Serializer for Subscriber model
    """
    class Meta:
        model = Subscriber
        fields = [
            'id', 'email', 'name', 'is_active', 'subscribed_date', 'ip_address',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'subscribed_date']


class NewsletterIssueSerializer(serializers.ModelSerializer):
    """
    Serializer for NewsletterIssue model
    """
    class Meta:
        model = NewsletterIssue
        fields = [
            'id', 'title', 'content', 'issue_number', 'sent_date', 'recipients_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']