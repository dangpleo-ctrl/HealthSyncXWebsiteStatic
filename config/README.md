# Configuration Directory

## Purpose

This directory contains the **secure configuration template** for HealthSyncX. The actual configuration file with real credentials will be created **OUTSIDE** the web root on your Hostinger server.

## File Structure

```
static-site/config/
└── config.php.template    ← Template with placeholders (committed to Git)

/home/username/config/     ← On Hostinger server (OUTSIDE public_html)
└── config.php             ← Real credentials (NOT committed to Git)
```

## Setup Instructions

### On Hostinger Server:

1. **Create config directory**:
   ```bash
   mkdir -p /home/username/config
   ```

2. **Copy the template**:
   ```bash
   cp /home/username/public_html/config/config.php.template /home/username/config/config.php
   ```

   Or upload `config.php.template` to `/home/username/config/` and rename it to `config.php`

3. **Edit with real credentials**:
   ```bash
   nano /home/username/config/config.php
   ```

   Replace these placeholders:
   - `YOUR_SMTP_PASSWORD_HERE` → Your actual SMTP password
   - `YOUR_HCAPTCHA_SECRET_KEY_HERE` → Your actual hCaptcha secret key

4. **Secure the file**:
   ```bash
   chmod 600 /home/username/config/config.php
   ```

## Security Notes

✅ **DO**:
- Keep `config.php` outside `public_html/`
- Set file permissions to 600 (owner read/write only)
- Use strong passwords
- Keep template updated in version control

❌ **DON'T**:
- Never commit `config.php` with real credentials to Git
- Never place config.php inside `public_html/`
- Never make config.php world-readable
- Never share config.php contents publicly

## Verification

To verify your setup is secure:

1. Try accessing config in browser:
   ```
   https://healthsyncx.org/config/config.php
   ```
   Should return **404 Not Found** ✅

2. Check file location:
   ```bash
   ls -la /home/username/config/config.php
   ```
   Should show `-rw-------` (600 permissions) ✅

3. Verify forms work:
   - Submit a test contact form
   - Check if email is received
   - If yes, configuration is correct! ✅

## Troubleshooting

**Error: "Configuration file not found"**
- Check that `/home/username/config/config.php` exists
- Verify file permissions (should be 600 or 644)
- Check path in PHP handlers matches your server structure

**Forms submit but no email received**
- Check SMTP credentials in config.php
- Verify SMTP password is correct
- Check Hostinger email logs for errors

**hCaptcha not working**
- Verify HCAPTCHA_SECRET matches your hCaptcha account
- Check HCAPTCHA_SITEKEY is correct in HTML pages

## Support

For deployment help, see: `DEPLOY_TO_HOSTINGER.md`
