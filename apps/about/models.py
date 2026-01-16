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


class AboutPage(TimeStampedModel):
    """
    Model for the About page content
    """
    mission = SummernoteTextField(help_text="Mission statement with rich text formatting")
    vision = SummernoteTextField(help_text="Vision statement with rich text formatting")
    history = SummernoteTextField(help_text="History of the university with rich text formatting")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"


class CoreValue(TimeStampedModel):
    """
    Model for core values that can be associated with the About page
    """
    title = models.CharField(max_length=200, help_text="Title of the core value")
    icon = models.ImageField(upload_to='core_values/', blank=True, null=True,
                             help_text="Icon image for the core value")
    description = models.TextField(help_text="Description of the core value")

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
        return self.title

    class Meta:
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"


class ViceChancellorMessage(TimeStampedModel):
    """
    Model for Vice Chancellor's message
    """
    name = models.CharField(max_length=200, help_text="Full name of the Vice Chancellor")
    title = models.CharField(max_length=300, help_text="Title and credentials")
    photo = models.ImageField(upload_to='vc_photos/', help_text="Photo of the Vice Chancellor")
    message = SummernoteTextField(help_text="Message from the Vice Chancellor")
    signature = models.ImageField(upload_to='vc_signatures/', blank=True, null=True,
                                  help_text="Signature image of the Vice Chancellor")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"VC Message: {self.name}"

    class Meta:
        verbose_name = "Vice Chancellor Message"
        verbose_name_plural = "Vice Chancellor Messages"
