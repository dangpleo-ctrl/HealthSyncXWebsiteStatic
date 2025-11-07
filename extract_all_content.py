#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re
from pathlib import Path
from html.parser import HTMLParser
from typing import List, Tuple

class ContentExtractor(HTMLParser):
    """Extract text content from HTML while preserving structure"""
    def __init__(self):
        super().__init__()
        self.content = []
        self.current_tag = None
        self.skip_tags = {'script', 'style', 'nav', 'footer'}
        self.depth = 0
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag not in self.skip_tags:
            self.depth += 1
            
    def handle_endtag(self, tag):
        if tag not in self.skip_tags:
            self.depth -= 1
        self.current_tag = None
        
    def handle_data(self, data):
        if self.current_tag not in self.skip_tags:
            text = data.strip()
            if text and len(text) > 1:  # Ignore single characters and empty strings
                self.content.append(text)

def clean_php_content(content: str) -> str:
    """Remove PHP tags and clean HTML"""
    # Remove PHP code blocks
    content = re.sub(r'<\?php.*?\?>', '', content, flags=re.DOTALL)
    # Remove PHP includes
    content = re.sub(r'include.*?;', '', content)
    return content

def extract_page_content(file_path: Path) -> List[str]:
    """Extract meaningful content from a PHP/HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Clean PHP content
        content = clean_php_content(content)
        
        # Extract text using parser
        parser = ContentExtractor()
        parser.feed(content)
        
        return parser.content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def match_content_sections(en_content: List[str], vi_content: List[str]) -> List[Tuple[str, str, str]]:
    """Match English and Vietnamese content sections"""
    rows = []
    max_len = max(len(en_content), len(vi_content))
    
    for i in range(max_len):
        en_text = en_content[i] if i < len(en_content) else ""
        vi_text = vi_content[i] if i < len(vi_content) else ""
        
        # Determine section type
        if en_text:
            if len(en_text) > 100:
                section = "Paragraph"
            elif en_text.isupper() or (en_text and en_text[0].isupper() and len(en_text) < 50):
                section = "Heading"
            elif any(word in en_text.lower() for word in ['click', 'learn', 'get', 'view', 'contact', 'submit']):
                section = "Button/Link"
            else:
                section = "Text"
        else:
            section = "Text"
            
        if en_text or vi_text:
            rows.append((section, en_text, vi_text))
            
    return rows

def main():
    """Extract all bilingual content and create CSV"""
    
    pages = [
        ('Landing', 'index.html', None),
        ('Home', 'en/index.php', 'vi/index.php'),
        ('Services', 'en/services.php', 'vi/services.php'),
        ('Solutions', 'en/solutions.php', 'vi/solutions.php'),
        ('Collaboration', 'en/collaboration.php', 'vi/collaboration.php'),
        ('About', 'en/about.php', 'vi/about.php'),
        ('People', 'en/people.php', 'vi/people.php'),
        ('Contact', 'en/contact.php', 'vi/contact.php'),
        ('Privacy', 'en/privacy.php', 'vi/privacy.php'),
        ('Terms', 'en/terms.php', 'vi/terms.php'),
    ]
    
    # Prepare CSV data
    csv_rows = [['Page', 'Section', 'English', 'Vietnamese', 'Notes']]
    
    for page_name, en_path, vi_path in pages:
        print(f"Processing {page_name}...")
        
        # Special handling for landing page
        if page_name == 'Landing':
            csv_rows.append([])
            csv_rows.append(['Landing', 'Heading', 'Welcome', 'Welcome', ''])
            csv_rows.append(['Landing', 'Button 1', 'English', 'English', ''])
            csv_rows.append(['Landing', 'Button 2', 'Tiếng Việt', 'Tiếng Việt', ''])
            csv_rows.append(['Landing', 'Tagline', 'Based in Vietnam & New Zealand | Serving APAC Region', 
                           'Based in Vietnam & New Zealand | Serving APAC Region', ''])
            continue
        
        # Extract content from both language versions
        en_content = extract_page_content(Path(en_path)) if en_path else []
        vi_content = extract_page_content(Path(vi_path)) if vi_path else []
        
        # Match sections
        sections = match_content_sections(en_content, vi_content)
        
        # Add to CSV with page breaks
        if sections:
            csv_rows.append([])  # Empty row for separation
            
        section_counter = {}
        for section_type, en_text, vi_text in sections:
            # Number duplicate section types
            if section_type in section_counter:
                section_counter[section_type] += 1
                section_label = f"{section_type} {section_counter[section_type]}"
            else:
                section_counter[section_type] = 1
                section_label = section_type
                
            csv_rows.append([page_name, section_label, en_text, vi_text, ''])
    
    # Write CSV with UTF-8 BOM for Excel compatibility
    output_file = 'bilingual-content-review.csv'
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(csv_rows)
    
    print(f"\n✓ Created {output_file} with {len(csv_rows)} rows")
    print(f"  Encoding: UTF-8 with BOM (Excel compatible)")
    print(f"  Pages processed: {len(pages)}")

if __name__ == '__main__':
    main()
