from django.db import models
from django.core.validators import validate_email
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


class ContactSubmission(TimeStampedModel):
    """
    Model for Contact Form Submissions
    """
    name = models.CharField(max_length=200, help_text="Name of the person submitting the form")
    email = models.EmailField(help_text="Email address of the submitter")
    phone = models.CharField(max_length=20, blank=True, help_text="Phone number of the submitter")
    subject = models.CharField(max_length=300, help_text="Subject of the message")
    message = models.TextField(help_text="Content of the message")
    ip_address = models.GenericIPAddressField(
        help_text="IP address of the submitter (captured automatically)"
    )
    is_read = models.BooleanField(default=False, help_text="Whether the submission has been read by admin")
    replied_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Date and time when the submission was replied to"
    )

    def __str__(self):
        return f"{self.subject} - {self.name}"

    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']


class ContactSettings(TimeStampedModel):
    """
    Model for Contact Form Settings
    """
    recipient_emails = models.TextField(
        help_text="Comma-separated list of email addresses to receive contact form submissions"
    )
    auto_reply_enabled = models.BooleanField(
        default=True,
        help_text="Whether to send an auto-reply to the submitter"
    )
    auto_reply_subject = models.CharField(
        max_length=300,
        default="Thank you for contacting us",
        help_text="Subject for the auto-reply email"
    )
    auto_reply_message = models.TextField(
        help_text="Template for the auto-reply message (use {name} for submitter's name)"
    )
    success_message = models.TextField(
        default="Thank you for your message. We will get back to you soon.",
        help_text="Message to display after successful submission"
    )

    def __str__(self):
        return "Contact Form Settings"

    class Meta:
        verbose_name = "Contact Settings"
        verbose_name_plural = "Contact Settings"