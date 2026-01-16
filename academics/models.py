from django.db import models
from django.utils.text import slugify
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


class Programme(TimeStampedModel):
    """
    Model for Academic Programmes
    """
    name = models.CharField(max_length=300, help_text="Full name of the programme")
    code = models.CharField(max_length=20, unique=True, help_text="Programme code (e.g., MISPS, MSIS)")
    slug = models.SlugField(unique=True, help_text="SEO-friendly slug for the programme")
    description = SummernoteTextField(help_text="Detailed description of the programme")
    duration = models.CharField(max_length=100, help_text="Duration of the programme (e.g., 2 years)")
    mode = models.CharField(max_length=100, help_text="Mode of study (e.g., Full-time / Part-time)")
    tagline = models.CharField(max_length=500, blank=True, help_text="Short tagline for the programme")
    full_description = SummernoteTextField(blank=True, help_text="Extended description of the programme")

    # General admission requirements description
    admission_requirements_description = models.TextField(help_text="General admission requirements description for the programme")

    # Application note
    application_note = models.TextField(blank=True, help_text="Application note or instructions")

    # Featured status
    is_featured = models.BooleanField(default=False, help_text="Whether this programme is featured")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Programme"
        verbose_name_plural = "Programmes"
        ordering = ['-is_featured', 'name']


class ProgrammeHighlight(TimeStampedModel):
    """
    Model for Programme Highlights
    """
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=200, help_text="Title of the highlight")
    icon = models.ImageField(upload_to='programme_highlights/', blank=True, null=True,
                             help_text="Icon image for the highlight")
    description = models.TextField(help_text="Description of the highlight")

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
        return f"{self.title} - {self.programme.name}"

    class Meta:
        verbose_name = "Programme Highlight"
        verbose_name_plural = "Programme Highlights"


class AdmissionRequirement(TimeStampedModel):
    """
    Model for Admission Requirements
    """
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='admission_reqs')
    requirement = models.TextField(help_text="Specific admission requirement")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Requirement for {self.programme.name}"

    class Meta:
        verbose_name = "Admission Requirement"
        verbose_name_plural = "Admission Requirements"
