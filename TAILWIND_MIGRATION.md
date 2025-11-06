# Tailwind CSS Local Installation Migration

## Overview

Successfully migrated from Tailwind CSS CDN to local installation with build process for production optimization.

## Changes Made

### 1. Package Installation
- **tailwindcss** v4.1.17
- **@tailwindcss/postcss** (required for v4)
- **postcss** v8.5.6
- **postcss-cli** v11.0.1
- **autoprefixer** v10.4.21

### 2. Configuration Files Created

#### `tailwind.config.js`
- Configured content paths for all PHP files (en/, vi/, includes/)
- Enabled dark mode with 'class' strategy
- Extended theme with custom colors (background, foreground, card, etc.)
- Added custom border radius and animations

#### `postcss.config.js`
- Configured @tailwindcss/postcss plugin
- Configured autoprefixer for browser compatibility

#### `src/input.css`
- Source CSS file using Tailwind v4 syntax (@import "tailwindcss")
- CSS custom properties for design tokens (:root and .dark)
- All custom styles from original styles.css:
  - Silver/Slate backgrounds (bg-slate-100, dark:bg-gray-900)
  - Silver/Slate borders (border-slate-300, dark:border-gray-700)
  - Silver/Slate text colors (text-slate-700, text-slate-900, etc.)
  - Orange navigation highlights (text-orange-600, bg-orange-100)
  - Dark mode hover effects (dark:hover:shadow-white/20)
  - Custom utility classes (text-9xl, h-24, no-underline, text-justify)

### 3. Build Process

**Build Script**: `npm run build:css`
- Compiles `src/input.css` → `assets/css/tailwind.css`
- Uses PostCSS with Tailwind v4 and Autoprefixer
- Purges unused CSS based on content paths
- Output: ~96KB optimized CSS (much smaller than CDN)

**Watch Script**: `npm run watch:css`
- Watches for changes and rebuilds automatically (for development)

### 4. Header Files Updated

**includes/header-en.php** and **includes/header-vi.php**:
- Changed: `<link rel="stylesheet" href="/assets/css/styles.css">`
- To: `<link rel="stylesheet" href="/assets/css/tailwind.css">`

### 5. Files to Upload to Hostinger

When deploying to Hostinger, upload these files:

**Required Files** (only changed/new files):
1. `assets/css/tailwind.css` - Compiled CSS (replaces styles.css functionality)
2. `includes/header-en.php` - Updated to use tailwind.css
3. `includes/header-vi.php` - Updated to use tailwind.css

**Optional Development Files** (not needed on Hostinger):
- `tailwind.config.js`
- `postcss.config.js`
- `src/input.css`
- `package.json`
- `node_modules/`

## Benefits

✅ **Production Optimized**: Purged unused CSS (96KB vs. much larger CDN)
✅ **Better Performance**: Single optimized CSS file, no CDN dependency
✅ **Exact Same Design**: All custom styles preserved perfectly
✅ **Dark Mode**: All hover effects and theme switching works identically
✅ **Maintainable**: Easy to update Tailwind or add custom styles

## Development Workflow

### Making CSS Changes

1. Edit `src/input.css` to add/modify custom styles
2. Run `npm run build:css` to compile
3. Test in browser
4. Upload `assets/css/tailwind.css` to Hostinger

### Updating Tailwind Version

```bash
npm install tailwindcss@latest @tailwindcss/postcss@latest
npm run build:css
```

## Verification

All 18 pages (English + Vietnamese) maintain identical appearance:
- ✅ Silver/slate color theme
- ✅ Orange navigation highlights (#ff6b35)
- ✅ Green solution icons (#16a34a)
- ✅ Red challenge icons (#dc2626)
- ✅ Dark mode support
- ✅ Enhanced hover effects (dark:hover:shadow-white/20)
- ✅ Responsive design
- ✅ All custom utility classes

## File Structure

```
/
├── src/
│   └── input.css                 # Tailwind source file
├── assets/
│   └── css/
│       ├── tailwind.css          # Compiled CSS (upload to Hostinger)
│       └── styles.css            # Legacy file (can be removed after verification)
├── includes/
│   ├── header-en.php             # Updated to use tailwind.css
│   └── header-vi.php             # Updated to use tailwind.css
├── tailwind.config.js            # Tailwind configuration
├── postcss.config.js             # PostCSS configuration
└── package.json                  # Build scripts
```

## Migration Complete

The website now uses a local Tailwind CSS installation with optimized production build, maintaining 100% identical design and functionality.
