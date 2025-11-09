#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update website PHP files with exact content from bilingual-content-reviewed CSV
"""

import csv
import os
import re
from pathlib import Path

# Mapping CSV page names to PHP filenames
PAGE_FILES = {
    'Home': ['en/index.php', 'vi/index.php'],
    'Services': ['en/services.php', 'vi/services.php'],
    'Solutions': ['en/solutions.php', 'vi/solutions.php'],
    'Collaboration': ['en/collaboration.php', 'vi/collaboration.php'],
    'Contact': ['en/contact.php', 'vi/contact.php'],
    'People': ['en/people.php', 'vi/people.php'],
    'Privacy': ['en/privacy.php', 'vi/privacy.php'],
    'Terms': ['en/terms.php', 'vi/terms.php'],
    'About': ['en/about.php', 'vi/about.php']
}

def read_csv(csv_path):
    """Read CSV and organize content by page"""
    content = {}
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            page = row['Page'].strip()
            if not page or page == '':
                continue
            if page not in content:
                content[page] = []
            content[page].append({
                'section': row['Section'],
                'english': row['English'],
                'vietnamese': row['Vietnamese'],
                'notes': row['Notes']
            })
    return content

def update_file(filepath, replacements, language):
    """Update PHP file with exact text replacements"""
    print(f"\nUpdating {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    updated_count = 0
    not_found = []
    
    for item in replacements:
        old_text = item['english'] if language == 'en' else item['vietnamese']
        new_text = item['english'] if language == 'en' else item['vietnamese']
        
        if not old_text or old_text.strip() == '':
            continue
            
        # Try exact match first
        if old_text in content:
            if old_text != new_text:  # Only replace if different
                content = content.replace(old_text, new_text)
                updated_count += 1
                print(f"  ✓ Replaced: {old_text[:50]}...")
        else:
            not_found.append(old_text[:80])
    
    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  → {updated_count} replacements made")
    else:
        print(f"  → No changes needed (content already matches)")
    
    if not_found:
        print(f"  ⚠ {len(not_found)} items not found (may already be updated)")
        for item in not_found[:3]:  # Show first 3
            print(f"    - {item}...")
    
    return updated_count

def main():
    csv_path = 'attached_assets/bilingual-content-reviewed_1762687506336.csv'
    
    print("=" * 70)
    print("HealthSyncX Content Update from CSV")
    print("=" * 70)
    
    # Read CSV content
    print(f"\nReading CSV: {csv_path}")
    content = read_csv(csv_path)
    
    total_updates = 0
    
    # Update each page
    for page_name, files in PAGE_FILES.items():
        if page_name not in content:
            print(f"\nWarning: No content found for page '{page_name}' in CSV")
            continue
        
        replacements = content[page_name]
        print(f"\n{'='*70}")
        print(f"Processing {page_name} page ({len(replacements)} content items)")
        print(f"{'='*70}")
        
        for filepath in files:
            if not os.path.exists(filepath):
                print(f"  ⚠ File not found: {filepath}")
                continue
            
            # Determine language from filepath
            language = 'en' if filepath.startswith('en/') else 'vi'
            count = update_file(filepath, replacements, language)
            total_updates += count
    
    print(f"\n{'='*70}")
    print(f"Update Complete: {total_updates} total replacements made")
    print(f"{'='*70}")

if __name__ == '__main__':
    main()
