from django.db import models
from django_summernote.fields import SummernoteTextField
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


class LibraryPage(TimeStampedModel):
    """
    Model for Library page content
    """
    mission = SummernoteTextField(help_text="Mission statement of the library")
    vision = SummernoteTextField(help_text="Vision statement of the library")
    objectives = SummernoteTextField(help_text="Objectives of the library")

    # Values
    value_1_title = models.CharField(max_length=200, help_text="Title for first value")
    value_1_description = models.TextField(help_text="Description for first value")

    value_2_title = models.CharField(max_length=200, help_text="Title for second value")
    value_2_description = models.TextField(help_text="Description for second value")

    value_3_title = models.CharField(max_length=200, help_text="Title for third value")
    value_3_description = models.TextField(help_text="Description for third value")

    value_4_title = models.CharField(max_length=200, help_text="Title for fourth value")
    value_4_description = models.TextField(help_text="Description for fourth value")

    # Quality statement
    quality_statement = SummernoteTextField(help_text="Quality statement of the library")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Library Page Content"

    class Meta:
        verbose_name = "Library Page"
        verbose_name_plural = "Library Pages"


class LibrarianMessage(TimeStampedModel):
    """
    Model for Librarian's message
    """
    name = models.CharField(max_length=200, help_text="Full name of the Librarian")
    title = models.CharField(max_length=300, help_text="Title of the Librarian")
    photo = models.ImageField(upload_to='librarian_photos/', help_text="Photo of the Librarian")
    message = SummernoteTextField(help_text="Message from the Librarian")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Librarian Message: {self.name}"

    class Meta:
        verbose_name = "Librarian Message"
        verbose_name_plural = "Librarian Messages"


class EResource(TimeStampedModel):
    """
    Model for Electronic Resources
    """
    CATEGORY_CHOICES = [
        ('catalog', 'Catalog'),
        ('eresources', 'Electronic Resources'),
        ('platform', 'Platform'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=300, help_text="Name of the electronic resource")
    description = models.TextField(help_text="Description of the electronic resource")
    url = models.URLField(help_text="URL to access the electronic resource")
    icon = models.ImageField(upload_to='e_resource_icons/', blank=True, null=True,
                             help_text="Icon image for the electronic resource")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        help_text="Category of the electronic resource"
    )

    # Thumbnail generation for the icon
    icon_thumbnail = ImageSpecField(
        source='icon',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 85}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "E-Resource"
        verbose_name_plural = "E-Resources"
        ordering = ['category', 'name']


class LibraryPolicy(TimeStampedModel):
    """
    Model for Library Policies
    """
    title = models.CharField(max_length=300, help_text="Title of the policy")
    document_file = models.FileField(upload_to='library_policies/', help_text="Policy document file")
    description = models.TextField(help_text="Description of the policy")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Library Policy"
        verbose_name_plural = "Library Policies"
