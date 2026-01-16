from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
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


class Service(TimeStampedModel):
    """
    Model for Student Services
    """
    name = models.CharField(max_length=200, help_text="Name of the service")
    image = models.ImageField(upload_to='services/', help_text="Image of the service")
    description = models.TextField(help_text="Description of the service")
    order = models.PositiveIntegerField(default=0, help_text="Order in which the service should be displayed")

    # Thumbnail generation for the image
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 300)],  # Standard thumbnail size
        format='JPEG',
        options={'quality': 85}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'name']


class Facility(TimeStampedModel):
    """
    Model for Facilities
    """
    CATEGORY_CHOICES = [
        ('recreation', 'Recreation'),
        ('accommodation', 'Accommodation'),
        ('dining', 'Dining'),
        ('study', 'Study'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200, help_text="Name of the facility")
    image = models.ImageField(upload_to='facilities/', help_text="Image of the facility")
    description = models.TextField(help_text="Description of the facility")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        help_text="Category of the facility"
    )

    # Thumbnail generation for the image
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 300)],  # Standard thumbnail size
        format='JPEG',
        options={'quality': 85}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"
        ordering = ['category', 'name']


class RecreationFacility(Facility):
    """
    Model extending Facility for Recreation-specific fields
    """
    capacity = models.CharField(max_length=100, blank=True, help_text="Capacity of the facility")
    availability = models.CharField(max_length=200, blank=True, help_text="Availability schedule")
    equipment_available = models.TextField(blank=True, help_text="List of equipment available")
    rules_regulations = models.TextField(blank=True, help_text="Rules and regulations for the facility")

    def __str__(self):
        return f"Recreation: {self.name}"

    class Meta:
        verbose_name = "Recreation Facility"
        verbose_name_plural = "Recreation Facilities"
