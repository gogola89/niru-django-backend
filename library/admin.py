from django.contrib import admin
from .models import LibraryPage, LibrarianMessage, EResource, LibraryPolicy


@admin.register(LibraryPage)
class LibraryPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Mission', {
            'fields': ('mission',)
        }),
        ('Vision', {
            'fields': ('vision',)
        }),
        ('Objectives', {
            'fields': ('objectives',)
        }),
        ('Values', {
            'fields': (
                'value_1_title', 'value_1_description',
                'value_2_title', 'value_2_description',
                'value_3_title', 'value_3_description',
                'value_4_title', 'value_4_description'
            )
        }),
        ('Quality Statement', {
            'fields': ('quality_statement',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one LibraryPage instance
        if LibraryPage.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(LibrarianMessage)
class LibrarianMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'updated_at')
    list_filter = ('updated_at', 'created_at')
    search_fields = ('name', 'title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Librarian Information', {
            'fields': ('name', 'title', 'photo')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(EResource)
class EResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'updated_at')
    list_filter = ('category', 'updated_at', 'created_at')
    search_fields = ('name', 'description', 'url')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Resource Information', {
            'fields': ('name', 'description', 'url', 'category')
        }),
        ('Visual Elements', {
            'fields': ('icon', 'icon_thumbnail'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(LibraryPolicy)
class LibraryPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    list_filter = ('updated_at', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Policy Information', {
            'fields': ('title', 'description', 'document_file')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
