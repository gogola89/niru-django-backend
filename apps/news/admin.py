from django.contrib import admin
from django.utils.html import format_html
from .models import NewsCategory, NewsArticle, Event


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Visual Elements', {
            'fields': ('icon_image',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_name', 'status', 'is_featured', 'publish_date', 'updated_at')
    list_filter = ('status', 'is_featured', 'category', 'publish_date', 'created_at')
    search_fields = ('title', 'excerpt', 'content', 'author_name')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Publishing Information', {
            'fields': ('author_name', 'author_title', 'publish_date', 'status', 'is_featured')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Images', {
            'fields': ('featured_image', 'thumbnail_image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        # Exclude events from the NewsArticle admin (they're managed separately)
        qs = super().get_queryset(request)
        return qs.exclude(pk__in=Event.objects.values_list('pk', flat=True))


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'status', 'updated_at')
    list_filter = ('status', 'event_date', 'publish_date', 'created_at')
    search_fields = ('title', 'excerpt', 'content', 'location', 'author_name')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Publishing Information', {
            'fields': ('author_name', 'author_title', 'publish_date', 'status', 'is_featured')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Event Details', {
            'fields': ('event_date', 'location', 'registration_link', 'event_image')
        }),
        ('Images', {
            'fields': ('featured_image', 'thumbnail_image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )