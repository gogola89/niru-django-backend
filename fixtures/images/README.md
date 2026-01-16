# Image Directory Structure

This directory contains the image structure for the NIRU Django Backend project as specified in the image requirements.

## Directory Structure

```
fixtures/
└── images/
    ├── heroes/                    # Page hero images (11 total)
    │   ├── home-hero.jpg
    │   ├── about-hero.jpg
    │   ├── governance-hero.jpg
    │   ├── programmes-hero.jpg
    │   ├── programme-detail-hero.jpg
    │   ├── library-hero.jpg
    │   ├── student-life-hero.jpg
    │   ├── recreation-hero.jpg
    │   ├── research-hero.jpg
    │   ├── news-events-hero.jpg
    │   └── contact-hero.jpg
    ├── governance/                # Governance body images (4 total) + personnel photos
    │   ├── board-of-trustees.jpg
    │   ├── university-council.jpg
    │   ├── university-senate.jpg
    │   ├── management-board.jpg
    │   ├── chancellor-ruto.jpg
    │   ├── vc-photo.jpg
    │   ├── vc-signature.png
    │   └── noordin-haji.jpg
    ├── services/                  # Student service images (6 total)
    │   ├── lecture-rooms.jpg
    │   ├── campus-internet.jpg
    │   ├── library-resources.jpg
    │   ├── accommodation.jpg
    │   ├── recreational-facilities.jpg
    │   └── cafeteria.jpg
    ├── recreation/                # Recreation facility images (5 total)
    │   ├── swimming-pool.jpg
    │   ├── tennis-court.jpg
    │   ├── handball-pitch.jpg
    │   ├── basketball-court.jpg
    │   └── football-field.jpg
    ├── news/                      # News article images
    │   ├── ai-hackathon-2025.jpg
    │   ├── newsletter-issue-20.jpg
    │   ├── newsletter-issue-19.jpg
    │   ├── newsletter-issue-18.jpg
    │   └── thumbnails/
    │       ├── ai-hackathon-2025-thumb.jpg
    │       ├── newsletter-issue-20-thumb.jpg
    │       ├── newsletter-issue-19-thumb.jpg
    │       └── newsletter-issue-18-thumb.jpg
    └── about/                     # About section images
        ├── vc-photo.jpg
        └── vc-signature.png

media/                            # Production uploads (same structure as fixtures)
├── heroes/
├── governance/
├── services/
├── recreation/
├── news/
│   └── thumbnails/
└── about/
```

## Image Specifications

### Page Hero Images
- Resolution: 1920x600px minimum (Full HD width)
- Aspect Ratio: 16:5 (wide banner)
- Format: JPEG or WebP
- File Size: < 500KB (optimized for web)

### Governance Body Images
- Resolution: 1200x800px
- Aspect Ratio: 3:2
- Format: JPEG
- File Size: < 300KB

### Service Images
- Resolution: 800x600px
- Aspect Ratio: 4:3
- Format: JPEG
- File Size: < 200KB

### Recreation Facility Images
- Resolution: 1200x800px
- Aspect Ratio: 3:2
- Format: JPEG
- File Size: < 300KB

### News Article Images
- Featured: 1200x630px (social media optimized)
- Thumbnail: 400x225px
- Format: JPEG
- File Size: < 300KB (featured), < 50KB (thumbnail)

## Usage

- `fixtures/images/` - Contains initial placeholder images for seeding
- `media/` - Contains uploaded images in production environment
- All images are managed through the Django admin and served via API
- API returns absolute URLs for images: `https://api.niru.ac.ke/media/[category]/[filename]`