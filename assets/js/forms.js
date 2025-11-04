// HealthSyncX - Form Handling with hCaptcha
(function() {
  'use strict';

  // Get hCaptcha site key from meta tag or global variable
  const HCAPTCHA_SITEKEY = document.querySelector('meta[name="hcaptcha-sitekey"]')?.content || window.HCAPTCHA_SITEKEY;

  // Form submission handler
  function handleFormSubmit(formId, endpoint) {
    const form = document.getElementById(formId);
    if (!form) return;

    form.addEventListener('submit', async function(e) {
      e.preventDefault();

      const submitButton = form.querySelector('button[type="submit"]');
      const originalButtonText = submitButton?.textContent;
      const messageDiv = document.getElementById(formId + '-message');

      try {
        // Disable submit button
        if (submitButton) {
          submitButton.disabled = true;
          submitButton.textContent = formId.includes('contact') 
            ? (form.dataset.lang === 'vi' ? 'Đang gửi...' : 'Sending...')
            : (form.dataset.lang === 'vi' ? 'Đang gửi...' : 'Submitting...');
        }

        // Get hCaptcha token
        const hcaptchaToken = form.querySelector('[name="h-captcha-response"]')?.value;
        
        if (!hcaptchaToken) {
          throw new Error(form.dataset.lang === 'vi' 
            ? 'Vui lòng hoàn thành xác minh captcha'
            : 'Please complete the captcha verification');
        }

        // Collect form data
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
          if (key !== 'h-captcha-response' && key !== 'g-recaptcha-response') {
            data[key] = value;
          }
        });
        data.hcaptchaToken = hcaptchaToken;
        data.language = form.dataset.lang || 'en';

        // Send request
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
          // Show success message
          if (messageDiv) {
            messageDiv.className = 'p-4 bg-green-50 border border-green-200 rounded-md text-green-800 mt-4';
            messageDiv.textContent = result.message || (form.dataset.lang === 'vi' 
              ? 'Cảm ơn bạn! Chúng tôi sẽ liên hệ sớm.'
              : 'Thank you! We will contact you soon.');
            messageDiv.style.display = 'block';
          }
          
          // Reset form
          form.reset();
          
          // Reset hCaptcha
          if (window.hcaptcha) {
            window.hcaptcha.reset();
          }
        } else {
          throw new Error(result.error || 'Submission failed');
        }
      } catch (error) {
        // Show error message
        if (messageDiv) {
          messageDiv.className = 'p-4 bg-red-50 border border-red-200 rounded-md text-red-800 mt-4';
          messageDiv.textContent = error.message || (form.dataset.lang === 'vi' 
            ? 'Đã xảy ra lỗi. Vui lòng thử lại.'
            : 'An error occurred. Please try again.');
          messageDiv.style.display = 'block';
        }
      } finally {
        // Re-enable submit button
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = originalButtonText;
        }
      }
    });
  }

  // Initialize forms when DOM is ready
  function initForms() {
    handleFormSubmit('contact-form', '/php/contact.php');
    handleFormSubmit('collaboration-form', '/php/collaboration.php');
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForms);
  } else {
    initForms();
  }
})();
