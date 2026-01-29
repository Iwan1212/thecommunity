/* ===================================
   THE COMMUNITY - Landing Page Scripts
   =================================== */

document.addEventListener('DOMContentLoaded', function() {

    // ===================================
    // Mobile Navigation Toggle
    // ===================================
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking on a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ===================================
    // Smooth Scroll for Anchor Links
    // ===================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const navHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ===================================
    // Navbar Background on Scroll
    // ===================================
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.08)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    });

    // ===================================
    // Reveal Elements on Scroll
    // ===================================
    const revealElements = document.querySelectorAll(
        '.section-header, .founder-card, .value-card, .business-card, ' +
        '.service-item, .event-card, .blog-card, .faq-item'
    );

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 150;

        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;

            if (elementTop < windowHeight - revealPoint) {
                element.classList.add('visible');
            }
        });
    };

    // Add reveal class to elements
    revealElements.forEach(el => el.classList.add('reveal'));

    // Initial check
    revealOnScroll();

    // Check on scroll
    window.addEventListener('scroll', revealOnScroll);

    // ===================================
    // Form Handling
    // ===================================
    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            // Simple validation
            if (!data.name || !data.email) {
                alert('Proszę wypełnić wszystkie wymagane pola.');
                return;
            }

            // Here you would normally send the data to a server
            // For now, we'll show a success message
            console.log('Form submitted:', data);

            // Show success message
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Wysłano! ✓';
            submitBtn.disabled = true;

            // Reset form
            setTimeout(() => {
                this.reset();
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }, 3000);

            // Optional: Show a modal or notification
            alert('Dziękujemy za wiadomość! Odezwiemy się wkrótce.');
        });
    }

    // ===================================
    // FAQ Accordion Enhancement
    // ===================================
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        item.addEventListener('toggle', function() {
            if (this.open) {
                // Close other open items
                faqItems.forEach(otherItem => {
                    if (otherItem !== this && otherItem.open) {
                        otherItem.open = false;
                    }
                });
            }
        });
    });

    // ===================================
    // Parallax Effect for Hero
    // ===================================
    const hero = document.querySelector('.hero');

    if (hero) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            if (scrolled < window.innerHeight) {
                hero.style.transform = `translateY(${scrolled * 0.3}px)`;
                hero.style.opacity = 1 - (scrolled / window.innerHeight * 0.5);
            }
        });
    }

    // ===================================
    // Intersection Observer for Animations
    // ===================================
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe specific elements
        document.querySelectorAll('.value-card, .result-item, .process-steps li').forEach(el => {
            observer.observe(el);
        });
    }

    // ===================================
    // Staggered Animation for Grid Items
    // ===================================
    const addStaggerDelay = (selector, baseDelay = 100) => {
        document.querySelectorAll(selector).forEach((item, index) => {
            item.style.transitionDelay = `${index * baseDelay}ms`;
        });
    };

    addStaggerDelay('.value-card', 80);
    addStaggerDelay('.service-item', 50);
    addStaggerDelay('.result-item', 100);

    // ===================================
    // Cursor Effect (Optional - disabled by default)
    // ===================================
    /*
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    document.body.appendChild(cursor);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    document.querySelectorAll('a, button').forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
    });
    */

    // ===================================
    // Console Easter Egg
    // ===================================
    console.log('%c✨ THE COMMUNITY ✨', 'font-size: 24px; font-weight: bold; color: #1E3A5F;');
    console.log('%cOffline is the new online', 'font-size: 14px; color: #C4846C; font-style: italic;');
    console.log('%c→ https://instagram.com/the.community.events', 'font-size: 12px; color: #6B6B6B;');

});

// ===================================
// Preloader (Optional)
// ===================================
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});
