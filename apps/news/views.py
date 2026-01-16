from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import NewsCategory, NewsArticle, Event
from .serializers import NewsCategorySerializer, NewsArticleSerializer, EventSerializer
from apps.newsletter.models import Subscriber, NewsletterIssue
from apps.newsletter.serializers import SubscriberSerializer, NewsletterIssueSerializer
from apps.contact.models import ContactSubmission, ContactSettings
from apps.contact.serializers import ContactSubmissionSerializer, ContactSettingsSerializer


from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import NewsCategory, NewsArticle, Event
from .serializers import NewsCategorySerializer, NewsArticleSerializer, EventSerializer
from apps.newsletter.models import Subscriber, NewsletterIssue
from apps.newsletter.serializers import SubscriberSerializer, NewsletterIssueSerializer
from apps.contact.models import ContactSubmission, ContactSettings
from apps.contact.serializers import ContactSubmissionSerializer, ContactSettingsSerializer


class NewsCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing news categories.
    """
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [AllowAny]


class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing news articles.
    """
    queryset = NewsArticle.objects.filter(status='published').order_by('-publish_date')
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'is_featured', 'status']

    def get_queryset(self):
        queryset = NewsArticle.objects.filter(status='published').order_by('-publish_date')
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)

        if category is not None:
            queryset = queryset.filter(category__slug=category)
        if featured is not None:
            queryset = queryset.filter(is_featured=(featured.lower() == 'true'))

        return queryset


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing events.
    """
    queryset = Event.objects.filter(status='published').order_by('-event_date')
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class SubscriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing newsletter subscribers.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create a new subscriber with email validation and duplicate checking
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check for duplicate email
        email = serializer.validated_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            return Response(
                {'error': 'This email is already subscribed.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save the subscriber
        subscriber = serializer.save()

        # Send confirmation email (optional)
        # send_confirmation_email(subscriber.email, subscriber.name)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


@api_view(['POST'])
def subscribe_newsletter(request):
    """
    API endpoint for subscribing to the newsletter
    """
    email = request.data.get('email')
    name = request.data.get('name', '')

    if not email:
        return Response(
            {'error': 'Email is required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validate email format
    from django.core.validators import validate_email
    try:
        validate_email(email)
    except ValidationError:
        return Response(
            {'error': 'Invalid email format.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Check for duplicates
    if Subscriber.objects.filter(email=email).exists():
        return Response(
            {'error': 'This email is already subscribed.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Create subscriber
    subscriber = Subscriber.objects.create(
        email=email,
        name=name,
        ip_address=request.META.get('REMOTE_ADDR', '')
    )

    serializer = SubscriberSerializer(subscriber, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsletterIssueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing newsletter issues.
    """
    queryset = NewsletterIssue.objects.all().order_by('-issue_number')
    serializer_class = NewsletterIssueSerializer
    permission_classes = [AllowAny]


class ContactSubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing contact form submissions.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create a new contact submission with spam protection
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Add IP address to the submission
        validated_data = serializer.validated_data
        validated_data['ip_address'] = request.META.get('REMOTE_ADDR', '')

        contact_submission = serializer.save()

        # Send notification email to admin
        self.send_notification_email(contact_submission)

        # Optionally send auto-reply to user if enabled
        self.send_auto_reply_if_enabled(contact_submission)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def send_notification_email(self, submission):
        """
        Send notification email to admin about new contact submission
        """
        try:
            # Get admin email settings
            contact_settings = ContactSettings.objects.first()
            if contact_settings:
                admin_emails = [email.strip() for email in contact_settings.recipient_emails.split(',')]

                subject = f"New Contact Form Submission: {submission.subject}"
                message = f"""
                New contact form submission received:

                Name: {submission.name}
                Email: {submission.email}
                Phone: {submission.phone}
                Subject: {submission.subject}
                Message: {submission.message}
                IP Address: {submission.ip_address}
                Submitted at: {submission.created_at}
                """

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    admin_emails,
                    fail_silently=False,
                )
        except Exception as e:
            # Log the error but don't fail the submission
            print(f"Error sending notification email: {e}")

    def send_auto_reply_if_enabled(self, submission):
        """
        Send auto-reply to user if enabled in settings
        """
        try:
            contact_settings = ContactSettings.objects.first()
            if contact_settings and contact_settings.auto_reply_enabled:
                subject = contact_settings.auto_reply_subject
                message = contact_settings.auto_reply_message.format(name=submission.name)

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [submission.email],
                    fail_silently=True,
                )
        except Exception as e:
            # Log the error but don't fail the submission
            print(f"Error sending auto-reply email: {e}")


@api_view(['POST'])
def submit_contact_form(request):
    """
    API endpoint for submitting the contact form
    """
    serializer = ContactSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        # Create the submission with IP address
        contact_submission = ContactSubmission.objects.create(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            phone=serializer.validated_data.get('phone', ''),
            subject=serializer.validated_data['subject'],
            message=serializer.validated_data['message'],
            ip_address=request.META.get('REMOTE_ADDR', '')
        )

        # Send notification emails
        try:
            # Get admin email settings
            contact_settings = ContactSettings.objects.first()
            if contact_settings:
                admin_emails = [email.strip() for email in contact_settings.recipient_emails.split(',')]

                subject = f"New Contact Form Submission: {contact_submission.subject}"
                message = f"""
                New contact form submission received:

                Name: {contact_submission.name}
                Email: {contact_submission.email}
                Phone: {contact_submission.phone}
                Subject: {contact_submission.subject}
                Message: {contact_submission.message}
                IP Address: {contact_submission.ip_address}
                Submitted at: {contact_submission.created_at}
                """

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    admin_emails,
                    fail_silently=False,
                )
        except Exception as e:
            # Log error but continue
            print(f"Error sending notification: {e}")

        # Prepare success response
        contact_settings = ContactSettings.objects.first()
        success_message = contact_settings.success_message if contact_settings else "Thank you for your message. We will get back to you soon."

        return Response({'message': success_message}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing contact form settings.
    """
    queryset = ContactSettings.objects.all()
    serializer_class = ContactSettingsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Only return the first (and typically only) contact settings instance
        queryset = ContactSettings.objects.all()
        if queryset.exists():
            return queryset[:1]  # Limit to just the first instance
        return queryset