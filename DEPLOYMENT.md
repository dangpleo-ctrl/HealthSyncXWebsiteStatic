# Deployment Guide - Hostinger Business Web Hosting

This guide provides step-by-step instructions for deploying the HealthSyncX static website to Hostinger Business Web Hosting.

## Prerequisites

- Hostinger Business Web Hosting account
- FTP/SFTP client (FileZilla, Cyberduck, or Hostinger File Manager)
- SMTP email credentials
- hCaptcha account and keys

## Step 1: Prepare Configuration File

### 1.1 Create config.php from template

```bash
cd HealthSyncXWebsiteStatic
cp config/config.php.template config/config.php
```

### 1.2 Edit config/config.php with your credentials

Open `config/config.php` and update the following:

```php
// SMTP Configuration (Hostinger Email)
define('SMTP_HOST', 'smtp.hostinger.com');
define('SMTP_PORT', 465);
define('SMTP_USERNAME', 'contact@healthsyncx.org');
define('SMTP_PASSWORD', 'YOUR_ACTUAL_EMAIL_PASSWORD'); // ⚠️ UPDATE THIS
define('SMTP_FROM_EMAIL', 'contact@healthsyncx.org');
define('SMTP_FROM_NAME', 'HealthSyncX Contact');

// hCaptcha Configuration
define('HCAPTCHA_SECRET', 'YOUR_ACTUAL_HCAPTCHA_SECRET'); // ⚠️ UPDATE THIS
define('ENABLE_HCAPTCHA', true);

// Form Configuration
define('CONTACT_FORM_RECIPIENT', 'contact@healthsyncx.org');
```

**Important**: Never commit `config.php` with real credentials to Git!

## Step 2: Install PHPMailer on Hostinger

### 2.1 Access Hostinger via SSH or File Manager

**Option A: SSH (Recommended)**
```bash
ssh u123456789@yourdomain.com
cd public_html
```

**Option B: Use Hostinger File Manager**
- Login to Hostinger hPanel
- Go to Files → File Manager
- Navigate to `public_html`

### 2.2 Install Composer dependencies

If Composer is not installed:
```bash
curl -sS https://getcomposer.org/installer | php
```

Install PHPMailer:
```bash
php composer.phar install
```

Or if Composer is globally available:
```bash
composer install
```

This will create the `vendor/` directory with PHPMailer.

## Step 3: Upload Files to Hostinger

### 3.1 File Upload Structure

Upload all files to `/public_html/` maintaining the directory structure:

```
/public_html/
├── index.html
├── composer.json
├── en/
│   └── [all PHP files]
├── vi/
│   └── [all PHP files]
├── php/
│   ├── contact.php
│   └── collaboration.php
├── includes/
│   └── [all header/footer files]
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
└── vendor/
    └── [created by composer install]
```

### 3.2 Upload Methods

**Method 1: FTP/SFTP (Recommended for bulk uploads)**
1. Open FileZilla or your FTP client
2. Connect using credentials from Hostinger hPanel
3. Navigate to `/public_html/`
4. Upload all files maintaining folder structure
5. Ensure file permissions are correct (see Step 4)

**Method 2: Hostinger File Manager**
1. Login to hPanel
2. Files → File Manager
3. Navigate to `public_html`
4. Use Upload button or drag-and-drop
5. Extract if uploaded as ZIP

## Step 4: Secure Configuration File

### 4.1 Move config.php outside web root (CRITICAL for security)

**Current location**: `/public_html/config/config.php`
**Move to**: `/home/u123456789/config/config.php`

```bash
# SSH into server
mkdir -p /home/u123456789/config
mv /public_html/config/config.php /home/u123456789/config/
```

### 4.2 Update PHP handlers to use new config path

The form handlers (`php/contact.php` and `php/collaboration.php`) are already configured to look for config outside web root:

```php
$config_path = dirname(__DIR__, 2) . '/config/config.php';
```

This path resolves to `/home/u123456789/config/config.php` when called from `/public_html/php/`.

### 4.3 Verify config path is correct

Test by submitting a form. If you get "Server configuration error", the path is incorrect.

## Step 5: Set File Permissions

### 5.1 Recommended permissions

```bash
# Directories
chmod 755 public_html/en
chmod 755 public_html/vi
chmod 755 public_html/php
chmod 755 public_html/includes
chmod 755 public_html/assets
chmod 755 public_html/assets/css
chmod 755 public_html/assets/js
chmod 755 public_html/assets/images

# PHP files
chmod 644 public_html/en/*.php
chmod 644 public_html/vi/*.php
chmod 644 public_html/php/*.php
chmod 644 public_html/includes/*.php

# Config file (OUTSIDE web root)
chmod 600 /home/u123456789/config/config.php

# Static assets
chmod 644 public_html/assets/css/*
chmod 644 public_html/assets/js/*
chmod 644 public_html/assets/images/*
chmod 644 public_html/index.html
```

