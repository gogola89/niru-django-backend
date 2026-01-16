from django.contrib import admin
from .models import Service, Facility, RecreationFacility


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'updated_at')
    list_filter = ('order', 'updated_at', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'description', 'order')
        }),
        ('Visual Elements', {
            'fields': ('image', 'image_thumbnail'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('order', 'name')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'updated_at')
    list_filter = ('category', 'updated_at', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Facility Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Visual Elements', {
            'fields': ('image', 'image_thumbnail'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('category', 'name')


@admin.register(RecreationFacility)
class RecreationFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'capacity', 'updated_at')
    list_filter = ('category', 'updated_at', 'created_at')
    search_fields = ('name', 'description', 'capacity')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Facility Information', {
            'fields': ('name', 'description', 'category', 'capacity')
        }),
        ('Availability & Equipment', {
            'fields': ('availability', 'equipment_available'),
            'classes': ('collapse',)
        }),
        ('Rules & Regulations', {
            'fields': ('rules_regulations',),
            'classes': ('collapse',)
        }),
        ('Visual Elements', {
            'fields': ('image', 'image_thumbnail'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('category', 'name')
