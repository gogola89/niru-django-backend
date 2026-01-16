from django.contrib import admin
from .models import AboutPage, CoreValue, ViceChancellorMessage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Mission', {
            'fields': ('mission',)
        }),
        ('Vision', {
            'fields': ('vision',)
        }),
        ('History', {
            'fields': ('history',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one AboutPage instance
        if AboutPage.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Core Value Information', {
            'fields': ('title', 'description')
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


@admin.register(ViceChancellorMessage)
class ViceChancellorMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Vice Chancellor Information', {
            'fields': ('name', 'title', 'photo')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Signature', {
            'fields': ('signature',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
