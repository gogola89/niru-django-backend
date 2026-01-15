# NIRU Backend Development Roadmap

This roadmap outlines the planned development sprints for the NIRU Django backend.

## Sprint 1: Foundation & Core Setup (Completed)
**Goal:** Establish project foundation with security-first approach and basic content models

### Completed Tasks:
- [x] Project initialization with proper separation of settings (base, dev, prod)
- [x] Virtual environment and dependency management
- [x] PostgreSQL database configuration (with SQLite for dev)
- [x] Git repository with main, staging, and dev branches
- [x] Environment variables management
- [x] Static and media files handling
- [x] Django REST Framework installation and configuration
- [x] CORS headers configuration for NextJS frontend
- [x] API versioning structure (api/v1/)
- [x] DRF settings configuration (pagination, authentication, permissions)
- [x] API authentication setup (TokenAuthentication and SessionAuthentication)
- [x] API throttling classes configuration
- [x] DRF Spectacular for API documentation
- [x] Swagger UI endpoint setup
- [x] Django Jazzmin installation and configuration
- [x] Jazzmin theme customization with NIRU branding
- [x] Admin interface layout and navigation configuration
- [x] Custom admin site title and header
- [x] Admin dashboard welcome page
- [x] Core models implementation:
  - [x] TimeStampedModel (abstract base with created_at, updated_at)
  - [x] SEOModel (meta title, description, keywords)
  - [x] PublishableModel (is_published, publish_date)
  - [x] SiteSettings model with global configurations
  - [x] PageHero model for page-specific hero sections
- [x] Model admins with proper list displays and filters
- [x] PageHeroSerializer implementation
- [x] API endpoint: `/api/v1/page-hero/{page_identifier}/`
- [x] User management and API authentication setup
- [x] Management command for data seeding

## Sprint 2: Content Management System (Planned)
**Goal:** Build comprehensive content models for all website pages

### Planned Tasks:
- [ ] Create `about` app
- [ ] Implement About Us models (AboutPage, CoreValue, ViceChancellorMessage)
- [ ] Add rich text editor functionality
- [ ] Implement image upload with validation
- [ ] Create comprehensive admin interfaces
- [ ] Create serializers and API endpoints for About Us content
- [ ] Create `governance` app
- [ ] Implement Governance models (Chancellor, BoardMember, GovernanceBody)
- [ ] Create admin interfaces with filtering
- [ ] Create serializers and API endpoints for Governance content
- [ ] Create `academics` app
- [ ] Implement Programme models (Programme, ProgrammeHighlight, AdmissionRequirement)
- [ ] Add slug fields for SEO
- [ ] Create detailed admin with inlines
- [ ] Create serializers and API endpoints for Academic Programmes
- [ ] Create `library` app
- [ ] Implement Library models (LibraryPage, LibrarianMessage, EResource, LibraryPolicy)
- [ ] Add file upload handling
- [ ] Create categorization for e-resources
- [ ] Create serializers and API endpoints for Library content
- [ ] Create `student_life` app
- [ ] Implement Student Life models (Service, Facility, RecreationFacility)
- [ ] Add image galleries functionality
- [ ] Create organized admin interfaces
- [ ] Create serializers and API endpoints for Student Life content

## Sprint 3: Dynamic Features (Planned)
**Goal:** Implement interactive features (news, events, newsletter, contact)

### Planned Tasks:
- [ ] Create `news` app with NewsArticle, NewsCategory, and Event models
- [ ] Create `newsletter` app with Subscriber and NewsletterIssue models
- [ ] Create `contact` app with ContactSubmission and ContactSettings models
- [ ] Create `research` app with Publication, ResearchArea, and ResearchProject models
- [ ] Create `resources` app with QuickLink and Download models
- [ ] Implement comprehensive API endpoints for all new models
- [ ] Add rich text editing, file uploads, and search capabilities

## Sprint 4: Data Seeding & API Testing (Planned)
**Goal:** Populate initial data and comprehensively test all API endpoints

### Planned Tasks:
- [ ] Create management commands for all content seeding
- [ ] Extract content from PDF documents into JSON/YAML files
- [ ] Write comprehensive API tests using APITestCase
- [ ] Write unit tests for serializers and models
- [ ] Complete Swagger/OpenAPI documentation
- [ ] Create Postman collection for API testing
- [ ] Implement performance optimizations

## Sprint 5: Deployment & Security Hardening (Planned)
**Goal:** Deploy to production with security best practices

### Planned Tasks:
- [ ] Production configuration setup
- [ ] Security hardening implementation
- [ ] Admin security enhancements
- [ ] Deployment setup on chosen platform
- [ ] Monitoring and logging configuration

## Current Status
Sprint 1 has been completed successfully. The foundational elements are in place including:
- Project structure with proper settings separation
- Django REST Framework with authentication and throttling
- CORS configuration for NextJS frontend
- Django Jazzmin admin interface with NIRU branding
- Core models (SiteSettings, PageHero) with admin interfaces
- API endpoint for page heroes
- Data seeding management command
- Proper branching strategy with main, staging, and dev branches