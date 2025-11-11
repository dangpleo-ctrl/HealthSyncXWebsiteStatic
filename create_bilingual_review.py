#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract bilingual content from HealthSyncX website for review
Properly matches English and Vietnamese content side-by-side
Creates Excel-compatible CSV with UTF-8 BOM encoding
"""

import os
import re
import csv
from html.parser import HTMLParser

class ContentExtractor(HTMLParser):
    """Extract structured content from HTML"""
    
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_section = None
        self.current_tag = None
        self.in_section = False
        self.skip_tags = {'script', 'style', 'nav', 'footer', 'header', 'form', 'svg'}
        self.depth = 0
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag in self.skip_tags:
            self.depth += 1
        
        # Start new section on h2
        if tag == 'h2' and self.depth == 0:
            if self.current_section:
                self.sections.append(self.current_section)
            self.current_section = {
                'heading': '',
                'content': []
            }
    
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.depth = max(0, self.depth - 1)
        self.current_tag = None
    
    def handle_data(self, data):
        if self.depth > 0:
            return
            
        text = ' '.join(data.split()).strip()
        if not text or len(text) < 2:
            return
        
        if self.current_tag == 'h1':
            # H1 is its own section
            self.sections.append({
                'heading': 'Main Heading (H1)',
                'content': [{'type': 'h1', 'text': text}]
            })
        elif self.current_tag == 'h2':
            if self.current_section:
                self.current_section['heading'] = text
        elif self.current_tag in ['h3', 'h4', 'p', 'li', 'span', 'a', 'blockquote', 'label']:
            if self.current_section:
                self.current_section['content'].append({
                    'type': self.current_tag,
                    'text': text
                })
    
    def get_sections(self):
        if self.current_section:
            self.sections.append(self.current_section)
        return self.sections

def extract_seo_metadata(filepath):
    """Extract SEO metadata from PHP file"""
    metadata = {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(3000)
        
        # Extract page title
        match = re.search(r'\$page_title\s*=\s*["\'](.+?)["\']', content)
        if match:
            metadata['page_title'] = match.group(1)
        
        # Extract meta description
        match = re.search(r'\$meta_description\s*=\s*["\'](.+?)["\']', content, re.DOTALL)
        if match:
            metadata['meta_description'] = match.group(1).replace('\n', ' ').strip()
    
    return metadata

def extract_page_content(en_file, vi_file):
    """Extract and match content from both language files"""
    
    # Read files
    with open(en_file, 'r', encoding='utf-8') as f:
        en_html = f.read()
    
    with open(vi_file, 'r', encoding='utf-8') as f:
        vi_html = f.read()
    
    # Extract SEO metadata
    en_seo = extract_seo_metadata(en_file)
    vi_seo = extract_seo_metadata(vi_file)
    
    # Parse HTML content
    en_parser = ContentExtractor()
    en_parser.feed(en_html)
    en_sections = en_parser.get_sections()
    
    vi_parser = ContentExtractor()
    vi_parser.feed(vi_html)
    vi_sections = vi_parser.get_sections()
    
    return en_seo, vi_seo, en_sections, vi_sections

def format_content_type(tag_type):
    """Format content type for display"""
    type_map = {
        'h1': 'Main Heading (H1)',
        'h2': 'Section Heading (H2)',
        'h3': 'Subsection (H3)',
        'h4': 'Minor Heading (H4)',
        'p': 'Paragraph',
        'li': 'List Item',
        'span': 'Label/Badge',
        'a': 'Link/Button',
        'blockquote': 'Quote',
        'label': 'Form Label'
    }
    return type_map.get(tag_type, 'Text')

def match_sections(en_sections, vi_sections):
    """Match English and Vietnamese sections"""
    matched = []
    
    # Try to match sections 1-to-1
    max_sections = max(len(en_sections), len(vi_sections))
    
    for i in range(max_sections):
        en_section = en_sections[i] if i < len(en_sections) else None
        vi_section = vi_sections[i] if i < len(vi_sections) else None
        
        if en_section or vi_section:
            matched.append((en_section, vi_section))
    
    return matched

def main():
    """Main extraction function"""
    
    pages = [
        ('index.php', 'Home Page'),
        ('about.php', 'About Us'),
        ('services.php', 'Services'),
        ('solutions.php', 'Solutions'),
        ('collaboration.php', 'Collaboration'),
        ('people.php', 'Our People'),
        ('contact.php', 'Contact'),
        ('privacy.php', 'Privacy Policy'),
        ('terms.php', 'Terms & Conditions')
    ]
    
    csv_rows = []
    
    # Header row
    csv_rows.append([
        'Page',
        'Section',
        'Content Type',
        'English Text',
        'Vietnamese Text',
        'Notes'
    ])
    
    for php_file, page_name in pages:
        en_file = f'en/{php_file}'
        vi_file = f'vi/{php_file}'
        
        if not os.path.exists(en_file) or not os.path.exists(vi_file):
            print(f"⚠️  Skipping {page_name} - files not found")
            continue
        
        print(f"📄 Processing {page_name}...")
        
        # Extract content
        en_seo, vi_seo, en_sections, vi_sections = extract_page_content(en_file, vi_file)
        
        # Add SEO metadata
        if en_seo.get('page_title') or vi_seo.get('page_title'):
            csv_rows.append([
                page_name,
                'SEO Metadata',
                'Page Title',
                en_seo.get('page_title', ''),
                vi_seo.get('page_title', ''),
                'Browser tab title'
            ])
        
        if en_seo.get('meta_description') or vi_seo.get('meta_description'):
            csv_rows.append([
                page_name,
                'SEO Metadata',
                'Meta Description',
                en_seo.get('meta_description', ''),
                vi_seo.get('meta_description', ''),
                'Search engine description (150-160 chars)'
            ])
        
        # Match and add sections
        matched_sections = match_sections(en_sections, vi_sections)
        
        for section_num, (en_section, vi_section) in enumerate(matched_sections, 1):
            # Get section heading
            en_heading = en_section['heading'] if en_section else ''
            vi_heading = vi_section['heading'] if vi_section else ''
            
            section_name = en_heading or vi_heading or f'Section {section_num}'
            
            # Add section heading
            if en_heading or vi_heading:
                csv_rows.append([
                    page_name,
                    section_name,
                    'Section Heading (H2)',
                    en_heading,
                    vi_heading,
                    ''
                ])
            
            # Match content items
            en_content = en_section['content'] if en_section else []
            vi_content = vi_section['content'] if vi_section else []
            
            max_items = max(len(en_content), len(vi_content))
            
            for i in range(max_items):
                en_item = en_content[i] if i < len(en_content) else None
                vi_item = vi_content[i] if i < len(vi_content) else None
                
                en_text = en_item['text'] if en_item else ''
                vi_text = vi_item['text'] if vi_item else ''
                
                # Skip empty pairs
                if not en_text and not vi_text:
                    continue
                
                # Get content type
                content_type = format_content_type(
                    en_item['type'] if en_item else (vi_item['type'] if vi_item else 'p')
                )
                
                csv_rows.append([
                    page_name,
                    section_name,
                    content_type,
                    en_text,
                    vi_text,
                    ''
                ])
    
    # Write to CSV with UTF-8 BOM
    output_file = 'HealthSyncX_Bilingual_Content.csv'
    
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_rows)
    
    print(f"\n✅ Content extraction completed!")
    print(f"📄 File created: {output_file}")
    print(f"📊 Total rows: {len(csv_rows):,}")
    print(f"📖 Pages processed: {len(pages)}")
    print(f"\n💡 The file uses UTF-8 encoding with BOM for proper Vietnamese display in Excel.")
    print(f"   English and Vietnamese content is now properly matched side-by-side!")

if __name__ == '__main__':
    main()
