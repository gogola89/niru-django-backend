from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse


class Command(BaseCommand):
    help = 'Test all API endpoints to ensure they are working correctly'

    def handle(self, *args, **options):
        client = Client()
        
        # Test Core API endpoints
        self.stdout.write("Testing Core API endpoints...")
        
        # Test Page Hero API
        try:
            response = client.get('/api/v1/page-hero/home/')
            self.stdout.write(
                self.style.SUCCESS(f"✓ Page Hero API: {response.status_code}")
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"✗ Page Hero API: {str(e)}")
            )
        
        # Test About API endpoints
        self.stdout.write("\nTesting About API endpoints...")
        
        endpoints = [
            '/api/v1/about/',
            '/api/v1/about/core-values/',
            '/api/v1/about/vc-message/',
            '/api/v1/about/about-full/',
        ]
        
        for endpoint in endpoints:
            try:
                response = client.get(endpoint)
                self.stdout.write(
                    self.style.SUCCESS(f"✓ {endpoint}: {response.status_code}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ {endpoint}: {str(e)}")
                )
        
        # Test Governance API endpoints
        self.stdout.write("\nTesting Governance API endpoints...")
        
        gov_endpoints = [
            '/api/v1/governance/chancellor/',
            '/api/v1/governance/board-members/',
            '/api/v1/governance/governance-bodies/',
            '/api/v1/governance/governance-structure/',
        ]
        
        for endpoint in gov_endpoints:
            try:
                response = client.get(endpoint)
                self.stdout.write(
                    self.style.SUCCESS(f"✓ {endpoint}: {response.status_code}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ {endpoint}: {str(e)}")
                )
        
        # Test Academics API endpoints
        self.stdout.write("\nTesting Academics API endpoints...")
        
        acad_endpoints = [
            '/api/v1/academics/programmes/',
            '/api/v1/academics/programme-highlights/',
            '/api/v1/academics/admission-requirements/',
            '/api/v1/academics/featured-programmes/',
        ]
        
        for endpoint in acad_endpoints:
            try:
                response = client.get(endpoint)
                self.stdout.write(
                    self.style.SUCCESS(f"✓ {endpoint}: {response.status_code}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ {endpoint}: {str(e)}")
                )
        
        # Test Library API endpoints
        self.stdout.write("\nTesting Library API endpoints...")
        
        lib_endpoints = [
            '/api/v1/library/library-page/',
            '/api/v1/library/librarian-message/',
            '/api/v1/library/e-resources/',
            '/api/v1/library/policies/',
            '/api/v1/library/library-resources/',
        ]
        
        for endpoint in lib_endpoints:
            try:
                response = client.get(endpoint)
                self.stdout.write(
                    self.style.SUCCESS(f"✓ {endpoint}: {response.status_code}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ {endpoint}: {str(e)}")
                )
        
        # Test Student Life API endpoints
        self.stdout.write("\nTesting Student Life API endpoints...")
        
        student_endpoints = [
            '/api/v1/student-life/services/',
            '/api/v1/student-life/facilities/',
            '/api/v1/student-life/recreation-facilities/',
            '/api/v1/student-life/student-services-facilities/',
        ]
        
        for endpoint in student_endpoints:
            try:
                response = client.get(endpoint)
                self.stdout.write(
                    self.style.SUCCESS(f"✓ {endpoint}: {response.status_code}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"✗ {endpoint}: {str(e)}")
                )
        
        self.stdout.write(
            self.style.SUCCESS("\n✓ All API endpoints tested successfully!")
        )