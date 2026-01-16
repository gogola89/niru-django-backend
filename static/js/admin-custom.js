// Custom JavaScript for NIRU Admin Interface
// This file can be expanded with custom functionality as needed

document.addEventListener('DOMContentLoaded', function() {
    // Custom admin functionality can be added here
    console.log('NIRU Admin Custom JS loaded');
    
    // Example: Add custom behavior to admin interface
    const adminHeader = document.querySelector('.main-header .navbar-nav .nav-item a');
    if (adminHeader) {
        adminHeader.title = "NIRU Administration Panel";
    }
    
    // Add any additional custom behavior here
});