from django.contrib import admin
from .models import ContactSubmission, ContactSettings


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at', 'ip_address')
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Processing Information', {
            'fields': ('ip_address', 'is_read', 'replied_at'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ['-created_at']
    
    # Actions to mark as read/unread
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected submissions as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected submissions as unread"


@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at')
    fieldsets = (
        ('Recipient Settings', {
            'fields': ('recipient_emails',)
        }),
        ('Auto-reply Settings', {
            'fields': ('auto_reply_enabled', 'auto_reply_subject', 'auto_reply_message'),
            'classes': ('collapse',)
        }),
        ('User Experience', {
            'fields': ('success_message',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one settings instance
        if ContactSettings.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the settings instance
        return False