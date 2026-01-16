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


class Chancellor(TimeStampedModel):
    """
    Model for Chancellor information
    """
    name = models.CharField(max_length=200, help_text="Full name of the Chancellor")
    title = models.CharField(max_length=300, help_text="Title and credentials")
    credentials = models.CharField(max_length=200, blank=True, help_text="Additional credentials (e.g., PhD, C.G.H)")
    photo = models.ImageField(upload_to='governance/chancellor/', help_text="Photo of the Chancellor")
    description = models.TextField(blank=True, help_text="Description or biography of the Chancellor")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chancellor: {self.name}"

    class Meta:
        verbose_name = "Chancellor"
        verbose_name_plural = "Chancellors"


class BoardMember(TimeStampedModel):
    """
    Model for Board Members
    """
    BOARD_TYPES = [
        ('trustees', 'Board of Trustees'),
        ('council', 'University Council'),
        ('senate', 'University Senate'),
        ('management', 'Management Board'),
    ]

    name = models.CharField(max_length=200, help_text="Full name of the Board Member")
    position = models.CharField(max_length=300, help_text="Position in the board")
    photo = models.ImageField(upload_to='governance/members/', help_text="Photo of the Board Member")
    bio = models.TextField(blank=True, help_text="Biography of the Board Member")
    board_type = models.CharField(
        max_length=20,
        choices=BOARD_TYPES,
        help_text="Type of board the member belongs to"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = "Board Member"
        verbose_name_plural = "Board Members"
        ordering = ['board_type', 'name']


class GovernanceBody(TimeStampedModel):
    """
    Model for Governance Bodies (Board of Trustees, Council, Senate, Management Board)
    """
    BODY_TYPES = [
        ('trustees', 'Board of Trustees'),
        ('council', 'University Council'),
        ('senate', 'University Senate'),
        ('management', 'Management Board'),
    ]

    name = models.CharField(
        max_length=100,
        choices=BODY_TYPES,
        unique=True,
        help_text="Name/type of the governance body"
    )
    description = models.TextField(help_text="Description of the governance body")
    image = models.ImageField(
        upload_to='governance/body_images/',
        help_text="Image representing the governance body (e.g., meeting photo)"
    )
    members = models.ManyToManyField(BoardMember, blank=True, help_text="Members of this governance body")
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which this body should be displayed"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = "Governance Body"
        verbose_name_plural = "Governance Bodies"
        ordering = ['display_order', 'name']
