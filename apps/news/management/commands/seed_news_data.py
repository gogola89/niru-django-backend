import os
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.news.models import NewsCategory, NewsArticle
from apps.newsletter.models import NewsletterIssue
from apps.contact.models import ContactSettings
from django.utils.text import slugify
from datetime import datetime


class Command(BaseCommand):
    help = 'Seed the database with initial data for news, newsletter, and contact apps'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force creation of data even if it already exists',
        )

    def handle(self, *args, **options):
        self.stdout.write('Seeding news, newsletter, and contact data...')

        # Create News Categories
        if options['force'] or not NewsCategory.objects.exists():
            self.stdout.write('Creating news categories...')

            categories_data = [
                {'name': 'Announcements', 'description': 'Official announcements from NIRU'},
                {'name': 'Events', 'description': 'Upcoming and past events'},
                {'name': 'Research', 'description': 'Research updates and discoveries'},
                {'name': 'Academics', 'description': 'Academic programme updates'},
                {'name': 'Student Life', 'description': 'Student life and activities'},
            ]

            for cat_data in categories_data:
                category, created = NewsCategory.objects.get_or_create(
                    name=cat_data['name'],
                    defaults={
                        'description': cat_data['description'],
                        'slug': slugify(cat_data['name'])
                    }
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Created category: {category.name}')
                    )
                else:
                    self.stdout.write(
                        f'Skipping existing category: {category.name}'
                    )
        else:
            self.stdout.write('News categories already exist. Use --force to recreate.')

        # Create sample News Articles
        if options['force'] or not NewsArticle.objects.exists():
            self.stdout.write('Creating sample news articles...')

            # Get the 'Announcements' category
            try:
                announcements_cat = NewsCategory.objects.get(name='Announcements')
            except NewsCategory.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING('Announcements category not found, using first category or creating default')
                )
                if NewsCategory.objects.exists():
                    announcements_cat = NewsCategory.objects.first()
                else:
                    announcements_cat, _ = NewsCategory.objects.get_or_create(
                        name='General',
                        defaults={'description': 'General news and announcements', 'slug': 'general'}
                    )

            news_articles_data = [
                {
                    'title': 'NIRU Launches AI Hackathon 2025',
                    'excerpt': 'NIRU announces its inaugural AI Hackathon focusing on intelligence and security solutions.',
                    'content': '<p>National Intelligence and Research University is proud to announce the launch of its first AI Hackathon in 2025. This groundbreaking event will bring together the brightest minds to develop innovative solutions for intelligence and security challenges.</p>',
                    'author_name': 'NIRU Communications',
                    'author_title': 'Communications Team',
                    'publish_date': datetime.now(),
                    'status': 'published',
                    'is_featured': True,
                    'category': announcements_cat
                },
                {
                    'title': 'Weekly Newsletter Issue #20',
                    'excerpt': 'This week\'s edition of our newsletter featuring campus updates.',
                    'content': '<p>Stay updated with the latest happenings at NIRU. This week we feature new research initiatives, upcoming events, and student achievements.</p>',
                    'author_name': 'NIRU Editorial Team',
                    'author_title': 'Editorial Staff',
                    'publish_date': datetime.now(),
                    'status': 'published',
                    'is_featured': False,
                    'category': announcements_cat
                }
            ]

            for article_data in news_articles_data:
                article, created = NewsArticle.objects.get_or_create(
                    title=article_data['title'],
                    defaults=article_data
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Created news article: {article.title}')
                    )
                else:
                    self.stdout.write(
                        f'Skipping existing news article: {article.title}'
                    )
        else:
            self.stdout.write('News articles already exist. Use --force to recreate.')

        # Create sample Newsletter Issue
        if options['force'] or NewsletterIssue.objects.count() == 0:
            self.stdout.write('Creating sample newsletter issue...')

            issue, created = NewsletterIssue.objects.get_or_create(
                issue_number=1,
                defaults={
                    'title': 'NIRU Monthly Digest - January 2025',
                    'content': '<p>Welcome to the first issue of NIRU Monthly Digest. This newsletter brings you the latest updates from our university.</p>',
                    'recipients_count': 100
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created newsletter issue: {issue.title}')
                )
            else:
                self.stdout.write(
                    f'Skipping existing newsletter issue: {issue.title}'
                )
        else:
            self.stdout.write('Newsletter issues already exist. Use --force to recreate.')

        # Create Contact Settings if not exists
        if options['force'] or not ContactSettings.objects.exists():
            self.stdout.write('Creating contact form settings...')

            contact_settings, created = ContactSettings.objects.get_or_create(
                id=1,  # Use a fixed ID to ensure singleton
                defaults={
                    'recipient_emails': 'admin@niru.ac.ke,info@niru.ac.ke',
                    'auto_reply_enabled': True,
                    'auto_reply_subject': 'Thank you for contacting NIRU',
                    'auto_reply_message': 'Dear {name}, thank you for contacting NIRU. We have received your message and will respond shortly.',
                    'success_message': 'Thank you for your message. We will get back to you soon.'
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS('Created contact form settings')
                )
            else:
                self.stdout.write('Contact form settings already exist.')
        else:
            self.stdout.write('Contact settings already exist. Use --force to recreate.')

        self.stdout.write(
            self.style.SUCCESS('Successfully completed seeding of news, newsletter, and contact data!')
        )