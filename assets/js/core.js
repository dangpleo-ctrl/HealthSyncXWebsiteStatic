// HealthSyncX - Core JavaScript Functionality
// Dark Mode, Mobile Navigation, Smooth Scroll

(function() {
  'use strict';

  // Dark Mode Toggle
  function initDarkMode() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const htmlElement = document.documentElement;
    
    // Check for saved preference or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    htmlElement.classList.toggle('dark', savedTheme === 'dark');
    
    if (darkModeToggle) {
      // Update toggle button icon
      updateToggleIcon(savedTheme === 'dark');
      
      darkModeToggle.addEventListener('click', function() {
        const isDark = htmlElement.classList.toggle('dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        updateToggleIcon(isDark);
      });
    }
  }
  
  function updateToggleIcon(isDark) {
    const toggle = document.getElementById('dark-mode-toggle');
    if (toggle) {
      toggle.innerHTML = isDark 
        ? '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'
        : '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
    }
  }

  // Mobile Menu Toggle
  function initMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    
    if (mobileMenuButton && mobileMenu) {
      mobileMenuButton.addEventListener('click', function() {
        mobileMenu.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
      });
    }
    
    if (mobileMenuClose && mobileMenu) {
      mobileMenuClose.addEventListener('click', function() {
        mobileMenu.classList.add('hidden');
        document.body.style.overflow = '';
      });
    }
    
    // Close mobile menu when clicking outside
    if (mobileMenu) {
      mobileMenu.addEventListener('click', function(e) {
        if (e.target === mobileMenu) {
          mobileMenu.classList.add('hidden');
          document.body.style.overflow = '';
        }
      });
    }
  }

  // Smooth Scroll for Anchor Links
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
          e.preventDefault();
          document.querySelector(href).scrollIntoView({
            behavior: 'smooth'
          });
        }
      });
    });
  }

  // Initialize all functions when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initDarkMode();
      initMobileMenu();
      initSmoothScroll();
    });
  } else {
    initDarkMode();
    initMobileMenu();
    initSmoothScroll();
  }
})();
