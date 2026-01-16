from django.contrib import admin
from .models import Subscriber, NewsletterIssue


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'subscribed_date', 'updated_at')
    list_filter = ('is_active', 'subscribed_date', 'created_at', 'updated_at')
    search_fields = ('email', 'name')
    readonly_fields = ('created_at', 'updated_at', 'unsubscribe_token', 'subscribed_date')

    fieldsets = (
        ('Subscriber Information', {
            'fields': ('email', 'name', 'is_active', 'ip_address')
        }),
        ('Subscription Details', {
            'fields': ('unsubscribe_token',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('subscribed_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ['-subscribed_date']


@admin.register(NewsletterIssue)
class NewsletterIssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_number', 'sent_date', 'recipients_count', 'updated_at')
    list_filter = ('sent_date', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Issue Information', {
            'fields': ('title', 'issue_number', 'content')
        }),
        ('Delivery Information', {
            'fields': ('sent_date', 'recipients_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ['-issue_number']