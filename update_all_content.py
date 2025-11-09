#!/usr/bin/env python3
"""
Comprehensive script to update all website content from bilingual CSV.
Maps CSV sections to exact locations in PHP files and performs replacements.
"""

import csv
import re
from pathlib import Path
from typing import Dict, List

def load_csv_content(csv_path: str) -> Dict:
    """Load and organize CSV content by page."""
    content = {}
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            page = row['Page'].strip()
            if not page:
                continue
            if page not in content:
                content[page] = []
            content[page].append({
                'section': row['Section'].strip(),
                'english': row['English'].strip(),
                'vietnamese': row['Vietnamese'].strip(),
                'notes': row['Notes'].strip()
            })
    return content

def safe_replace(file_path: Path, old_text: str, new_text: str, context: str = "") -> bool:
    """Safely replace text in file, return True if changed."""
    if not file_path.exists():
        print(f"  ⚠ File not found: {file_path}")
        return False
    
    content = file_path.read_text(encoding='utf-8')
    
    if old_text not in content:
        if context:
            print(f"  ⚠ Text not found ({context}): {old_text[:60]}...")
        return False
    
    new_content = content.replace(old_text, new_text)
    file_path.write_text(new_content, encoding='utf-8')
    return True

def update_home_pages(content_map: Dict):
    """Update en/index.php and vi/index.php"""
    print("\n=== Updating Home Pages ===")
    
    home_content = content_map.get('Home', [])
    if not home_content:
        print("No Home content found in CSV")
        return
    
    # Create lookup dict by section
    sections = {item['section']: item for item in home_content}
    
    # Update English home page
    en_file = Path('en/index.php')
    print(f"\nUpdating {en_file}...")
    
    replacements_en = [
        # Hero section
        ('Get Free 30-Min Consultation', sections.get('Heading 2', {}).get('english', 'Free 30-Minute Strategy Session')),
        ('Building Healthcare Partnerships in Vietnam & APAC', sections.get('Text', {}).get('english', 'Building Healthcare Partnerships in Vietnam & APAC')),
        
        # Challenges section
        ('Disconnected Systems', sections.get('Heading 5', {}).get('english', 'Disconnected Systems')),
        ("Critical data trapped in legacy tools that don't communicate.", sections.get('Text 2', {}).get('english', '')),
        ('Unclear Return on Investment', sections.get('Heading 6', {}).get('english', 'Unclear Return on Investment')),
        ('Technology investments that look good on paper but never deliver measurable returns.', sections.get('Text 3', {}).get('english', '')),
        ('Workflow Friction', sections.get('Heading 7', {}).get('english', 'Workflow Friction')),
        ('New systems that disrupt how people actually work.', sections.get('Text 4', {}).get('english', '')),
        ('Security & Compliance Risks', sections.get('Heading 8', {}).get('english', 'Security & Compliance Risks')),
        ('Mounting regulatory pressure, from international to local data rules.', sections.get('Text 5', {}).get('english', '')),
        ('Resistance to Change', sections.get('Heading 9', {}).get('english', 'Resistance to Change')),
        ('Teams overwhelmed by too many tools, too little training.', sections.get('Text 6', {}).get('english', '')),
        ('Vendor Lock-In', sections.get('Heading 10', {}).get('english', 'Vendor Lock-In')),
        ('Locked into systems that limit flexibility and innovation.', sections.get('Text 7', {}).get('english', '')),
        
        # Who We Support
        ('Who We Support', sections.get('Heading 11', {}).get('english', 'Who We Support')),
        ('For Small and Mid-Sized Businesses', sections.get('Heading 12', {}).get('english', 'Small and Mid-Sized Businesses')),
        ('For Large Enterprises', sections.get('Heading 13', {}).get('english', 'Large Enterprises')),
        ('For Industry Leaders and Innovators', sections.get('Heading 14', {}).get('english', 'Industry Leaders and Innovators')),
    ]
    
    changed = 0
    for old, new in replacements_en:
        if new and safe_replace(en_file, old, new):
            changed += 1
    
    print(f"  ✓ Made {changed} replacements")
    
    # Update Vietnamese home page
    vi_file = Path('vi/index.php')
    print(f"\nUpdating {vi_file}...")
    
    replacements_vi = [
        # Hero section  
        ('Nhận Tư vấn Miễn phí 30 Phút', sections.get('Heading 2', {}).get('vietnamese', 'Đăng ký 30 phút tư vấn miễn phí')),
        ('Xây dựng Quan hệ Đối tác Y tế tại Việt Nam & APAC', sections.get('Text', {}).get('vietnamese', 'Kết nối hợp tác y tế tại Việt Nam và khu vực Châu Á – Thái Bình Dương')),
        ('Tư vấn Tích hợp Hệ thống Lấy Con người Làm Trung tâm', sections.get('Heading', {}).get('vietnamese', 'Tư vấn tích hợp hệ thống với trọng tâm là con người')),
        
        # Challenges
        ('Hệ thống Không Kết nối', sections.get('Heading 5', {}).get('vietnamese', 'Hệ thống rời rạc, thiếu kết nối')),
        ('Lợi Tức Đầu Tư Không Rõ ràng', sections.get('Heading 6', {}).get('vietnamese', 'Hiệu quả đầu tư khó đo lường')),
        ('Ma sát Quy trình Làm việc', sections.get('Heading 7', {}).get('vietnamese', 'Quy trình vận hành thiếu mượt mà')),
        ('Rủi ro Bảo mật & Tuân thủ', sections.get('Heading 8', {}).get('vietnamese', 'Rủi ro về bảo mật và tuân thủ quy định')),
        ('Kháng cự Thay đổi', sections.get('Heading 9', {}).get('vietnamese', 'Tâm lý ngại thay đổi công nghệ')),
        ('Bị Khóa với Nhà cung cấp', sections.get('Heading 10', {}).get('vietnamese', 'Phụ thuộc vào nhà cung cấp')),
        
        # Who We Support
        ('Chúng tôi Hỗ trợ Ai', sections.get('Heading 11', {}).get('vietnamese', 'Đối tượng khách hàng của chúng tôi')),
        ('Dành cho Doanh nghiệp Vừa và Nhỏ', sections.get('Heading 12', {}).get('vietnamese', 'Doanh nghiệp vừa và nhỏ')),
        ('Dành cho Doanh nghiệp Lớn', sections.get('Heading 13', {}).get('vietnamese', 'Doanh nghiệp lớn')),
        ('Dành cho Lãnh đạo Ngành và Nhà Đổi mới', sections.get('Heading 14', {}).get('vietnamese', 'Dành cho các nhà lãnh đạo và đơn vị đổi mới')),
    ]
    
    changed = 0
    for old, new in replacements_vi:
        if new and safe_replace(vi_file, old, new):
            changed += 1
    
    print(f"  ✓ Made {changed} replacements")

def main():
    """Main execution."""
    csv_path = 'attached_assets/bilingual-content-reviewed_1762690260794.csv'
    
    print("Loading CSV content...")
    content_map = load_csv_content(csv_path)
    
    print(f"\n✓ Loaded content for {len(content_map)} pages:")
    for page, items in content_map.items():
        print(f"  - {page}: {len(items)} sections")
    
    # Update pages
    update_home_pages(content_map)
    
    print("\n✅ Content update complete!")

if __name__ == '__main__':
    main()
