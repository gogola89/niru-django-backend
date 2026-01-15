from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
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


class SEOModel(models.Model):
    """
    Abstract model to add SEO fields
    """
    meta_title = models.CharField(max_length=200, blank=True, help_text="SEO title (max 200 chars)")
    meta_description = models.TextField(max_length=500, blank=True, help_text="SEO description (max 500 chars)")
    meta_keywords = models.CharField(max_length=500, blank=True, help_text="Comma-separated keywords")

    class Meta:
        abstract = True


class PublishableModel(models.Model):
    """
    Abstract model to add publishing functionality
    """
    is_published = models.BooleanField(default=True, help_text="Whether this content is published")
    publish_date = models.DateTimeField(null=True, blank=True, help_text="Date to publish this content")

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    """
    Model for global site configuration
    """
    university_name = models.CharField(max_length=200, default="National Intelligence and Research University")
    short_name = models.CharField(max_length=20, default="NIRU")
    tagline = models.CharField(max_length=200, default="Premier Science and Research-Intensive African University")

    # Contact information
    address = models.TextField(default="P.O. Box 47446 - 00100, Nairobi, Kenya")
    phone_numbers = models.JSONField(default=list, help_text="List of phone numbers")  # e.g., ["+254 798 471845", "+254 742 093140"]
    email = models.EmailField(default="admin@niru.ac.ke")

    # Social media links
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    # Logo and branding
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    # Copyright and legal
    copyright_text = models.TextField(default="Copyright 2025. National Intelligence and Research University. All Rights Reserved.")

    # University charter information
    charter_date = models.DateField(null=True, blank=True)
    charter_by = models.CharField(max_length=200, blank=True, help_text="Who chartered the university")

    # Site-wide settings
    maintenance_mode = models.BooleanField(default=False)
    analytics_code = models.TextField(blank=True, help_text="Google Analytics or other tracking code")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.university_name} Settings"

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"


class PageHero(models.Model):
    """
    Model for page-specific hero sections with background images
    """
    # Unique page identifier
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About Us'),
        ('governance', 'Governance'),
        ('programmes', 'Academic Programmes'),
        ('programme-detail', 'Programme Detail'),
        ('library', 'Library'),
        ('student-life', 'Student Life'),
        ('recreation', 'Recreation'),
        ('research', 'Research'),
        ('news-events', 'News & Events'),
        ('contact', 'Contact Us'),
    ]

    page_identifier = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        unique=True,
        help_text="Unique identifier for the page"
    )

    title = models.CharField(max_length=200, blank=True, help_text="Optional overlay title")
    subtitle = models.CharField(max_length=300, blank=True, help_text="Optional overlay subtitle")

    # Background image for the hero section
    background_image = models.ImageField(
        upload_to='heroes/',
        help_text="Hero image for the page navbar/hero section"
    )

    # Overlay opacity for better text readability
    overlay_opacity = models.IntegerField(
        default=50,
        choices=[(i, i) for i in range(0, 101, 5)],  # 0 to 100 in steps of 5
        help_text="Opacity percentage for dark overlay (0-100)"
    )

    # Status
    is_active = models.BooleanField(default=True, help_text="Whether this hero is active")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_page_identifier_display()} Hero"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Optimize the image after saving
        if self.background_image:
            img_path = self.background_image.path
            if os.path.exists(img_path):
                img = Image.open(img_path)

                # Resize if too large (max 1920x600 for hero images)
                if img.width > 1920 or img.height > 600:
                    img.thumbnail((1920, 600), Image.Resampling.LANCZOS)

                # Save the optimized image
                img.save(img_path, optimize=True, quality=85)

    class Meta:
        verbose_name = "Page Hero"
        verbose_name_plural = "Page Heroes"
        ordering = ['page_identifier']
