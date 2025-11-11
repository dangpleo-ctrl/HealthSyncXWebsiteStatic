<?php
$page_title = "Liên hệ";
$current_page = "contact";
$meta_description = "Liên hệ với HealthSyncX để được tư vấn chuyên môn về tích hợp hệ thống. Tư vấn miễn phí 30 phút. Phục vụ Việt Nam & Khu vực APAC.";
$canonical_url = "/vi/contact";
$en_page = "contact.php";
include '../includes/header-vi.php';
?>

<!-- hCaptcha -->
<meta name="hcaptcha-sitekey" content="5ec2caae-dac8-40fc-8fa6-ce1a0262a04a">
<script src="https://js.hcaptcha.com/1/api.js" async defer></script>

<!-- Hero -->
<section class="relative overflow-hidden">
    <div class="w-full h-64 md:h-80 lg:h-96">
        <img src="/assets/images/contact-hero.jpg" alt="Liên hệ HealthSyncX" class="w-full h-full object-cover object-center">
    </div>
</section>

<!-- Contact Form & Info -->
<section class="py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 mb-0">
            <!-- Contact Form -->
            <div class="lg:col-span-2">
                <div class="bg-slate-100 dark:bg-gray-900 border border-slate-300 dark:border-gray-700 rounded-lg p-8 hover:shadow-lg dark:hover:shadow-xl dark:hover:shadow-white/20 transition-shadow">
                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                        Liên hệ với chúng tôi
                    </h2>
                    
                    <form id="contact-form" data-lang="vi" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="space-y-2">
                                <label for="name" class="text-sm font-medium text-foreground dark:text-white">Họ và tên *</label>
                                <input
                                    id="name"
                                    name="name"
                                    type="text"
                                    required
                                    class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring"
                                />
                            </div>
                            
                            <div class="space-y-2">
                                <label for="email" class="text-sm font-medium text-foreground dark:text-white">Email *</label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    required
                                    class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring"
                                />
                            </div>
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="space-y-2">
                                <label for="company" class="text-sm font-medium text-foreground dark:text-white">Công ty/Tổ chức *</label>
                                <input
                                    id="company"
                                    name="company"
                                    type="text"
                                    required
                                    class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring"
                                />
                            </div>
                            
                            <div class="space-y-2">
                                <label for="phone" class="text-sm font-medium text-foreground dark:text-white">Điện thoại *</label>
                                <input
                                    id="phone"
                                    name="phone"
                                    type="tel"
                                    required
                                    class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring"
                                />
                            </div>
                        </div>
                        
                        <div class="space-y-2">
                            <label for="website" class="text-sm font-medium text-foreground dark:text-white">Website (nếu có)</label>
                            <input
                                id="website"
                                name="website"
                                type="url"
                                placeholder="https://"
                                class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring"
                            />
                        </div>
                        
                        <div class="space-y-2">
                            <label for="message" class="text-sm font-medium text-foreground dark:text-white">Nội dung tin nhắn *</label>
                            <textarea
                                id="message"
                                name="message"
                                required
                                rows="6"
                                class="w-full px-3 py-2 border border-input bg-background dark:bg-gray-800 dark:border-gray-600 rounded-md text-foreground dark:text-white focus:outline-none focus:ring-2 focus:ring-ring resize-none"
                            ></textarea>
                        </div>
                        
                        <!-- Consent Checkbox -->
                        <div class="flex items-start gap-3">
                            <input
                                type="checkbox"
                                id="consent"
                                name="consent"
                                required
                                class="mt-1 w-4 h-4 rounded border-input text-primary focus:ring-2 focus:ring-ring"
                            />
                            <label for="consent" class="text-sm text-muted-foreground dark:text-gray-300 leading-relaxed cursor-pointer">
                                Tôi đồng ý để HealthSyncX sử dụng thông tin tôi cung cấp để liên hệ và phản hồi yêu cầu của tôi.
                            </label>
                        </div>
                        
                        <!-- hCaptcha -->
                        <div class="flex justify-center">
                            <div class="h-captcha" data-sitekey="5ec2caae-dac8-40fc-8fa6-ce1a0262a04a"></div>
                        </div>
                        
                        <!-- Success/Error Message -->
                        <div id="contact-form-message" style="display: none;"></div>
                        
                        <button type="submit" class="w-full inline-flex items-center justify-center px-6 py-3 bg-slate-600 text-white rounded-md font-medium hover:bg-slate-700 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                            Gửi tin nhắn
                        </button>
                    </form>
                </div>
            </div>
            
            <!-- Contact Information -->
            <div class="space-y-6">
                <div class="bg-slate-100 dark:bg-gray-900 border border-slate-300 dark:border-gray-700 rounded-lg p-6 hover:shadow-lg dark:hover:shadow-xl dark:hover:shadow-white/20 transition-shadow">
                    <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-6">
                        Thông tin liên hệ
                    </h3>
                    
                    <div class="space-y-6">
                        <div class="flex gap-4">
                            <div class="flex-shrink-0 flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                            </div>
                            <div>
                                <h4 class="font-semibold text-foreground mb-1">
                                    Email
                                </h4>
                                <a href="mailto:contact@healthsyncx.org" class="text-sm text-muted-foreground dark:text-gray-300 hover:text-primary transition-colors">
                                    contact@healthsyncx.org
                                </a>
                            </div>
                        </div>
                        
                        <div class="flex gap-4">
                            <div class="flex-shrink-0 flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            </div>
                            <div>
                                <h4 class="font-semibold text-foreground mb-1">
                                    Địa điểm
                                </h4>
                                <p class="text-sm text-muted-foreground dark:text-gray-300">
                                    Việt Nam<br />
                                    New Zealand
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-slate-100 dark:bg-gray-900 border border-slate-300 dark:border-gray-700 rounded-lg p-8 hover:shadow-lg dark:hover:shadow-xl dark:hover:shadow-white/20 transition-shadow">
                    <h4 class="font-semibold text-foreground mb-3">
                        30 phút tư vấn miễn phí
                    </h4>
                    <p class="text-sm text-muted-foreground dark:text-gray-300 mb-4">
                        Đăng ký tư vấn miễn phí 30 phút để trao đổi về nhu cầu tích hợp hệ thống của bạn.
                    </p>
                    <p class="text-xs text-muted-foreground dark:text-gray-300">
                        Thời gian phản hồi: trong vòng 24 giờ
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<script src="/assets/js/forms.js"></script>

<?php include '../includes/footer-vi.php'; ?>
