#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPLETE content extraction from HealthSyncX website
Extracts EVERY text element side-by-side for EN/VI review
"""

import os
import re
import csv
from html.parser import HTMLParser

class CompleteContentExtractor(HTMLParser):
    """Extract ALL text content preserving order"""
    
    def __init__(self):
        super().__init__()
        self.content_items = []
        self.current_tag = None
        self.tag_stack = []
        self.skip_tags = {'script', 'style', 'svg', 'path'}
        self.inside_skip = 0
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        self.current_tag = tag
        
        if tag in self.skip_tags:
            self.inside_skip += 1
    
    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        
        if tag in self.skip_tags:
            self.inside_skip = max(0, self.inside_skip - 1)
        
        self.current_tag = self.tag_stack[-1] if self.tag_stack else None
    
    def handle_data(self, data):
        if self.inside_skip > 0:
            return
        
        # Clean text
        text = ' '.join(data.split()).strip()
        
        # Skip empty or very short text
        if not text or len(text) < 2:
            return
        
        # Skip common metadata/code snippets
        if text.startswith('<?php') or text.startswith('$'):
            return
        
        # Determine content type
        if self.current_tag == 'h1':
            content_type = 'H1 Heading'
        elif self.current_tag == 'h2':
            content_type = 'H2 Heading'
        elif self.current_tag == 'h3':
            content_type = 'H3 Heading'
        elif self.current_tag == 'h4':
            content_type = 'H4 Heading'
        elif self.current_tag == 'p':
            content_type = 'Paragraph'
        elif self.current_tag == 'li':
            content_type = 'List Item'
        elif self.current_tag == 'span':
            content_type = 'Label/Badge'
        elif self.current_tag == 'a':
            content_type = 'Link/Button'
        elif self.current_tag == 'label':
            content_type = 'Form Label'
        elif self.current_tag == 'button':
            content_type = 'Button'
        else:
            content_type = 'Text'
        
        self.content_items.append({
            'type': content_type,
            'text': text
        })
    
    def get_content(self):
        return self.content_items

def extract_seo_from_file(filepath):
    """Extract SEO metadata"""
    metadata = {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(3000)
            
            # Page title
            match = re.search(r'\$page_title\s*=\s*["\'](.+?)["\']', content)
            if match:
                metadata['page_title'] = match.group(1)
            
            # Meta description
            match = re.search(r'\$meta_description\s*=\s*["\'](.+?)["\']', content, re.DOTALL)
            if match:
                metadata['meta_description'] = match.group(1).replace('\n', ' ').strip()
    except:
        pass
    
    return metadata

def extract_all_content(en_file, vi_file):
    """Extract all content from both files"""
    
    # Read files
    with open(en_file, 'r', encoding='utf-8') as f:
        en_html = f.read()
    
    with open(vi_file, 'r', encoding='utf-8') as f:
        vi_html = f.read()
    
    # Extract SEO
    en_seo = extract_seo_from_file(en_file)
    vi_seo = extract_seo_from_file(vi_file)
    
    # Parse HTML
    en_parser = CompleteContentExtractor()
    en_parser.feed(en_html)
    en_content = en_parser.get_content()
    
    vi_parser = CompleteContentExtractor()
    vi_parser.feed(vi_html)
    vi_content = vi_parser.get_content()
    
    return en_seo, vi_seo, en_content, vi_content

def main():
    """Main extraction"""
    
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
    
    # Header
    csv_rows.append([
        'Page',
        'Row #',
        'Content Type',
        'English Text',
        'Vietnamese Text'
    ])
    
    for php_file, page_name in pages:
        en_file = f'en/{php_file}'
        vi_file = f'vi/{php_file}'
        
        if not os.path.exists(en_file) or not os.path.exists(vi_file):
            print(f"⚠️  Skipping {page_name}")
            continue
        
        print(f"📄 Extracting {page_name}...")
        
        en_seo, vi_seo, en_content, vi_content = extract_all_content(en_file, vi_file)
        
        row_num = 1
        
        # SEO metadata
        if en_seo.get('page_title') or vi_seo.get('page_title'):
            csv_rows.append([
                page_name,
                f'SEO-{row_num}',
                'Page Title',
                en_seo.get('page_title', ''),
                vi_seo.get('page_title', '')
            ])
            row_num += 1
        
        if en_seo.get('meta_description') or vi_seo.get('meta_description'):
            csv_rows.append([
                page_name,
                f'SEO-{row_num}',
                'Meta Description',
                en_seo.get('meta_description', ''),
                vi_seo.get('meta_description', '')
            ])
            row_num += 1
        
        # Match content items position by position
        max_items = max(len(en_content), len(vi_content))
        
        for i in range(max_items):
            en_item = en_content[i] if i < len(en_content) else None
            vi_item = vi_content[i] if i < len(vi_content) else None
            
            # Get text and type
            en_text = en_item['text'] if en_item else ''
            vi_text = vi_item['text'] if vi_item else ''
            
            # Skip completely empty pairs
            if not en_text and not vi_text:
                continue
            
            # Use English type if available, otherwise Vietnamese
            content_type = en_item['type'] if en_item else (vi_item['type'] if vi_item else 'Text')
            
            csv_rows.append([
                page_name,
                row_num,
                content_type,
                en_text,
                vi_text
            ])
            row_num += 1
    
    # Write CSV with UTF-8 BOM
    output_file = 'HealthSyncX_Complete_Content.csv'
    
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_rows)
    
    print(f"\n✅ COMPLETE extraction finished!")
    print(f"📄 File: {output_file}")
    print(f"📊 Total rows: {len(csv_rows):,}")
    print(f"📖 Pages: {len(pages)}")
    print(f"\n💡 ALL text content extracted side-by-side with Vietnamese UTF-8 BOM encoding")

if __name__ == '__main__':
    main()
