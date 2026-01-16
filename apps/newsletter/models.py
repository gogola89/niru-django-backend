from django.db import models
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
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


class Subscriber(TimeStampedModel):
    """
    Model for Newsletter Subscribers
    """
    email = models.EmailField(unique=True, help_text="Email address of the subscriber")
    name = models.CharField(max_length=200, blank=True, help_text="Name of the subscriber")
    is_active = models.BooleanField(default=True, help_text="Whether the subscriber is active")
    subscribed_date = models.DateTimeField(auto_now_add=True, help_text="Date when the user subscribed")
    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
        help_text="IP address from which the user subscribed"
    )
    unsubscribe_token = models.CharField(
        max_length=32,
        unique=True,
        help_text="Token for unsubscribe functionality"
    )

    def save(self, *args, **kwargs):
        # Generate unsubscribe token if not already set
        if not self.unsubscribe_token:
            self.unsubscribe_token = get_random_string(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.name})"

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        ordering = ['-subscribed_date']


class NewsletterIssue(TimeStampedModel):
    """
    Model for Newsletter Issues
    """
    title = models.CharField(max_length=300, help_text="Title of the newsletter issue")
    content = models.TextField(help_text="Content of the newsletter issue")
    issue_number = models.PositiveIntegerField(help_text="Sequential issue number")
    sent_date = models.DateTimeField(null=True, blank=True, help_text="Date when the newsletter was sent")
    recipients_count = models.PositiveIntegerField(
        default=0,
        help_text="Number of recipients the newsletter was sent to"
    )

    def __str__(self):
        return f"{self.title} (Issue #{self.issue_number})"

    class Meta:
        verbose_name = "Newsletter Issue"
        verbose_name_plural = "Newsletter Issues"
        ordering = ['-issue_number']