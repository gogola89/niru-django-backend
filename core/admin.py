from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import SiteSettings, PageHero


# Update the default admin site's attributes
AdminSite.site_header = 'NIRU Administration'
AdminSite.site_title = 'NIRU Admin Portal'
AdminSite.index_title = 'Welcome to NIRU Admin Portal'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'short_name', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('University Information', {
            'fields': ('university_name', 'short_name', 'tagline', 'logo')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone_numbers', 'email')
        }),
        ('Social Media', {
            'fields': ('facebook', 'twitter', 'linkedin', 'instagram', 'youtube'),
            'classes': ('collapse',)
        }),
        ('Legal & Copyright', {
            'fields': ('copyright_text', 'charter_date', 'charter_by')
        }),
        ('Site Settings', {
            'fields': ('maintenance_mode', 'analytics_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PageHero)
class PageHeroAdmin(admin.ModelAdmin):
    list_display = ('page_identifier', 'title', 'is_active', 'overlay_opacity', 'updated_at')
    list_filter = ('is_active', 'page_identifier', 'overlay_opacity')
    list_editable = ('is_active', 'overlay_opacity')
    search_fields = ('title', 'subtitle', 'page_identifier')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Page Identification', {
            'fields': ('page_identifier',)
        }),
        ('Hero Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Visual Settings', {
            'fields': ('background_image', 'overlay_opacity')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('page_identifier')