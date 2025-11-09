const fs = require('fs');
const path = require('path');

// CSV escape helper
function csvEscape(text) {
  if (!text) return '';
  text = text.toString().trim().replace(/\s+/g, ' ');
  if (text.includes('"') || text.includes(',') || text.includes('\n')) {
    return '"' + text.replace(/"/g, '""') + '"';
  }
  return text;
}

const csvRows = [];
csvRows.push(['Page', 'Section', 'English Text', 'Vietnamese Text']);

function addRow(page, section, english, vietnamese) {
  csvRows.push([csvEscape(page), csvEscape(section), csvEscape(english), csvEscape(vietnamese)]);
}

// HEADER & FOOTER
addRow('header', 'Meta Keywords', 'systems integration, healthcare technology, consultancy, Vietnam, APAC, medical devices, hospital information systems', 'tích hợp hệ thống, công nghệ y tế, tư vấn, Việt Nam, APAC, thiết bị y tế, hệ thống thông tin bệnh viện');
addRow('header', 'Default Meta Description', 'HealthSyncX - People-first Systems Integration Consultancy for Healthcare, Education, Beauty Tech, and Manufacturing', 'HealthSyncX - Tư vấn Tích hợp Hệ thống Lấy Con người Làm Trung tâm cho các lĩnh vực Y tế, Giáo dục, Công nghệ Làm đẹp và Sản xuất');
addRow('header', 'Default OG Description', 'Expert technology integration consultancy for healthcare, education, beauty tech, and manufacturing', 'Tư vấn tích hợp công nghệ chuyên nghiệp cho y tế, giáo dục, công nghệ làm đẹp và sản xuất');
addRow('header', 'Default Title', 'HealthSyncX - People-first Systems Integration Consultancy', 'HealthSyncX - Tư vấn Tích hợp Hệ thống Lấy Con người Làm Trung tâm');
addRow('header', 'Navigation - Home', 'Home', 'Trang chủ');
addRow('header', 'Navigation - Services', 'Services', 'Dịch vụ');
addRow('header', 'Navigation - Solutions', 'Solutions', 'Giải pháp');
addRow('header', 'Navigation - Collaboration', 'Collaboration', 'Hợp tác');
addRow('header', 'Navigation - About', 'About Us', 'Về chúng tôi');
addRow('header', 'Navigation - People', 'Our People', 'Đội ngũ');
addRow('header', 'Navigation - Contact', 'Contact', 'Liên hệ');
addRow('header', 'Language Switcher', 'VI / EN', 'EN / VI');
addRow('header', 'Mobile Menu Title', 'Menu', 'Menu');

addRow('footer', 'Column - Services Header', 'Services', 'Dịch vụ');
addRow('footer', 'Link - Our Services', 'Our Services', 'Dịch vụ của Chúng tôi');
addRow('footer', 'Link - Industry Solutions', 'Industry Solutions', 'Giải pháp Ngành');
addRow('footer', 'Link - Partnership Opportunities', 'Partnership Opportunities', 'Cơ hội Hợp tác');
addRow('footer', 'Column - Company Header', 'Company', 'Công ty');
addRow('footer', 'Link - About Us', 'About Us', 'Về Chúng tôi');
addRow('footer', 'Link - Our People', 'Our People', 'Đội ngũ');
addRow('footer', 'Link - Contact', 'Contact', 'Liên hệ');
addRow('footer', 'Column - Legal Header', 'Legal', 'Pháp lý');
addRow('footer', 'Link - Privacy Policy', 'Privacy Policy', 'Chính sách Bảo mật');
addRow('footer', 'Link - Terms of Service', 'Terms of Service', 'Điều khoản Dịch vụ');
addRow('footer', 'Copyright', 'HealthSyncX. All rights reserved. | Based in Vietnam & New Zealand | Serving APAC Region', 'HealthSyncX. Tất cả quyền được bảo lưu. | Có trụ sở tại Việt Nam & New Zealand | Phục vụ Khu vực APAC');

// INDEX PAGE
addRow('index', 'Page Title', 'Home', 'Trang chủ');
addRow('index', 'Meta Description', 'HealthSyncX - People-first Systems Integration Consultancy for Healthcare, Beauty Tech, and diverse industries. Expert technology integration serving Vietnam & APAC Region.', 'HealthSyncX - Tư vấn Tích hợp Hệ thống Lấy Con người Làm trung tâm cho Y tế, Công nghệ Làm đẹp và các ngành công nghiệp đa dạng. Tích hợp công nghệ chuyên gia phục vụ Việt Nam & Khu vực APAC.');
addRow('index', 'Hero Badge', 'Building Healthcare Partnerships in Vietnam & APAC', 'Xây dựng Quan hệ Đối tác Y tế tại Việt Nam & APAC');
addRow('index', 'Hero Heading', 'People-first Systems Integration Consultancy', 'Tư vấn Tích hợp Hệ thống Lấy Con người Làm Trung tâm');
addRow('index', 'Hero Subheading', 'Transform your operations with seamless technology integration that puts people at the center. Expert guidance for healthcare, beauty tech, and diverse industry sectors.', 'Chuyển đổi hoạt động với tích hợp công nghệ liền mạch đặt con người làm trung tâm. Hướng dẫn chuyên môn cho y tế, công nghệ làm đẹp và các lĩnh vực đa dạng.');
addRow('index', 'CTA Button - Primary', 'Get Free 30-Min Consultation', 'Nhận Tư vấn Miễn phí 30 Phút');
addRow('index', 'CTA Button - Secondary', 'View All Services', 'Xem Tất cả Dịch vụ');
addRow('index', 'Section - Challenges Heading', 'The Challenges We See Every Day', 'Những Thách thức Chúng tôi Thấy Mỗi Ngày');
addRow('index', 'Section - Challenges Intro', 'Most of our clients come to us facing at least one of these issues:', 'Hầu hết khách hàng đến với chúng tôi đều đối mặt với ít nhất một trong những vấn đề sau:');
addRow('index', 'Challenge 1 - Heading', 'Disconnected Systems', 'Hệ thống Không Kết nối');
addRow('index', 'Challenge 1 - Description', 'Critical data trapped in legacy tools that don\'t communicate.', 'Dữ liệu quan trọng bị mắc kẹt trong các công cụ cũ không giao tiếp được với nhau.');
addRow('index', 'Challenge 2 - Heading', 'Unclear ROI', 'ROI Không Rõ ràng');
addRow('index', 'Challenge 2 - Description', 'Technology investments that look good on paper but never deliver measurable returns.', 'Đầu tư công nghệ trông tốt trên giấy nhưng không bao giờ mang lại lợi nhuận có thể đo lường được.');
addRow('index', 'Challenge 3 - Heading', 'Workflow Friction', 'Ma sát Quy trình Làm việc');
addRow('index', 'Challenge 3 - Description', 'New systems that disrupt how people actually work.', 'Hệ thống mới làm gián đoạn cách mọi người thực sự làm việc.');
addRow('index', 'Challenge 4 - Heading', 'Security & Compliance Risks', 'Rủi ro Bảo mật & Tuân thủ');
addRow('index', 'Challenge 4 - Description', 'Mounting regulatory pressure, from international to local data rules.', 'Áp lực quy định ngày càng tăng, từ quy tắc dữ liệu quốc tế đến địa phương.');
addRow('index', 'Challenge 5 - Heading', 'Resistance to Change', 'Kháng cự Thay đổi');
addRow('index', 'Challenge 5 - Description', 'Teams overwhelmed by too many tools, too little training.', 'Các nhóm bị quá tải bởi quá nhiều công cụ, quá ít đào tạo.');
addRow('index', 'Challenge 6 - Heading', 'Vendor Lock-In', 'Bị Khóa với Nhà cung cấp');
addRow('index', 'Challenge 6 - Description', 'Locked into systems that limit flexibility and innovation.', 'Bị khóa vào các hệ thống hạn chế tính linh hoạt và đổi mới.');
addRow('index', 'Section - Why Choose Us Heading', 'Why Choose Us?', 'Tại sao Chọn Chúng tôi?');
addRow('index', 'Section - Why Choose Us P1', 'Every organization feels the pressure to modernize — yet too often, the result is complexity instead of clarity. New tools don\'t connect. Data lives in silos. Teams resist change. Projects drag on with no clear ROI.', 'Mọi tổ chức đều cảm thấy áp lực phải hiện đại hóa — nhưng quá thường xuyên, kết quả là sự phức tạp thay vì rõ ràng. Các công cụ mới không kết nối. Dữ liệu tồn tại trong các hệ thống riêng lẻ. Các nhóm kháng cự thay đổi. Dự án kéo dài mà không có ROI rõ ràng.');
addRow('index', 'Section - Why Choose Us P2 (Highlighted)', 'At HealthSyncX, we help you make technology work for people — not the other way around.', 'Tại HealthSyncX, chúng tôi giúp bạn làm cho công nghệ phục vụ con người — chứ không phải ngược lại.');
addRow('index', 'Section - Why Choose Us P3', 'Our integration experts connect systems, data, and workflows so your teams can focus on results, not roadblocks.', 'Các chuyên gia tích hợp của chúng tôi kết nối hệ thống, dữ liệu và quy trình làm việc để nhóm của bạn có thể tập trung vào kết quả, không phải rào cản.');
addRow('index', 'Section - People-First Integration Heading', 'What is People-First Systems Integration?', 'Tích hợp Hệ thống Lấy Con người Làm Trung tâm là gì?');
addRow('index', 'Section - People-First Integration Intro', 'At HealthSyncX, we believe systems integration is more than just connecting technologies. True integration requires a holistic approach that puts people at the center of every solution.', 'Tại HealthSyncX, chúng tôi tin rằng tích hợp hệ thống không chỉ là kết nối các công nghệ. Tích hợp thực sự đòi hỏi một cách tiếp cận toàn diện đặt con người làm trung tâm của mọi giải pháp.');
addRow('index', 'Component 1 - Heading', 'Hardware & Devices', 'Phần cứng & Thiết bị');
addRow('index', 'Component 1 - Description', 'Medical devices, IoT sensors, equipment, and physical infrastructure', 'Thiết bị y tế, cảm biến IoT, thiết bị và cơ sở hạ tầng vật lý');
addRow('index', 'Component 2 - Heading', 'Software & Digital Solutions', 'Phần mềm & Giải pháp Số');
addRow('index', 'Component 2 - Description', 'EMR/EHR systems, PACS, management platforms, and applications', 'Hệ thống EMR/EHR, PACS, nền tảng quản lý và ứng dụng');
addRow('index', 'Component 3 - Heading', 'Networks & Cybersecurity', 'Mạng & Bảo mật Mạng');
addRow('index', 'Component 3 - Description', 'Secure connectivity, data protection, and infrastructure', 'Kết nối an toàn, bảo vệ dữ liệu và cơ sở hạ tầng');
addRow('index', 'Component 4 - Heading', 'Workflows & Processes', 'Quy trình & Luồng công việc');
addRow('index', 'Component 4 - Description', 'Optimized processes that fit organizational culture and needs', 'Quy trình tối ưu phù hợp với văn hóa và nhu cầu tổ chức');
addRow('index', 'Component 5 (Highlighted) - Heading', 'People - The Heart of Integration', 'Con người - Trái tim của Tích hợp');
addRow('index', 'Component 5 (Highlighted) - Description', 'Technology adoption readiness, comprehensive user training, ongoing support, and change management', 'Sẵn sàng áp dụng công nghệ, đào tạo người dùng toàn diện, hỗ trợ liên tục và quản lý thay đổi');
addRow('index', 'Why People-First Matters - Heading', 'Why People-First Matters', 'Tại sao Lấy Con người Làm Trung tâm Quan trọng');
addRow('index', 'Why People-First Matters - Text', 'The most sophisticated technology integration will fail without considering the people who will use it. HealthSyncX assesses user readiness, designs intuitive workflows, provides comprehensive training, and ensures ongoing support - because successful integration means successful adoption.', 'Tích hợp công nghệ tinh vi nhất sẽ thất bại nếu không xem xét những người sử dụng nó. HealthSyncX đánh giá sự sẵn sàng của người dùng, thiết kế quy trình trực quan, cung cấp đào tạo toàn diện và đảm bảo hỗ trợ liên tục - bởi vì tích hợp thành công có nghĩa là áp dụng thành công.');
addRow('index', 'Section - Core Services Heading', 'Our Core Services', 'Dịch vụ Cốt lõi của Chúng tôi');
addRow('index', 'Section - Core Services Intro', 'People-centered consultancy services designed to help you navigate technology challenges and opportunities', 'Dịch vụ tư vấn lấy con người làm trung tâm được thiết kế để giúp bạn vượt qua các thách thức và cơ hội công nghệ');
addRow('index', 'Service 1 - Heading', 'Holistic Systems Integration', 'Tích hợp Hệ thống Toàn diện');
addRow('index', 'Service 1 - Description', 'Comprehensive integration planning that encompasses hardware, software, networks, workflows, AND people - ensuring adoption success through training and support.', 'Lập kế hoạch tích hợp toàn diện bao gồm phần cứng, phần mềm, mạng, quy trình VÀ con người - đảm bảo thành công áp dụng thông qua đào tạo và hỗ trợ.');
addRow('index', 'Service 1 - CTA', 'Learn More →', 'Tìm hiểu thêm →');
addRow('index', 'Service 2 - Heading', 'Workflow Optimization', 'Tối ưu hóa Quy trình');
addRow('index', 'Service 2 - Description', 'Process analysis and redesign that respects organizational culture while introducing efficiency improvements. We optimize for both technology and people.', 'Phân tích và thiết kế lại quy trình tôn trọng văn hóa tổ chức đồng thời cải thiện hiệu quả. Chúng tôi tối ưu hóa cho cả công nghệ và con người.');
addRow('index', 'Service 3 - Heading', 'Training & Capacity Building', 'Đào tạo & Phát triển Năng lực');
addRow('index', 'Service 3 - Description', 'Comprehensive user training, adoption support, and capacity building to ensure your team can effectively use and maintain integrated systems.', 'Đào tạo người dùng toàn diện, hỗ trợ áp dụng và phát triển năng lực để đảm bảo đội ngũ của bạn có thể sử dụng và bảo trì hệ thống tích hợp hiệu quả.');
addRow('index', 'Service 4 - Heading', 'Product Development', 'Phát triển Sản phẩm');
addRow('index', 'Service 4 - Description', 'Partnering with healthcare innovators to transform ideas into market-ready solutions through comprehensive product development support, from concept validation to market entry.', 'Hợp tác với các nhà đổi mới y tế để biến ý tưởng thành giải pháp sẵn sàng ra thị trường thông qua hỗ trợ phát triển sản phẩm toàn diện, từ xác thực ý tưởng đến gia nhập thị trường.');

// Write CSV
const csvContent = csvRows.map(row => row.join(',')).join('\n');
fs.writeFileSync('bilingual-content-review.csv', csvContent, 'utf8');

console.log('CSV file created successfully!');
console.log('Total rows:', csvRows.length - 1);
console.log('Location: bilingual-content-review.csv');
