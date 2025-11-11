#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract bilingual content from HealthSyncX website for review
Creates an Excel-compatible CSV file with UTF-8 BOM encoding
"""

import os
import re
import csv
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    """Extract text content from HTML while preserving structure"""
    
    def __init__(self):
        super().__init__()
        self.current_tag = None
        self.current_attrs = {}
        self.text_items = []
        self.in_script = False
        self.in_style = False
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_attrs = dict(attrs)
        if tag in ['script', 'style']:
            if tag == 'script':
                self.in_script = True
            else:
                self.in_style = True
    
    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
        elif tag == 'style':
            self.in_style = False
        self.current_tag = None
        self.current_attrs = {}
    
    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        
        # Clean up whitespace
        text = ' '.join(data.split())
        if text and len(text.strip()) > 0:
            tag_info = {
                'tag': self.current_tag,
                'text': text.strip(),
                'attrs': self.current_attrs
            }
            self.text_items.append(tag_info)

def extract_php_metadata(filepath):
    """Extract PHP variables from the beginning of the file"""
    metadata = {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(2000)  # Read first 2000 chars for metadata
        
        # Extract page_title
        match = re.search(r'\$page_title\s*=\s*["\'](.+?)["\']', content)
        if match:
            metadata['page_title'] = match.group(1)
        
        # Extract meta_description
        match = re.search(r'\$meta_description\s*=\s*["\'](.+?)["\']', content, re.DOTALL)
        if match:
            metadata['meta_description'] = match.group(1).strip()
    
    return metadata

def extract_content_from_file(filepath):
    """Extract all text content from a PHP file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata
    metadata = extract_php_metadata(filepath)
    
    # Extract HTML content
    parser = TextExtractor()
    parser.feed(content)
    
    return metadata, parser.text_items

def categorize_content(text_item):
    """Categorize content based on HTML tag and context"""
    tag = text_item.get('tag', '')
    text = text_item.get('text', '')
    
    if tag == 'h1':
        return 'Main Heading (H1)'
    elif tag == 'h2':
        return 'Section Heading (H2)'
    elif tag == 'h3':
        return 'Subsection Heading (H3)'
    elif tag == 'h4':
        return 'Minor Heading (H4)'
    elif tag == 'p':
        return 'Paragraph'
    elif tag == 'a':
        return 'Link Text'
    elif tag == 'span':
        return 'Label/Badge'
    elif tag == 'li':
        return 'List Item'
    elif tag == 'button':
        return 'Button Text'
    elif tag == 'label':
        return 'Form Label'
    elif tag == 'blockquote':
        return 'Quote'
    else:
        return 'Text Content'

def main():
    """Main extraction function"""
    
    pages = [
        ('index.php', 'Home'),
        ('about.php', 'About Us'),
        ('services.php', 'Services'),
        ('solutions.php', 'Solutions'),
        ('collaboration.php', 'Collaboration'),
        ('people.php', 'Our People'),
        ('contact.php', 'Contact'),
        ('privacy.php', 'Privacy Policy'),
        ('terms.php', 'Terms & Conditions')
    ]
    
    csv_data = []
    
    # Add header row
    csv_data.append(['Page', 'Content Type', 'Section', 'English Text', 'Vietnamese Text', 'Notes'])
    
    for php_file, page_name in pages:
        en_file = f'en/{php_file}'
        vi_file = f'vi/{php_file}'
        
        if not os.path.exists(en_file) or not os.path.exists(vi_file):
            print(f"Skipping {php_file} - files not found")
            continue
        
        print(f"Processing {page_name}...")
        
        # Extract content
        en_metadata, en_items = extract_content_from_file(en_file)
        vi_metadata, vi_items = extract_content_from_file(vi_file)
        
        # Add SEO metadata
        if 'page_title' in en_metadata or 'page_title' in vi_metadata:
            csv_data.append([
                page_name,
                'SEO - Page Title',
                'Meta Tag',
                en_metadata.get('page_title', ''),
                vi_metadata.get('page_title', ''),
                'Browser tab title'
            ])
        
        if 'meta_description' in en_metadata or 'meta_description' in vi_metadata:
            csv_data.append([
                page_name,
                'SEO - Meta Description',
                'Meta Tag',
                en_metadata.get('meta_description', ''),
                vi_metadata.get('meta_description', ''),
                'Search engine description'
            ])
        
        # Match up English and Vietnamese content
        # This is a simple approach - match by index
        max_items = max(len(en_items), len(vi_items))
        
        for i in range(max_items):
            en_item = en_items[i] if i < len(en_items) else {}
            vi_item = vi_items[i] if i < len(vi_items) else {}
            
            en_text = en_item.get('text', '')
            vi_text = vi_item.get('text', '')
            
            # Skip empty rows
            if not en_text and not vi_text:
                continue
            
            # Skip very short non-meaningful text
            if len(en_text) < 3 and len(vi_text) < 3:
                continue
            
            content_type = categorize_content(en_item if en_item else vi_item)
            
            csv_data.append([
                page_name,
                content_type,
                f'Item {i+1}',
                en_text,
                vi_text,
                ''
            ])
    
    # Write to CSV with UTF-8 BOM for Excel compatibility
    output_file = 'HealthSyncX_Bilingual_Content_Review.csv'
    
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
    
    print(f"\n✅ Content extracted successfully!")
    print(f"📄 File created: {output_file}")
    print(f"📊 Total rows: {len(csv_data)}")
    print(f"\nThe file uses UTF-8 encoding with BOM for proper Vietnamese character display in Excel.")

if __name__ == '__main__':
    main()
