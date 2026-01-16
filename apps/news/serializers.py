from rest_framework import serializers
from apps.news.models import NewsCategory, NewsArticle, Event
from apps.newsletter.models import Subscriber, NewsletterIssue
from apps.contact.models import ContactSubmission, ContactSettings
from django_summernote.fields import SummernoteTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class NewsCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for NewsCategory model
    """
    class Meta:
        model = NewsCategory
        fields = [
            'id', 'name', 'slug', 'description', 'icon_image', 'created_at', 'updated_at'
        ]


class NewsArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for NewsArticle model
    """
    category = NewsCategorySerializer(read_only=True)
    featured_image_url = serializers.SerializerMethodField()
    thumbnail_image_url = serializers.SerializerMethodField()
    featured_image_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = NewsArticle
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content',
            'featured_image_url', 'thumbnail_image_url', 'featured_image_thumbnail_url',
            'author_name', 'author_title', 'publish_date', 'status',
            'is_featured', 'tags', 'category',
            'created_at', 'updated_at'
        ]

    def get_featured_image_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image and hasattr(obj.featured_image, 'url'):
            if request:
                return request.build_absolute_uri(obj.featured_image.url)
            else:
                return obj.featured_image.url
        return None

    def get_thumbnail_image_url(self, obj):
        request = self.context.get('request')
        # If thumbnail_image is provided, use it; otherwise use the auto-generated thumbnail
        image = obj.thumbnail_image or obj.featured_image
        if image and hasattr(image, 'url'):
            if request:
                return request.build_absolute_uri(image.url)
            else:
                return image.url
        return None

    def get_featured_image_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image_thumbnail and hasattr(obj.featured_image_thumbnail, 'url'):
            if request:
                return request.build_absolute_uri(obj.featured_image_thumbnail.url)
            else:
                return obj.featured_image_thumbnail.url
        return None


class EventSerializer(NewsArticleSerializer):
    """
    Serializer for Event model (extends NewsArticle)
    """
    class Meta(NewsArticleSerializer.Meta):
        model = Event
        fields = NewsArticleSerializer.Meta.fields + [
            'event_date', 'location', 'registration_link', 'event_image'
        ]


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