from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SiteSettings, PageHero
import os


class Command(BaseCommand):
    help = 'Seed the database with initial data for NIRU website'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force creation even if data already exists',
        )

    def handle(self, *args, **options):
        self.stdout.write('Seeding initial data...')
        
        # Create SiteSettings if it doesn't exist
        if not SiteSettings.objects.exists() or options['force']:
            site_settings = SiteSettings.objects.create(
                university_name="National Intelligence and Research University",
                short_name="NIRU",
                tagline="Premier Science and Research-Intensive African University",
                address="P.O. Box 47446 - 00100, Nairobi, Kenya",
                phone_numbers=["+254 798 471845", "+254 742 093140"],
                email="admin@niru.ac.ke",
                copyright_text="Copyright 2025. National Intelligence and Research University. All Rights Reserved.",
                charter_date=None,  # Will be set later when available
                charter_by="H.E. William Samoei Ruto, President and Commander in Chief of the Kenya Defence Forces"
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created SiteSettings: {site_settings.university_name}')
            )
        else:
            self.stdout.write('SiteSettings already exists. Use --force to recreate.')
        
        # Create PageHero entries for all required pages if they don't exist
        page_hero_defaults = [
            {
                'page_identifier': 'home',
                'title': 'National Intelligence and Research University',
                'subtitle': 'Premier Science and Research-Intensive African University',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'about',
                'title': 'About NIRU',
                'subtitle': 'Our History, Mission and Vision',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'governance',
                'title': 'Governance',
                'subtitle': 'Leadership and Administrative Structure',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'programmes',
                'title': 'Academic Programmes',
                'subtitle': 'Empowering Future Leaders in Intelligence and Strategy',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'programme-detail',
                'title': '',
                'subtitle': '',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'library',
                'title': 'Library',
                'subtitle': 'Resources for Academic Excellence',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'student-life',
                'title': 'Student Life',
                'subtitle': 'Support and Services',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'recreation',
                'title': 'Recreation',
                'subtitle': 'Facilities for Wellness and Fitness',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'research',
                'title': 'Research',
                'subtitle': 'Advancing Knowledge and Innovation',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'news-events',
                'title': 'News & Events',
                'subtitle': 'Latest Updates from NIRU',
                'overlay_opacity': 50
            },
            {
                'page_identifier': 'contact',
                'title': 'Contact Us',
                'subtitle': 'Get in Touch',
                'overlay_opacity': 50
            }
        ]
        
        created_count = 0
        for hero_data in page_hero_defaults:
            page_id = hero_data['page_identifier']
            defaults = {
                'title': hero_data['title'],
                'subtitle': hero_data['subtitle'],
                'overlay_opacity': hero_data['overlay_opacity'],
                'is_active': True
            }
            
            # Since background_image is required, we'll create with a placeholder
            # In a real scenario, we'd copy actual images from fixtures
            obj, created = PageHero.objects.update_or_create(
                page_identifier=page_id,
                defaults=defaults
            )
            
            if created:
                # Set a default image path
                obj.background_image = f'heroes/{page_id}-hero.jpg'
                obj.save()
                created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created/updated {created_count} PageHero entries')
        )
        
        # If no superusers exist, create one
        if not User.objects.filter(is_superuser=True).exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@niru.ac.ke',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser: {admin_user.username}')
            )
        else:
            self.stdout.write('Superuser already exists.')
        
        self.stdout.write(
            self.style.SUCCESS('Database seeding completed successfully!')
        )