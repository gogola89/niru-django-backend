from django.contrib import admin
from .models import Programme, ProgrammeHighlight, AdmissionRequirement


class ProgrammeHighlightInline(admin.TabularInline):
    model = ProgrammeHighlight
    extra = 1


class AdmissionRequirementInline(admin.TabularInline):
    model = AdmissionRequirement
    extra = 1


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_featured', 'updated_at')
    list_filter = ('is_featured', 'mode', 'duration', 'updated_at', 'created_at')
    search_fields = ('name', 'code', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'code', 'slug', 'tagline', 'is_featured')
        }),
        ('Description', {
            'fields': ('description', 'full_description')
        }),
        ('Details', {
            'fields': ('duration', 'mode')
        }),
        ('Admissions', {
            'fields': ('admission_requirements_description', 'application_note')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [ProgrammeHighlightInline, AdmissionRequirementInline]


@admin.register(ProgrammeHighlight)
class ProgrammeHighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'programme', 'created_at')
    list_filter = ('programme', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'programme__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Highlight Information', {
            'fields': ('programme', 'title', 'description')
        }),
        ('Visual Elements', {
            'fields': ('icon',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AdmissionRequirement)
class AdmissionRequirementAdmin(admin.ModelAdmin):
    list_display = ('programme', 'requirement', 'created_at')
    list_filter = ('programme', 'created_at', 'updated_at')
    search_fields = ('requirement', 'programme__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Admission Requirement', {
            'fields': ('programme', 'requirement')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
