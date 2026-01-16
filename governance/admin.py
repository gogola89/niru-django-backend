from django.contrib import admin
from .models import Chancellor, BoardMember, GovernanceBody


@admin.register(Chancellor)
class ChancellorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'updated_at')
    list_filter = ('updated_at', 'created_at')
    search_fields = ('name', 'title', 'credentials')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Chancellor Information', {
            'fields': ('name', 'title', 'credentials')
        }),
        ('Visual Elements', {
            'fields': ('photo',)
        }),
        ('Biography', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one Chancellor instance
        if Chancellor.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'board_type', 'updated_at')
    list_filter = ('board_type', 'updated_at', 'created_at')
    search_fields = ('name', 'position', 'bio')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Board Member Information', {
            'fields': ('name', 'position', 'board_type')
        }),
        ('Visual Elements', {
            'fields': ('photo',)
        }),
        ('Biography', {
            'fields': ('bio',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class BoardMemberInline(admin.TabularInline):
    model = GovernanceBody.members.through
    extra = 1


@admin.register(GovernanceBody)
class GovernanceBodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'updated_at')
    list_filter = ('name', 'display_order', 'updated_at', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Body Information', {
            'fields': ('name', 'description', 'display_order')
        }),
        ('Visual Elements', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    inlines = [BoardMemberInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "members":
            kwargs["queryset"] = BoardMember.objects.order_by('board_type', 'name')
        return super().formfield_for_manytomany(db_field, request, **kwargs)
