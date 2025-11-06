<!DOCTYPE html>
<html lang="en" class="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?php echo isset($meta_description) ? htmlspecialchars($meta_description) : 'HealthSyncX - People-first Systems Integration Consultancy for Healthcare, Education, Beauty Tech, and Manufacturing'; ?>">
    <meta name="keywords" content="systems integration, healthcare technology, consultancy, Vietnam, APAC, medical devices, hospital information systems">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="<?php echo isset($page_title) ? htmlspecialchars($page_title) : 'HealthSyncX'; ?>">
    <meta property="og:description" content="<?php echo isset($meta_description) ? htmlspecialchars($meta_description) : 'Expert technology integration consultancy for healthcare, education, beauty tech, and manufacturing'; ?>">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://healthsyncx.org<?php echo isset($canonical_url) ? htmlspecialchars($canonical_url) : ''; ?>">
    
    <title><?php echo isset($page_title) ? htmlspecialchars($page_title) . ' - HealthSyncX' : 'HealthSyncX - People-first Systems Integration Consultancy'; ?></title>
    
    <link rel="stylesheet" href="/assets/css/tailwind.css">
    <link rel="stylesheet" href="/assets/css/styles.css">
    <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg">
</head>
<body>
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-background border-b border-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-28">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="/en/" class="flex items-center">
                        <img src="/assets/images/healthsyncx-logo.png" alt="HealthSyncX" class="h-24" />
                    </a>
                </div>
                
                <!-- Desktop Navigation -->
                <div class="hidden md:flex items-center space-x-6">
                    <a href="/en/" class="<?php echo (isset($current_page) && $current_page === 'home') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Home</a>
                    <a href="/en/services.php" class="<?php echo (isset($current_page) && $current_page === 'services') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Services</a>
                    <a href="/en/solutions.php" class="<?php echo (isset($current_page) && $current_page === 'solutions') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Solutions</a>
                    <a href="/en/collaboration.php" class="<?php echo (isset($current_page) && $current_page === 'collaboration') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Collaboration</a>
                    <a href="/en/about.php" class="<?php echo (isset($current_page) && $current_page === 'about') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">About Us</a>
                    <a href="/en/people.php" class="<?php echo (isset($current_page) && $current_page === 'people') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Our People</a>
                    <a href="/en/contact.php" class="<?php echo (isset($current_page) && $current_page === 'contact') ? 'text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:text-orange-600'; ?> transition-colors no-underline">Contact</a>
                </div>
                
                <!-- Right side buttons -->
                <div class="flex items-center gap-3">
                    <!-- Language Switcher -->
                    <a href="/vi/<?php echo isset($vi_page) ? $vi_page : ''; ?>" class="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors no-underline" title="Switch to Vietnamese">VI</a>
                    
                    <!-- Dark Mode Toggle -->
                    <button id="dark-mode-toggle" class="p-2 text-foreground hover:bg-accent rounded-md transition-colors" aria-label="Toggle dark mode">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                    </button>
                    
                    <!-- Mobile Menu Button -->
                    <button id="mobile-menu-button" class="md:hidden p-2 text-foreground hover:bg-accent rounded-md" aria-label="Open mobile menu">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>
    
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="hidden fixed inset-0 z-50 bg-background/80 backdrop-blur-sm md:hidden">
        <div class="fixed inset-y-0 right-0 w-full max-w-sm bg-card border-l border-border shadow-xl">
            <div class="flex items-center justify-between p-4 border-b border-border">
                <span class="text-lg font-semibold text-foreground">Menu</span>
                <button id="mobile-menu-close" class="p-2 text-foreground hover:bg-accent rounded-md" aria-label="Close mobile menu">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
            <nav class="flex flex-col p-4 space-y-2">
                <a href="/en/" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'home') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Home</a>
                <a href="/en/services.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'services') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Services</a>
                <a href="/en/solutions.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'solutions') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Solutions</a>
                <a href="/en/collaboration.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'collaboration') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Collaboration</a>
                <a href="/en/about.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'about') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">About Us</a>
                <a href="/en/people.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'people') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Our People</a>
                <a href="/en/contact.php" class="px-4 py-3 <?php echo (isset($current_page) && $current_page === 'contact') ? 'bg-orange-100 dark:bg-orange-900/20 text-orange-600 dark:text-orange-500 font-semibold' : 'text-foreground hover:bg-accent'; ?> rounded-md transition-colors no-underline">Contact</a>
            </nav>
        </div>
    </div>

    <!-- Page Content -->
    <main class="min-h-screen">
