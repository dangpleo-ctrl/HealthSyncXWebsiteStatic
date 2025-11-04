# GitHub Setup Guide

Quick guide to push this repository to GitHub.

## Initial Setup

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `HealthSyncXWebsiteStatic`
3. Description: "Bilingual static website for HealthSyncX healthcare consultancy - PHP/HTML/CSS/JS"
4. Choose: **Public** or **Private**
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### 2. Initialize Local Git Repository

```bash
cd HealthSyncXWebsiteStatic
git init
git add .
git commit -m "Initial commit: HealthSyncX static website"
```

### 3. Connect to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/HealthSyncXWebsiteStatic.git
git branch -M main
git push -u origin main
```

### 4. Verify Upload

Go to: `https://github.com/YOUR_USERNAME/HealthSyncXWebsiteStatic`

You should see all files except those in `.gitignore`:
- ✅ README.md displayed on homepage
- ✅ All source files visible
- ❌ `/vendor/` excluded (will be created via Composer)
- ❌ `config/config.php` excluded (use template)

## Important Security Notes

### Files NOT in Repository (Protected by .gitignore)

- `config/config.php` - Contains SMTP passwords and API keys
- `/vendor/` - Composer dependencies (generated via `composer install`)
- Log files, temp files, OS files

### To Deploy From GitHub

When deploying to a new server:

1. Clone repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HealthSyncXWebsiteStatic.git
   cd HealthSyncXWebsiteStatic
   ```

2. Install dependencies:
   ```bash
   composer install
   ```

3. Create config from template:
   ```bash
   cp config/config.php.template config/config.php
   ```

4. Edit `config/config.php` with actual credentials

5. Follow `DEPLOYMENT.md` for full deployment steps

## Future Updates

### Making Changes

1. Edit files locally
2. Test changes
3. Commit and push:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```

### Pulling Changes

On production server:
```bash
git pull origin main
composer install  # If composer.json changed
```

## Repository Description

Add this to your GitHub repository description:

```
Bilingual (EN/VI) static website for HealthSyncX healthcare consultancy. 
Features: PHP form processing, PHPMailer integration, hCaptcha validation, 
Tailwind CSS, responsive design. Deployed on Hostinger Business Hosting.
```

## Tags to Add

```
php
tailwindcss
static-website
healthcare
bilingual
phpmailer
hcaptcha
consultancy
vietnam
```

## Branch Strategy (Optional)

For team collaboration:

```bash
# Create development branch
git checkout -b development
git push -u origin development

# Create feature branch
git checkout -b feature/new-feature
# ... make changes ...
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Then create Pull Request on GitHub
```

## Backup Strategy

GitHub serves as your version control and backup:

1. **Every commit is backed up** in GitHub
2. **Can revert to any previous version**
3. **Clone to multiple locations** for redundancy

---

**Ready to push!** 🚀
