from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from PIL import Image
import os


class TimeStampedModel(models.Model):
    """
    Abstract model to add created_at and updated_at timestamps
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsCategory(TimeStampedModel):
    """
    Model for News Categories
    """
    name = models.CharField(max_length=200, unique=True, help_text="Name of the news category")
    slug = models.SlugField(unique=True, help_text="SEO-friendly slug for the category")
    description = models.TextField(blank=True, help_text="Description of the category")
    icon_image = models.ImageField(
        upload_to='news/category_icons/',
        blank=True,
        null=True,
        help_text="Icon image for the category"
    )

    # Thumbnail generation for the icon
    icon_thumbnail = ImageSpecField(
        source='icon_image',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 85}
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"
        ordering = ['name']


class NewsArticle(TimeStampedModel):
    """
    Model for News Articles
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('review', 'Under Review'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=300, help_text="Title of the news article")
    slug = models.SlugField(unique=True, help_text="SEO-friendly slug for the article")
    content = models.TextField(help_text="Content of the news article")
    excerpt = models.TextField(help_text="Brief excerpt of the article for list views")

    # Featured image and thumbnail
    featured_image = models.ImageField(
        upload_to='news/featured/',
        help_text="Featured image for the article (used in detail view)"
    )
    thumbnail_image = models.ImageField(
        upload_to='news/thumbnails/',
        blank=True,
        null=True,
        help_text="Thumbnail image for the article (used in list views, auto-generated if not provided)"
    )

    # Auto-generated thumbnail from featured image if thumbnail_image is not provided
    featured_image_thumbnail = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(400, 225)],  # Standard thumbnail size for news cards
        format='JPEG',
        options={'quality': 85}
    )

    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        help_text="Category of the news article"
    )

    # Author information
    author_name = models.CharField(max_length=200, help_text="Name of the author")
    author_title = models.CharField(max_length=300, blank=True, help_text="Title of the author")

    # Publishing information
    publish_date = models.DateTimeField(help_text="Date when the article should be published")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        help_text="Status of the article in the publishing workflow"
    )

    # Featured status
    is_featured = models.BooleanField(default=False, help_text="Whether this article is featured on homepage")

    # Tags
    tags = TaggableManager(help_text="Tags for the article (comma separated)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # If no thumbnail is provided, we'll use the auto-generated one from featured_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ['-publish_date', '-created_at']


class Event(NewsArticle):
    """
    Model for Events (extends NewsArticle with event-specific fields)
    """
    event_date = models.DateTimeField(help_text="Date and time of the event")
    location = models.CharField(max_length=300, help_text="Location of the event")
    registration_link = models.URLField(
        blank=True,
        help_text="Registration link for the event (optional)"
    )
    event_image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True,
        help_text="Specific image for the event (if different from news featured image)"
    )

    def __str__(self):
        return f"Event: {self.title}"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-event_date', '-publish_date']