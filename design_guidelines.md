# HealthSyncX Corporate Website Design Guidelines

## Design Approach

**Design System**: Material Design 3 principles adapted for B2B healthcare
**Rationale**: Enterprise healthcare demands trust, stability, and accessibility. Material Design provides robust component patterns, excellent dark mode support, and professional polish suitable for corporate clients.

**Key Design Principles**:
- Professional credibility through structured layouts
- Clear information hierarchy for text-heavy content
- Consistent, predictable patterns across all pages
- Accessibility-first for healthcare compliance

## Typography System

**Font Families**: 
- Primary: Inter (headings, UI elements) - via Google Fonts
- Secondary: Source Sans Pro (body text, long-form content) - via Google Fonts

**Type Scale**:
- Hero Headlines: text-5xl md:text-6xl, font-bold, tracking-tight
- Page Titles: text-4xl md:text-5xl, font-bold
- Section Headers: text-3xl md:text-4xl, font-semibold
- Card Titles: text-xl md:text-2xl, font-semibold
- Body Large: text-lg, leading-relaxed
- Body Standard: text-base, leading-relaxed
- Body Small: text-sm
- Captions: text-xs, uppercase, tracking-wide, font-medium

## Layout System

**Spacing Primitives**: Consistently use Tailwind units of **4, 6, 8, 12, 16, 20, 24** (e.g., p-4, gap-8, mt-12, py-20)

**Container Strategy**:
- Full-width sections: w-full with max-w-7xl mx-auto px-6 md:px-8
- Content sections: max-w-6xl mx-auto
- Text-heavy sections: max-w-4xl mx-auto
- Reading content: max-w-prose mx-auto

**Grid Patterns**:
- Services/Solutions: 3-column grid (grid-cols-1 md:grid-cols-2 lg:grid-cols-3)
- Features: 2-column (grid-cols-1 lg:grid-cols-2)
- Team/People: 4-column grid (grid-cols-1 sm:grid-cols-2 lg:grid-cols-4)
- Mobile: Always stack to single column

## Component Library

### Navigation Header
- Sticky header with subtle elevation shadow
- Logo left, main navigation center-right, language toggle + CTA right
- Desktop: Horizontal menu items with subtle underline on active
- Mobile: Hamburger menu with full-screen overlay
- Include "Request Demo" primary CTA button

### Hero Sections
**Home Page Hero**:
- Full-width, 75vh minimum height
- Large professional hero image (healthcare technology context: modern hospital/medical tech collaboration)
- Overlay gradient for text readability
- Centered content: headline, 2-line subheading, dual CTA (primary + secondary)
- Buttons with backdrop-blur-md for glass effect on images
- Trust indicators below: "Trusted by 50+ Healthcare Organizations" with client logo strip

**Internal Page Heroes**:
- Shorter height (40-50vh)
- Breadcrumb navigation above title
- Page title + 1-line description
- Contextual background image (services: consultation imagery, about: team collaboration)

### Card Components
**Service/Solution Cards**:
- Elevated cards with hover lift effect (shadow transition)
- Icon top (Heroicons via CDN - use outline style)
- Title, 2-3 line description
- "Learn More" link with arrow
- Consistent padding: p-8
- Rounded corners: rounded-xl

**Insight/Blog Cards**:
- Horizontal layout on desktop (image left, content right)
- Vertical stack on mobile
- Category tag, title, excerpt, read time
- "Read Article" link

### Icon Sections
**Why Choose Us / Value Props**:
- Icon + Title + Description pattern
- Icons from Heroicons (64x64px size, stroke-width-1.5)
- 3-column grid on desktop
- Icons positioned top-center of each cell
- Generous spacing between icon and text (gap-6)

### Trust Elements
**Client Logos Section**:
- Grayscale logo grid on light mode, opacity-adjusted on dark
- 6-8 logos per row, 2 rows max
- Logos sized uniformly (h-12 to h-16)

**Testimonial Cards**:
- Quote icon (Heroicons quote mark)
- Testimonial text in larger font (text-lg)
- Author info: photo (small circular), name, title, organization
- 2-column grid for multiple testimonials

### Forms
**Contact Form**:
- 2-column layout: form left (60%), contact info/map right (40%)
- Input fields with clear labels above
- Consistent height inputs (h-12)
- Textarea for message (min-h-32)
- Form validation states (error borders, helper text)
- Submit button full-width on mobile

### Footer
**Multi-section Footer**:
- 4-column grid (Company, Services, Resources, Contact)
- Logo and tagline in first column
- Email subscription form in contact column
- Social media icons (Heroicons - 24x24)
- Bottom bar: Copyright, Privacy, Terms links
- Language toggle repeated

### People/Team Page
- Grid layout with profile cards
- Photo (circular or rounded-square), name, role, bio excerpt
- LinkedIn icon link per person
- Filter by department/expertise (tabs or dropdown)

## Page-Specific Layouts

### Home Page Structure
1. Hero with CTA
2. Client Logo Trust Bar
3. Services Overview (3 cards)
4. Solutions Highlight (2-column: text + visual)
5. Why Choose Us (icon grid, 6 items)
6. Case Study Spotlight (full-width card)
7. Testimonials (2 cards)
8. CTA Section ("Ready to Transform Healthcare?")

### Services/Solutions Pages
1. Hero
2. Overview text section
3. Service/Solution cards grid (3-column, 6-9 items)
4. Process timeline (horizontal on desktop, vertical mobile)
5. Related case studies
6. CTA section

### About Page
1. Hero with company vision image
2. Story section (2-column: text + timeline graphic)
3. Mission/Vision/Values (3 cards)
4. Leadership team preview (link to People page)
5. Certifications/Partnerships (logo grid)

### Collaboration Page
1. Hero
2. Partnership models (card grid)
3. Process workflow (illustrated steps)
4. Partner testimonials
5. Partnership inquiry form

## Images

**Hero Images**:
- **Home**: Modern hospital corridor with natural light, healthcare professionals collaborating with digital displays (1920x1080, high quality)
- **Services**: Close-up of hands working on healthcare technology interface/tablet (1920x800)
- **Solutions**: Wide shot of modern medical facility with integrated technology (1920x800)
- **About**: Team collaboration in modern office setting, diverse professionals (1920x800)
- **Collaboration**: Handshake or partnership imagery in professional context (1920x800)

**Supporting Images**:
- Service cards: Icon-based (no images)
- Case studies: Project screenshots or results visualizations (800x600)
- Testimonials: Professional headshots (200x200, circular crop)
- Team/People: Professional portraits (400x400)

All hero images should have subtle gradient overlays (dark to transparent) for text legibility.

## Accessibility & Dark Mode

- Maintain WCAG AA contrast ratios (4.5:1 text, 3:1 UI)
- All interactive elements: min 44x44px touch targets
- Focus indicators: 2px outline with appropriate contrast
- Dark mode: Automatically adjust card elevations, reduce image brightness slightly
- Bilingual toggle clearly labeled with flags or language codes

## Animations

**Minimal, Purposeful Only**:
- Card hover: Subtle lift (translateY -2px) + shadow transition
- Hero CTA: Pulse animation on initial load (once, 2 seconds)
- Scroll-triggered: Fade-in for section headers (subtle, no excessive motion)
- NO: Parallax, continuous animations, distracting effects