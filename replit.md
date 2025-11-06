# HealthSyncX - People-first System Integration Consultancy

## Overview

HealthSyncX is a bilingual (English/Vietnamese) healthcare technology consultancy platform serving the APAC region, with a focus on Vietnam and New Zealand markets. The application is a static HTML/CSS/JavaScript website with PHP backend for form processing, designed for deployment on Hostinger Business Web Hosting. It showcases system integration consultancy services for healthcare, education, cosmetics, and manufacturing sectors, emphasizing a "people-first" approach to technology integration.

The platform features a language selection landing page, followed by fully localized content in both English and Vietnamese, with pages for services, solutions, collaboration opportunities, company information, contact forms, privacy policy, and terms & conditions.

## Deployment

**See DEPLOYMENT.md** for complete deployment instructions including:
- Configuring SMTP and hCaptcha credentials
- Uploading files to Hostinger
- Setting proper file permissions
- Testing the deployment

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology**: Static HTML/CSS/JavaScript with PHP
- **Structure**: Bilingual pages organized in `/en/` and `/vi/` directories
- **Styling**: Tailwind CSS via CDN with custom healthcare design system
- **Design**: Professional silver/slate color theme with green (#16a34a) and red (#dc2626) accent icons
- **Responsive**: Mobile-first design supporting all device sizes
- **SEO**: Optimized meta tags, semantic HTML, and proper heading structure

**Key Design Decisions**:
- Static site architecture for maximum compatibility with Hostinger hosting
- Silver/slate color theme (bg-slate-100, border-slate-300, bg-slate-600 for buttons) for professional B2B positioning
- Green icons for solutions/benefits, red icons for challenges
- Fully responsive design with professional B2B healthcare positioning
- Language-specific directory structure (`/en/` and `/vi/`) for clear organization

### Translation System

**Architecture**: Separate page files for each language
- English pages in `/static-site/en/` directory
- Vietnamese pages in `/static-site/vi/` directory
- Shared includes for headers and footers per language
- Language switcher in navigation linking to corresponding pages

**Rationale**: Simple file-based translation approach suitable for static hosting, easy to maintain and deploy without build steps.

### Backend Architecture

**Server Framework**: PHP 7.4+ (Hostinger compatibility)
- **Form Processing**: PHP scripts in `/api/` directory
- **Email**: PHPMailer for SMTP email delivery
- **Security**: hCaptcha verification on all forms
- **Configuration**: Centralized config file at `/config/config.php`

**Email System**:
- PHPMailer with SMTP authentication (Hostinger's smtp.hostinger.com)
- Bilingual email templates (English/Vietnamese)
- Form submissions sent to: contact@healthsyncx.org
- Separate templates for contact and collaboration forms

**Key Architectural Decisions**:
- PHP backend for form processing (no Node.js, compatible with Hostinger)
- Configuration file outside web root for security
- PHPMailer for reliable email delivery
- hCaptcha for spam prevention

### Form Handling & Validation

**Technology**: 
- Client-side validation with HTML5 and JavaScript
- Hookform Resolvers with Zod schemas for validation
- Integrated with Shadcn/ui form components

**Pattern**: Server-side schemas defined with Zod are reused on client for consistent validation before API submission.

### Development Environment

**Replit Integration**:
- Vite plugins for runtime error overlay and dev banner
- Cartographer plugin for code navigation (development only)
- Hot module replacement configured for Express + Vite middleware mode

**Type Safety**:
- Strict TypeScript configuration across client, server, and shared code
- Path aliases for clean imports (`@/`, `@shared/`, `@assets/`)
- Incremental compilation for faster development

### Component Architecture

**UI Components**: 
- Atomic design pattern with Shadcn/ui providing base components
- Custom composition in page-level components
- Consistent use of Card, Button, Input, and other primitives
- Toast notifications for user feedback

**Page Structure**:
- Layout wrapper with Navigation and Footer
- Language-specific routers (EnglishRouter, VietnameseRouter)
- Consistent page structure: Hero section → Content sections → CTA
- Responsive grid layouts with mobile-first approach

### Asset Management

**Static Assets**:
- Favicon and images stored in `/attached_assets`
- Vite alias (`@assets`) for importing assets
- Google Fonts loaded via CDN (Inter, DM Sans, Fira Code, Geist Mono)

## External Dependencies

### Third-Party Services

**Database**: 
- **Neon Database** (Serverless PostgreSQL)
- Connection via `@neondatabase/serverless` adapter
- Environment variable `DATABASE_URL` required for database connection

**Future Integrations** (prepared but not implemented):
- PHPMailer or similar email service for contact form submissions
- Analytics platform (structure supports GA4 or similar)

### Key NPM Packages

**Frontend Core**:
- `react` & `react-dom`: UI framework
- `wouter`: Client-side routing
- `@tanstack/react-query`: Server state management
- `tailwindcss`: Utility-first CSS framework

**UI Components**:
- `@radix-ui/*`: Headless component primitives (accordion, dialog, dropdown, etc.)
- `class-variance-authority`: Component variant management
- `clsx` & `tailwind-merge`: Class name utilities
- `lucide-react`: Icon library

**Forms & Validation**:
- `react-hook-form`: Form state management
- `@hookform/resolvers`: Validation resolver
- `zod`: Schema validation

**Backend Core**:
- `express`: Web server framework
- `drizzle-orm`: Type-safe ORM
- `drizzle-zod`: Schema to Zod conversion
- `connect-pg-simple`: PostgreSQL session store

**Development Tools**:
- `vite`: Build tool and dev server
- `tsx`: TypeScript execution for server
- `esbuild`: Production server bundling
- `@replit/*` plugins: Development enhancements

### Build & Deployment

**Scripts**:
- `dev`: Development server with Vite middleware (port managed by Replit)
- `build`: Client build with Vite + Server build with esbuild
- `start`: Production server serving static files
- `db:push`: Push Drizzle schema changes to database

**Production Architecture**:
- Client compiled to `/dist/public`
- Server compiled to `/dist/index.js`
- Single Node.js process serves both static files and API routes
- Environment-based configuration (NODE_ENV)