# HealthSyncX - Static Website

A bilingual (English/Vietnamese) corporate website for HealthSyncX, a healthcare technology consultancy platform serving the APAC region with focus on Vietnam and New Zealand markets.

## 🌟 Features

### Multilingual Support
- Full English and Vietnamese language versions
- Separate page files for each language (`/en/` and `/vi/`)
- Language selection landing page

### Pages
- **Home** - Landing page with language selector
- **Services** - Systems integration consultancy services
- **Solutions** - Industry-specific solutions (Healthcare, Beauty Tech, Education, Manufacturing)
- **Collaboration** - Partnership opportunities
- **People** - Team and company information
- **Contact** - Contact form with hCaptcha validation
- **Privacy Policy** - Data protection and privacy information
- **Terms & Conditions** - Legal terms and conditions

### Technical Features
- **Static HTML/CSS/JavaScript** with PHP backend
- **Responsive Design** - Mobile-first approach using Tailwind CSS
- **Form Processing** - PHP-based with PHPMailer for email delivery
- **Security** - hCaptcha spam protection on all forms
- **SEO Optimized** - Meta tags, semantic HTML, proper heading structure

## 🎨 Design

- **Primary Color**: Orange (#F97316) - Warmth and approachability
- **Accent Color**: Teal (#14B8A6) - Trust and healthcare professionalism
- **Framework**: Tailwind CSS via CDN
- **Typography**: System fonts with fallbacks
- **Approach**: People-first, professional B2B positioning

## 📁 Project Structure

```
HealthSyncXWebsiteStatic/
├── index.html                 # Language selection landing page
├── composer.json              # PHP dependencies (PHPMailer)
├── README.md                  # This file
├── DEPLOYMENT.md              # Deployment instructions
├── .gitignore                 # Git ignore rules
│
├── en/                        # English pages
│   ├── index.php              # Home page
│   ├── services.php           # Services page
│   ├── solutions.php          # Solutions page
│   ├── collaboration.php      # Partnership page with form
│   ├── people.php             # About/Team page
│   ├── contact.php            # Contact page with form
│   ├── privacy.php            # Privacy policy
│   └── terms.php              # Terms & conditions
│
├── vi/                        # Vietnamese pages (same structure as /en/)
│   ├── index.php
│   ├── services.php
│   ├── solutions.php
│   ├── collaboration.php
│   ├── people.php
│   ├── contact.php
│   ├── privacy.php
│   └── terms.php
│
├── php/                       # Backend form handlers
│   ├── contact.php            # Contact form processor
│   └── collaboration.php      # Partnership form processor
│
├── config/                    # Configuration files
│   ├── config.php.template    # Configuration template (copy to config.php)
│   └── README.md              # Configuration instructions
│
├── includes/                  # Reusable PHP components
│   ├── header-en.php          # English header/navigation
│   ├── header-vi.php          # Vietnamese header/navigation
│   ├── footer-en.php          # English footer
│   └── footer-vi.php          # Vietnamese footer
│
└── assets/                    # Static assets
    ├── css/
    │   └── styles.css         # Compiled Tailwind CSS
    ├── js/
    │   ├── core.js            # Core JavaScript utilities
    │   └── forms.js           # Form handling and validation
    └── images/                # All website images
        ├── healthsyncx-logo.png
        ├── hero-background.jpg
        └── ...
```

## 🚀 Local Development

### Requirements
- PHP 7.4 or higher
- Composer (for PHPMailer)
- Web server (Apache/Nginx) or PHP built-in server

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/HealthSyncXWebsiteStatic.git
   cd HealthSyncXWebsiteStatic
   ```

2. **Install PHP dependencies**
   ```bash
   composer install
   ```

3. **Configure email and captcha**
   ```bash
   cp config/config.php.template config/config.php
   ```
   
   Edit `config/config.php` and update:
   - SMTP credentials (email server settings)
   - hCaptcha secret key
   - Contact form recipient email

4. **Run local server**
   ```bash
   php -S localhost:8000
   ```

5. **Open in browser**
   ```
   http://localhost:8000
   ```

## 📧 Form Configuration

Both contact and collaboration forms require:

1. **SMTP Settings** - For sending emails via PHPMailer
   - Host: Your mail server (e.g., smtp.hostinger.com)
   - Port: Usually 465 (SSL) or 587 (TLS)
   - Username: Your email address
   - Password: Your email password

2. **hCaptcha Keys**
   - Site Key: Add to forms (already included)
   - Secret Key: Add to `config/config.php`
   - Get keys from: https://www.hcaptcha.com/

3. **Recipient Email**
   - Set in `config/config.php`
   - Default: contact@healthsyncx.org

## 🌐 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to Hostinger.

## 🔒 Security Notes

- **Never commit `config/config.php`** with real credentials (excluded via .gitignore)
- **Move config.php outside web root** on production server
- **Use environment variables** for sensitive data in production
- **Keep PHPMailer updated** via Composer

## 📝 Forms

### Contact Form
- **Fields**: Name*, Email*, Organization*, Phone*, Website (optional), Message*
- **Validation**: Client-side HTML5 + Server-side PHP
- **Protection**: hCaptcha
- **Processing**: PHP backend with PHPMailer

### Collaboration/Partnership Form
- **Fields**: Name*, Email*, Organization*, Phone*, Website (optional), Partnership Type*, Description*
- **Validation**: Client-side HTML5 + Server-side PHP
- **Protection**: hCaptcha
- **Processing**: PHP backend with PHPMailer

## 🎯 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 License

Proprietary - HealthSyncX © 2024

## 🤝 Support

For questions or issues:
- Email: contact@healthsyncx.org
- Website: https://healthsyncx.org

---

**Built with ❤️ for healthcare systems integration across APAC**
