#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Semantic content extraction with intelligent EN/VI matching
Matches content by structure and meaning, not position
"""

import os
import re
import csv
from html.parser import HTMLParser
from difflib import SequenceMatcher

class SemanticExtractor(HTMLParser):
    """Extract content organized by semantic sections"""
    
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_section = None
        self.current_tag = None
        self.tag_stack = []
        self.skip_tags = {'script', 'style', 'svg', 'path', 'nav', 'footer'}
        self.inside_skip = 0
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        self.current_tag = tag
        
        if tag in self.skip_tags:
            self.inside_skip += 1
        
        # Start new section on H1 or H2
        if tag in ['h1', 'h2'] and self.inside_skip == 0:
            if self.current_section and self.current_section['items']:
                self.sections.append(self.current_section)
            self.current_section = {
                'heading_type': tag,
                'heading_text': '',
                'items': []
            }
    
    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        
        if tag in self.skip_tags:
            self.inside_skip = max(0, self.inside_skip - 1)
        
        self.current_tag = self.tag_stack[-1] if self.tag_stack else None
    
    def handle_data(self, data):
        if self.inside_skip > 0:
            return
        
        text = ' '.join(data.split()).strip()
        
        if not text or len(text) < 2:
            return
        
        if text.startswith('<?php') or text.startswith('$'):
            return
        
        # Determine content type
        content_type = 'Text'
        if self.current_tag == 'h1':
            content_type = 'H1'
        elif self.current_tag == 'h2':
            content_type = 'H2'
        elif self.current_tag == 'h3':
            content_type = 'H3'
        elif self.current_tag == 'h4':
            content_type = 'H4'
        elif self.current_tag == 'p':
            content_type = 'Paragraph'
        elif self.current_tag == 'li':
            content_type = 'List Item'
        elif self.current_tag == 'span':
            content_type = 'Span'
        elif self.current_tag == 'a':
            content_type = 'Link'
        elif self.current_tag == 'label':
            content_type = 'Label'
        
        # Add to section
        if self.current_section is not None:
            if self.current_tag in ['h1', 'h2'] and not self.current_section['heading_text']:
                self.current_section['heading_text'] = text
            else:
                self.current_section['items'].append({
                    'type': content_type,
                    'text': text
                })
    
    def get_sections(self):
        if self.current_section and self.current_section['items']:
            self.sections.append(self.current_section)
        return self.sections

def normalize_heading(text):
    """Normalize heading for comparison"""
    return text.lower().strip().replace('?', '').replace('!', '')

def calculate_similarity(text1, text2):
    """Calculate text similarity score"""
    return SequenceMatcher(None, normalize_heading(text1), normalize_heading(text2)).ratio()

def match_sections(en_sections, vi_sections):
    """Match EN and VI sections by heading similarity"""
    matched = []
    used_vi = set()
    
    for en_section in en_sections:
        en_heading = en_section['heading_text']
        best_match = None
        best_score = 0
        
        # Try to find matching VI section
        for i, vi_section in enumerate(vi_sections):
            if i in used_vi:
                continue
            
            vi_heading = vi_section['heading_text']
            
            # Check if headings are both present
            if not en_heading or not vi_heading:
                continue
            
            # Calculate similarity
            score = calculate_similarity(en_heading, vi_heading)
            
            # Also check if both have similar number of items
            item_ratio = min(len(en_section['items']), len(vi_section['items'])) / max(len(en_section['items']), len(vi_section['items']), 1)
            
            # Combined score
            combined_score = (score * 0.7) + (item_ratio * 0.3)
            
            if combined_score > best_score:
                best_score = combined_score
                best_match = i
        
        if best_match is not None and best_score > 0.3:
            matched.append((en_section, vi_sections[best_match]))
            used_vi.add(best_match)
        else:
            matched.append((en_section, None))
    
    # Add unmatched VI sections
    for i, vi_section in enumerate(vi_sections):
        if i not in used_vi:
            matched.append((None, vi_section))
    
    return matched

def align_section_items(en_items, vi_items):
    """Align items within a section"""
    aligned = []
    
    # Group by content type
    en_by_type = {}
    vi_by_type = {}
    
    for item in en_items:
        item_type = item['type']
        if item_type not in en_by_type:
            en_by_type[item_type] = []
        en_by_type[item_type].append(item)
    
    for item in vi_items:
        item_type = item['type']
        if item_type not in vi_by_type:
            vi_by_type[item_type] = []
        vi_by_type[item_type].append(item)
    
    # Get all types
    all_types = sorted(set(list(en_by_type.keys()) + list(vi_by_type.keys())))
    
    for item_type in all_types:
        en_list = en_by_type.get(item_type, [])
        vi_list = vi_by_type.get(item_type, [])
        
        # Align 1-to-1
        max_len = max(len(en_list), len(vi_list))
        for i in range(max_len):
            en_item = en_list[i] if i < len(en_list) else None
            vi_item = vi_list[i] if i < len(vi_list) else None
            aligned.append((en_item, vi_item))
    
    return aligned

def extract_seo(filepath):
    """Extract SEO metadata"""
    metadata = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(3000)
            match = re.search(r'\$page_title\s*=\s*["\'](.+?)["\']', content)
            if match:
                metadata['page_title'] = match.group(1)
            match = re.search(r'\$meta_description\s*=\s*["\'](.+?)["\']', content, re.DOTALL)
            if match:
                metadata['meta_description'] = match.group(1).replace('\n', ' ').strip()
    except:
        pass
    return metadata

def main():
    """Main extraction with semantic matching"""
    
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
    csv_rows.append(['Page', 'Section', 'Type', 'English Text', 'Vietnamese Text'])
    
    for php_file, page_name in pages:
        en_file = f'en/{php_file}'
        vi_file = f'vi/{php_file}'
        
        if not os.path.exists(en_file) or not os.path.exists(vi_file):
            print(f"⚠️  Skipping {page_name}")
            continue
        
        print(f"📄 Processing {page_name}...")
        
        # Extract SEO
        en_seo = extract_seo(en_file)
        vi_seo = extract_seo(vi_file)
        
        if en_seo.get('page_title') or vi_seo.get('page_title'):
            csv_rows.append([
                page_name,
                'SEO',
                'Page Title',
                en_seo.get('page_title', ''),
                vi_seo.get('page_title', '')
            ])
        
        if en_seo.get('meta_description') or vi_seo.get('meta_description'):
            csv_rows.append([
                page_name,
                'SEO',
                'Meta Description',
                en_seo.get('meta_description', ''),
                vi_seo.get('meta_description', '')
            ])
        
        # Parse HTML
        with open(en_file, 'r', encoding='utf-8') as f:
            en_html = f.read()
        with open(vi_file, 'r', encoding='utf-8') as f:
            vi_html = f.read()
        
        en_parser = SemanticExtractor()
        en_parser.feed(en_html)
        en_sections = en_parser.get_sections()
        
        vi_parser = SemanticExtractor()
        vi_parser.feed(vi_html)
        vi_sections = vi_parser.get_sections()
        
        # Match sections
        matched_sections = match_sections(en_sections, vi_sections)
        
        for en_section, vi_section in matched_sections:
            # Get section info
            section_name = ''
            if en_section:
                section_name = en_section['heading_text'] or 'Content'
            elif vi_section:
                section_name = vi_section['heading_text'] or 'Content'
            
            # Add heading row
            en_heading = en_section['heading_text'] if en_section else ''
            vi_heading = vi_section['heading_text'] if vi_section else ''
            
            if en_heading or vi_heading:
                heading_type = 'H1' if (en_section and en_section['heading_type'] == 'h1') or (vi_section and vi_section['heading_type'] == 'h1') else 'H2'
                csv_rows.append([
                    page_name,
                    section_name,
                    heading_type,
                    en_heading,
                    vi_heading
                ])
            
            # Align items within section
            en_items = en_section['items'] if en_section else []
            vi_items = vi_section['items'] if vi_section else []
            
            aligned_items = align_section_items(en_items, vi_items)
            
            for en_item, vi_item in aligned_items:
                en_text = en_item['text'] if en_item else ''
                vi_text = vi_item['text'] if vi_item else ''
                content_type = en_item['type'] if en_item else (vi_item['type'] if vi_item else 'Text')
                
                if en_text or vi_text:
                    csv_rows.append([
                        page_name,
                        section_name,
                        content_type,
                        en_text,
                        vi_text
                    ])
    
    # Write CSV
    output_file = 'HealthSyncX_Semantic_Aligned.csv'
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_rows)
    
    print(f"\n✅ Semantic alignment complete!")
    print(f"📄 File: {output_file}")
    print(f"📊 Rows: {len(csv_rows):,}")
    print(f"💡 Content matched by semantic structure, not position")

if __name__ == '__main__':
    main()