### 5.2 Using File Manager

If using Hostinger File Manager:
1. Right-click file/folder → Permissions
2. Set as above (755 for directories, 644 for files, 600 for config)

## Step 6: Configure DNS and Domain

### 6.1 Point domain to Hostinger

In your domain registrar:
1. Update nameservers to Hostinger's:
   - ns1.dns-parking.com
   - ns2.dns-parking.com

Or use A records pointing to your Hostinger IP.

### 6.2 Set up in Hostinger hPanel

1. Websites → Add Website
2. Enter domain: healthsyncx.org
3. Point to `/public_html/`
4. Enable SSL certificate (Let's Encrypt - free)

## Step 7: Test the Deployment

### 7.1 Test website pages

Visit each page and verify:
- [ ] https://healthsyncx.org (language selector)
- [ ] https://healthsyncx.org/en/ (English home)
- [ ] https://healthsyncx.org/vi/ (Vietnamese home)
- [ ] All navigation links work
- [ ] Images load correctly
- [ ] CSS styling is applied

### 7.2 Test forms

**Contact Form** (`/en/contact.php` and `/vi/contact.php`):
1. Fill out all required fields
2. Complete hCaptcha
3. Submit form
4. Verify email received at `contact@healthsyncx.org`
5. Check for success message on page

**Collaboration Form** (`/en/collaboration.php` and `/vi/collaboration.php`):
1. Fill out all required fields
2. Complete hCaptcha
3. Submit form
4. Verify email received
5. Check for success message

### 7.3 Test hCaptcha

1. Submit form without completing captcha → Should show error
2. Complete captcha and submit → Should send email

## Step 8: Enable SSL/HTTPS

### 8.1 Install SSL certificate (Let's Encrypt)

In Hostinger hPanel:
1. Advanced → SSL
2. Install SSL for your domain
3. Enable "Force HTTPS redirect"

### 8.2 Update site references

Ensure all internal links use relative paths (already implemented) or HTTPS.

## Step 9: Configure Email Deliverability

### 9.1 SPF Record

Add to DNS:
```
Type: TXT
Name: @
Value: v=spf1 include:titan.email ~all
```

### 9.2 DKIM Record

1. Hostinger hPanel → Emails
2. Enable DKIM for your domain
3. Add DKIM records to DNS (provided by Hostinger)

### 9.3 Test email delivery

Send test emails from contact forms and verify:
- Emails arrive in inbox (not spam)
- "From" address shows correctly
- Reply-To works

## Troubleshooting

### Forms not sending emails

**Check 1**: Config file location
```bash
ls -la /home/u123456789/config/config.php
```

**Check 2**: SMTP credentials
- Verify username/password in config.php
- Test SMTP credentials using email client

**Check 3**: PHP error logs
```bash
tail -f /home/u123456789/domains/healthsyncx.org/logs/error.log
```

**Check 4**: PHPMailer installed
```bash
ls -la public_html/vendor/phpmailer/
```

### hCaptcha not working

**Check 1**: Site key correct in forms
- Look for `data-sitekey` in contact.php and collaboration.php

**Check 2**: Secret key correct
- Verify in config.php

**Check 3**: Domain registered with hCaptcha
- Add healthsyncx.org to hCaptcha dashboard

### 500 Internal Server Error

**Check 1**: File permissions
- PHP files should be 644
- Directories should be 755

**Check 2**: PHP syntax errors
- Check error logs
- Test PHP files individually

**Check 3**: Missing dependencies
- Run `composer install` again

### Images not loading

**Check 1**: File paths
- All images use `/assets/images/` path
- Check case sensitivity (Linux is case-sensitive)

**Check 2**: File permissions
- Images should be 644

**Check 3**: Upload complete
- Verify all image files uploaded

## Maintenance

### Update website content

1. Edit files locally
2. Test locally
3. Upload changed files via FTP
4. Clear browser cache to see changes

### Update PHPMailer

```bash
ssh u123456789@healthsyncx.org
cd public_html
composer update phpmailer/phpmailer
```

### Backup

**Automated** (Hostinger):
- Hostinger provides automatic daily backups
- Access via hPanel → Backups

**Manual**:
```bash
# Download entire site via FTP
# Or create archive:
tar -czf healthsyncx-backup-$(date +%Y%m%d).tar.gz public_html/
```

## Security Checklist

- [ ] config.php moved outside public_html
- [ ] config.php has 600 permissions (owner read/write only)
- [ ] SSL certificate installed and HTTPS enforced
- [ ] hCaptcha enabled on all forms
- [ ] PHPMailer up to date
- [ ] File permissions correct (755 directories, 644 files)
- [ ] Error display disabled in production (check php.ini)
- [ ] Email passwords not exposed in code
- [ ] .git directory not uploaded to server

## Support

For deployment issues:
- **Hostinger Support**: https://www.hostinger.com/support
- **Email**: contact@healthsyncx.org

---

**Last Updated**: November 2024
