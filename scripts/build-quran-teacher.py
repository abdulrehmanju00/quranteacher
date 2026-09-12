#!/usr/bin/env python3
"""
Surgical website generator for QuranTeacher.uk
Preserves the exact theme, CSS classes, animations, layout structure, typography, and responsive styles.
Replaces template content with authentic UK-focused Quran teaching content.
"""

import os
import re

COMMON_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="QuranTeacher.uk">
    <link rel="shortcut icon" type="image/png" href="assets/images/favicon.png">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://QuranTeacher.uk{canonical_path}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="https://QuranTeacher.uk{canonical_path}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="QuranTeacher.uk">
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="page-wrapper">
        <!-- start preloader -->
        <div class="preloader">
            <div class="vertical-centered-box">
                <div class="content">
                    <div class="loader-circle"></div>
                    <div class="loader-line-mask">
                        <div class="loader-line"></div>
                    </div>
                    <img src="assets/images/favicon.png" alt="QuranTeacher.uk preloader">
                </div>
            </div>
        </div>
        <!-- end preloader -->
"""

def get_header(active_nav="home", is_home=False):
    header_cls = "wpo-site-header"
    
    def nav_active(page):
        return ' class="active"' if active_nav == page else ''

    return f"""        <!-- Start header -->
        <header id="header" class="{header_cls}">
            <nav class="navigation navbar navbar-expand-lg navbar-light">
                <div class="container">
                    <div class="header-row">
                        <!-- Mobile toggler (mobile/tablet only) -->
                        <div class="mobail-menu d-lg-none">
                            <button type="button" class="navbar-toggler open-btn" aria-label="Toggle navigation">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar first-angle"></span>
                                <span class="icon-bar middle-angle"></span>
                                <span class="icon-bar last-angle"></span>
                            </button>
                        </div>

                        <!-- Brand Logo -->
                        <div class="navbar-header">
                            <a class="navbar-brand" href="index.html">
                                <img src="assets/images/logo.svg" alt="QuranTeacher.uk Logo">
                            </a>
                        </div>

                        <!-- Navigation Menu & Mobile Drawer -->
                        <div id="navbar" class="collapse navbar-collapse navigation-holder">
                            <button class="menu-close d-lg-none" aria-label="Close menu"><i class="ti-close"></i></button>
                            <ul class="nav navbar-nav small-nav">
                                <li><a href="index.html"{nav_active('home')}>Home</a></li>
                                <li><a href="about.html"{nav_active('about')}>About</a></li>
                                <li class="menu-item-has-children">
                                    <a href="service.html"{nav_active('classes')}>Quran Classes <i class="ti-angle-down d-none d-lg-inline-block" style="font-size: 11px; margin-left: 4px;"></i></a>
                                    <ul class="sub-menu">
                                        <li><a href="service.html">All Courses Overview</a></li>
                                        <li><a href="service.html#quran-reading">Quran Reading (Nazra)</a></li>
                                        <li><a href="service.html#noorani-qaida">Noorani Qaida</a></li>
                                        <li><a href="service.html#tajweed">Quran with Tajweed</a></li>
                                        <li><a href="service.html#memorisation">Quran Memorisation (Hifz)</a></li>
                                        <li><a href="service.html#islamic-studies">Islamic Studies</a></li>
                                        <li><a href="service.html#children-adults">Classes for Children &amp; Adults</a></li>
                                    </ul>
                                </li>
                                <li><a href="index.html#how-it-works">How It Works</a></li>
                                <li><a href="index.html#why-us">Why Choose Us</a></li>
                                <li><a href="index.html#faqs">FAQs</a></li>
                                <li><a href="blog.html"{nav_active('resources')}>Resources</a></li>
                                <li><a href="contact.html"{nav_active('contact')}>Contact</a></li>
                            </ul>
                            <!-- Mobile drawer trial button -->
                            <div class="d-lg-none text-center" style="margin-top: 25px; padding: 0 10px;">
                                <a href="register.html" class="theme-btn" style="width: 100%; border-radius: 25px; padding: 12px 20px; display: block;">Book a Free Trial</a>
                            </div>
                        </div>

                        <!-- Header Right CTA button -->
                        <div class="header-right">
                            <a href="register.html" class="theme-btn">Book Free Trial</a>
                        </div>
                    </div>
                </div>
            </nav>
        </header>
        <!-- end of header -->
"""

COMMON_FOOTER = """        <!-- start of footer-section -->
        <footer class="site-footer">
            <div class="upper-footer">
                <div class="container">
                    <div class="row">
                        <div class="col col-lg-4 col-md-6 col-sm-12 col-12">
                            <div class="widget about-widget">
                                <div class="logo widget-title">
                                    <a href="index.html">
                                        <img src="assets/images/logo.svg" alt="QuranTeacher.uk Logo" style="max-height: 48px; width: auto; filter: brightness(0) invert(1);">
                                    </a>
                                </div>
                                <p>QuranTeacher.uk is a dedicated UK-based online Quran teaching academy. We deliver live one-to-one lessons for children and adults across the UK from the comfort and safety of home.</p>
                                <div class="social-widget">
                                    <ul>
                                        <li><a href="contact.html" title="Contact Us"><i class="ti-email"></i></a></li>
                                        <li><a href="register.html" title="Book Free Trial"><i class="ti-calendar"></i></a></li>
                                        <li><a href="about.html" title="About Us"><i class="ti-info-alt"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col col-lg-3 col-md-6 col-sm-12 col-12">
                            <div class="widget link-widget">
                                <div class="widget-title">
                                    <h3>Quran Courses</h3>
                                </div>
                                <ul>
                                    <li><a href="service.html#quran-reading">Quran Reading</a></li>
                                    <li><a href="service.html#noorani-qaida">Noorani Qaida</a></li>
                                    <li><a href="service.html#tajweed">Quran with Tajweed</a></li>
                                    <li><a href="service.html#memorisation">Quran Memorisation (Hifz)</a></li>
                                    <li><a href="service.html#islamic-studies">Islamic Studies</a></li>
                                    <li><a href="service.html#children-adults">Classes for Children &amp; Adults</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col col-lg-2 col-md-6 col-sm-12 col-12">
                            <div class="widget link-widget s2">
                                <div class="widget-title">
                                    <h3>Quick Links</h3>
                                </div>
                                <ul>
                                    <li><a href="index.html">Home</a></li>
                                    <li><a href="about.html">About Us</a></li>
                                    <li><a href="service.html">Quran Classes</a></li>
                                    <li><a href="index.html#how-it-works">How It Works</a></li>
                                    <li><a href="index.html#faqs">FAQs</a></li>
                                    <li><a href="register.html">Book Free Trial</a></li>
                                    <li><a href="contact.html">Contact Us</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col col-lg-3 col-md-6 col-sm-12 col-12">
                            <div class="widget newsletter-widget">
                                <div class="widget-title">
                                    <h3>Start Learning</h3>
                                </div>
                                <p style="color: #c5c5c5; font-size: 14px; margin-bottom: 15px;">Book a free online trial lesson with an experienced Quran teacher.</p>
                                <a href="register.html" class="theme-btn" style="width: 100%; text-align: center; padding: 12px 20px; font-size: 15px; border-radius: 8px;">Book a Free Trial</a>
                                <p style="color: #9e9e9e; font-size: 13px; margin-top: 15px;">Questions? Email <a href="mailto:info@quranteacher.uk" style="color: #DB9E30;">info@quranteacher.uk</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="lower-footer">
                <div class="container">
                    <div class="row g-0 align-items-center">
                        <div class="col col-lg-6 col-12">
                            <p class="copyright"> &copy; 2026 QuranTeacher.uk. All rights reserved.</p>
                        </div>
                        <div class="col col-lg-6 col-12">
                            <ul>
                                <li><a href="privacy.html">Privacy Policy</a></li>
                                <li><a href="terms.html">Terms &amp; Conditions</a></li>
                                <li><a href="contact.html">Contact</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- end of footer-section -->
    </div>
    <!-- end of page-wrapper -->

    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <a href="#" class="back-to-top" style="display: none;" aria-label="Back to top"><i class="ti-arrow-up"></i></a>

    <script>
    (function() {
        // Preloader hide
        var preloader = document.querySelector('.preloader');
        if (preloader) {
            preloader.style.transition = 'opacity 0.4s ease';
            preloader.style.opacity = '0';
            setTimeout(function() { preloader.style.display = 'none'; }, 400);
        }

        // Mobile menu toggle
        var openBtns = document.querySelectorAll('.mobail-menu .navbar-toggler, .open-btn');
        var closeBtns = document.querySelectorAll('.menu-close');
        var navHolders = document.querySelectorAll('.navigation-holder');

        openBtns.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                navHolders.forEach(function(nh) { nh.classList.toggle('slideInn'); });
            });
        });

        closeBtns.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                navHolders.forEach(function(nh) { nh.classList.remove('slideInn'); });
            });
        });

        // Mobile sub-menu toggle
        var menuItems = document.querySelectorAll('.menu-item-has-children > a');
        menuItems.forEach(function(item) {
            item.addEventListener('click', function(e) {
                if (window.innerWidth <= 991) {
                    var sub = item.nextElementSibling;
                    if (sub && sub.classList.contains('sub-menu')) {
                        e.preventDefault();
                        sub.style.display = (sub.style.display === 'block') ? 'none' : 'block';
                    }
                }
            });
        });

        // Close mobile drawer when clicking outside
        document.addEventListener('click', function(e) {
            if (window.innerWidth <= 991) {
                var drawer = document.querySelector('.navigation-holder.slideInn');
                if (drawer && !drawer.contains(e.target) && !e.target.closest('.open-btn') && !e.target.closest('.navbar-toggler')) {
                    drawer.classList.remove('slideInn');
                }
            }
        });

        // Sticky header
        var header = document.querySelector('.wpo-site-header');
        var backToTop = document.querySelector('.back-to-top');

        window.addEventListener('scroll', function() {
            var scrollY = window.pageYOffset || document.documentElement.scrollTop;
            if (header) {
                if (scrollY > 150) {
                    header.classList.add('sticky-on');
                } else {
                    header.classList.remove('sticky-on');
                }
            }
            if (backToTop) {
                backToTop.style.display = (scrollY > 300) ? 'block' : 'none';
            }
        });

        if (backToTop) {
            backToTop.addEventListener('click', function(e) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        // Scroll Reveal Animation Engine (IntersectionObserver)
        var revealElements = document.querySelectorAll('.reveal-on-scroll, .reveal-left, .reveal-right');
        if ('IntersectionObserver' in window) {
            var revealObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        revealObserver.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.08,
                rootMargin: '0px 0px -25px 0px'
            });

            revealElements.forEach(function(el) {
                revealObserver.observe(el);
            });
        } else {
            revealElements.forEach(function(el) {
                el.classList.add('revealed');
            });
        }
    })();
    </script>
</body>
</html>
"""

def breadcrumb(title, trail=[("Home", "index.html")]):
    trail_items = "".join([f'<li><a href="{href}">{name}</a></li>' for name, href in trail])
    return f"""        <!-- start of breadcumb -->
        <div class="wpo-breadcumb-area" style="background: url('assets/images/page-title.jpg') center/cover no-repeat; position: relative;">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <div class="wpo-breadcumb-wrap text-center">
                            <h2>{title}</h2>
                            <ul>
                                {trail_items}
                                <li><span>{title}</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end of breadcumb -->
"""

print("Writing pages...")

# -------------------------------------------------------------
# 1. INDEX.HTML (Homepage)
# -------------------------------------------------------------
index_body = """
        <!-- start of static-hero -->
        <section class="static-hero">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="hero-content">
                            <span class="hero-badge animate-fade-down">
                                <i class="ti-check-box" style="margin-right: 6px;"></i> UK-BASED ONLINE QURAN ACADEMY
                            </span>
                            <h1 class="hero-heading animate-fade-up">Learn the Quran from the comfort of your home</h1>
                            <p class="hero-subtitle animate-fade-up delay-1">Online Quran classes for children and adults across the UK, with qualified teachers and flexible lesson times.</p>
                            
                            <div class="hero-btn-group animate-fade-up delay-2">
                                <a href="register.html" class="hero-primary-btn">
                                    <span>Book a Free Trial</span>
                                    <i class="ti-arrow-right" style="margin-left: 8px;"></i>
                                </a>
                                <a href="service.html" class="hero-secondary-btn">
                                    <span>Explore Classes</span>
                                </a>
                            </div>

                            <div class="hero-trust-badges animate-fade-up delay-3">
                                <div class="trust-item"><i class="ti-star"></i> <span>1-to-1 Live Classes</span></div>
                                <div class="trust-item"><i class="ti-time"></i> <span>UK Flexible Slots</span></div>
                                <div class="trust-item"><i class="ti-shield"></i> <span>DBS-Vetted Tutors</span></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="hero-media-wrapper animate-fade-in delay-2">
                            <div class="hero-img-card">
                                <img src="assets/images/about/hero-right.jpg" alt="Online Quran Teaching for UK Students" class="hero-main-img">
                                <div class="floating-badge badge-top-left animate-float">
                                    <div class="badge-icon"><i class="ti-video-camera"></i></div>
                                    <div class="badge-text">
                                        <strong>Live 1-to-1</strong>
                                        <span>Interactive Video</span>
                                    </div>
                                </div>
                                <div class="floating-badge badge-bottom-right animate-float-delay">
                                    <div class="badge-icon gold-bg"><i class="ti-medall"></i></div>
                                    <div class="badge-text">
                                        <strong>Noorani Qaida &amp; Tajweed</strong>
                                        <span>For Children &amp; Adults</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of static-hero -->

        <!-- start of prayertine (UK Lesson Schedules) -->
        <section class="prayertine-section">
            <div class="container">
                <div class="prayertine-wrap">
                    <div class="row g-0 text-center" id="prayerTimeRow">
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>Weekday Afternoons</h2>
                                <span>4:00 pm – 6:00 pm</span>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>Weekday Evenings</h2>
                                <span>6:00 pm – 9:00 pm</span>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>Saturday Classes</h2>
                                <span>9:00 am – 7:00 pm</span>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>Sunday Classes</h2>
                                <span>9:00 am – 7:00 pm</span>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>Adult Morning Slots</h2>
                                <span>Flexible Schedules</span>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-4 col-sm-6 col-12">
                            <div class="item">
                                <h2>1-on-1 Lessons</h2>
                                <span>Dedicated Tutors</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of prayertine -->

        <!-- start of about -->
        <section class="about-section section-padding" id="about">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-12">
                        <div class="about-img-wrap reveal-on-scroll reveal-left">
                            <div class="image-1">
                                <img src="assets/images/about/about-1.jpg" alt="Online Quran Teaching" style="border-radius: 12px; width: 100%; object-fit: cover;">
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-12">
                        <div class="about-content reveal-on-scroll reveal-right" style="padding-left: 15px;">
                            <div class="section-title">
                                <h2>About QuranTeacher.uk</h2>
                                <h3>Personalised Online Quran Education for UK Families</h3>
                            </div>
                            <p>QuranTeacher.uk provides dedicated, one-to-one online Quran education tailored specifically for learners in the United Kingdom. Whether your child is starting with Noorani Qaida or you are an adult looking to refine your Tajweed and understanding, our lessons are structured around your schedule and learning pace.</p>
                            <p>All classes are conducted live online by qualified and supportive tutors. With interactive screen-sharing, gentle guidance, and flexible morning, evening, and weekend timings, we make authentic Quran learning accessible from the safety and comfort of your home.</p>
                            <div class="about-features" style="margin: 25px 0;">
                                <div class="row">
                                    <div class="col-sm-6 col-12 mb-2">
                                        <div style="display: flex; align-items: center;">
                                            <i class="ti-check" style="color: #DB9E30; font-weight: bold; margin-right: 10px; font-size: 16px;"></i>
                                            <span style="font-weight: 600; color: #232f4b;">1-to-1 Live Online Lessons</span>
                                        </div>
                                    </div>
                                    <div class="col-sm-6 col-12 mb-2">
                                        <div style="display: flex; align-items: center;">
                                            <i class="ti-check" style="color: #DB9E30; font-weight: bold; margin-right: 10px; font-size: 16px;"></i>
                                            <span style="font-weight: 600; color: #232f4b;">UK-Friendly Schedules</span>
                                        </div>
                                    </div>
                                    <div class="col-sm-6 col-12 mb-2">
                                        <div style="display: flex; align-items: center;">
                                            <i class="ti-check" style="color: #DB9E30; font-weight: bold; margin-right: 10px; font-size: 16px;"></i>
                                            <span style="font-weight: 600; color: #232f4b;">Qualified &amp; Supportive Tutors</span>
                                        </div>
                                    </div>
                                    <div class="col-sm-6 col-12 mb-2">
                                        <div style="display: flex; align-items: center;">
                                            <i class="ti-check" style="color: #DB9E30; font-weight: bold; margin-right: 10px; font-size: 16px;"></i>
                                            <span style="font-weight: 600; color: #232f4b;">Regular Student Progress Reports</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="btns" style="margin-top: 25px;">
                                <a href="register.html" class="theme-btn">Book a Free Trial</a>
                                <a href="about.html" class="theme-btn-s2" style="margin-left: 15px;">Learn More</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of about -->

        <!-- start of pillars (Why Choose Us) -->
        <section class="pillars-section section-padding" id="why-us" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-md-9 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Why Choose Us</h2>
                            <h3>Benefits of Learning with QuranTeacher.uk</h3>
                        </div>
                    </div>
                </div>
                <div class="row" style="margin-top: 30px;">
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-home" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Learn From Home</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">Attend live Quran lessons online without the stress of travelling or bad weather. Safe and comfortable learning for children.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-time" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Flexible Lesson Times</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">Choose lesson schedules that fit around UK school, university, work, and family commitments with ease.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-user" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Qualified Teachers</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">Learn with experienced, vetted, and patient Quran tutors trained in Tajweed rules and English communication.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-book" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Personalised Learning</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">1-on-1 lessons adapted to each student's age, baseline ability, and learning speed for optimal retention.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-heart" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Children &amp; Adults</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">Courses tailored for young children (age 4+), teenagers, and adults who wish to start or refresh their Quranic skills.</p>
                        </div>
                    </div>
                    <div class="col-xl-4 col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 35px 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); height: 100%; border-top: 3px solid #DB9E30;">
                            <div style="width: 55px; height: 55px; background: rgba(219, 158, 48, 0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-stats-up" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 12px; color: #232f4b;">Regular Progress</h4>
                            <p style="color: #666; line-height: 1.6; margin-bottom: 0;">Consistent lesson routines, weekly revision, and constructive feedback help learners develop confident habits.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of pillars -->

        <!-- start of service (Quran Courses) -->
        <section class="service-section section-padding" id="courses">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Our Courses</h2>
                            <h3>Online Quran Classes for Every Level</h3>
                        </div>
                    </div>
                </div>
                <div class="service-wrap">
                    <div class="row">
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>01</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-1.svg" alt="Quran Reading">
                                </div>
                                <h2>Quran Reading</h2>
                                <p>Learn to read the Quran correctly from the basics and gradually improve fluency with guided recitation and correct pronunciation.</p>
                                <a href="service.html#quran-reading">Read More...</a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>02</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-2.svg" alt="Noorani Qaida">
                                </div>
                                <h2>Noorani Qaida</h2>
                                <p>A structured foundation for beginners learning Arabic letters, vowel signs (Harakat), joining letters, and Quran reading rules.</p>
                                <a href="service.html#noorani-qaida">Read More...</a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>03</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-3.svg" alt="Quran with Tajweed">
                                </div>
                                <h2>Quran with Tajweed</h2>
                                <p>Master the essential rules of Tajweed (Makharij, Ghunnah, Idgham, Madd) to recite the Quran with beauty and precision.</p>
                                <a href="service.html#tajweed">Read More...</a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>04</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-4.svg" alt="Quran Memorisation">
                                </div>
                                <h2>Quran Memorisation</h2>
                                <p>A structured approach to memorising Surahs or full Hifz with regular teacher assessment, systematic revision, and retention techniques.</p>
                                <a href="service.html#memorisation">Read More...</a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>05</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-5.svg" alt="Islamic Studies">
                                </div>
                                <h2>Islamic Studies</h2>
                                <p>Learn essential Islamic knowledge, daily Duas, Kalimahs, prayer methods (Salah), and Islamic manners in an age-appropriate curriculum.</p>
                                <a href="service.html#islamic-studies">Read More...</a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-6 col-md-6 col-12">
                            <div class="service-card reveal-on-scroll">
                                <div class="top-number">
                                    <span>06</span>
                                </div>
                                <div class="icon">
                                    <img src="assets/images/service/icon-6.svg" alt="Children & Adults">
                                </div>
                                <h2>Children &amp; Adults</h2>
                                <p>Friendly, engaging lessons designed for children, alongside flexible, private evening schedules for busy adult learners.</p>
                                <a href="service.html#children-adults">Read More...</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of service -->

        <!-- start of How It Works -->
        <section class="section-padding" id="how-it-works" style="background: #fbfbfb;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-md-9 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>How It Works</h2>
                            <h3>Start Your Quran Learning in 4 Simple Steps</h3>
                        </div>
                    </div>
                </div>
                <div class="row" style="margin-top: 35px;">
                    <div class="col-lg-3 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 30px 20px; text-align: center; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: relative;">
                            <div style="width: 50px; height: 50px; background: #DB9E30; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; margin: 0 auto 20px auto;">1</div>
                            <h4 style="font-size: 19px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Register</h4>
                            <p style="color: #666; font-size: 14px; line-height: 1.6;">Send your details through our simple registration form or send an online enquiry.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 30px 20px; text-align: center; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: relative;">
                            <div style="width: 50px; height: 50px; background: #DB9E30; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; margin: 0 auto 20px auto;">2</div>
                            <h4 style="font-size: 19px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Choose a Time</h4>
                            <p style="color: #666; font-size: 14px; line-height: 1.6;">Select lesson days and UK time slots that work smoothly with your routine.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 30px 20px; text-align: center; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: relative;">
                            <div style="width: 50px; height: 50px; background: #DB9E30; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; margin: 0 auto 20px auto;">3</div>
                            <h4 style="font-size: 19px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Start Your Trial</h4>
                            <p style="color: #666; font-size: 14px; line-height: 1.6;">Begin your free one-to-one online trial lesson and meet your teacher.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-4">
                        <div style="background: #fff; border-radius: 12px; padding: 30px 20px; text-align: center; height: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: relative;">
                            <div style="width: 50px; height: 50px; background: #DB9E30; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 800; margin: 0 auto 20px auto;">4</div>
                            <h4 style="font-size: 19px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Continue Learning</h4>
                            <p style="color: #666; font-size: 14px; line-height: 1.6;">Build confidence in reading, Tajweed or memorisation with regular lessons.</p>
                        </div>
                    </div>
                </div>
                <div class="text-center" style="margin-top: 25px;">
                    <a href="register.html" class="theme-btn">Book Your Free Trial Lesson</a>
                </div>
            </div>
        </section>
        <!-- end of How It Works -->

        <!-- start of funfact (Free Trial CTA) -->
        <section class="funfact-section section-padding" id="trial">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-11 col-12">
                        <div class="funfact-content reveal-on-scroll">
                            <div class="top-content">
                                <h2 class="title">Start Your Quran Learning Journey</h2>
                                <h3 class="sudtitle" style="font-size: 28px; font-weight: 700; color: #232f4b; margin: 10px 0 15px 0;">Book a Free Online Trial Lesson</h3>
                                <p class="text">Take your first step with an online Quran lesson designed around your learning needs. Experience our supportive one-to-one teaching with no commitment required.</p>
                            </div>
                            <div class="funfact" style="display: flex; flex-wrap: wrap; margin: 25px 0 35px 0;">
                                <div class="item" style="margin-right: 35px; margin-bottom: 20px;">
                                    <h2 style="font-size: 38px; color: #DB9E30; font-weight: 800;">100%</h2>
                                    <h4 style="font-size: 15px; color: #232f4b;">Online Lessons</h4>
                                </div>
                                <div class="item" style="margin-right: 35px; margin-bottom: 20px;">
                                    <h2 style="font-size: 38px; color: #DB9E30; font-weight: 800;">1-on-1</h2>
                                    <h4 style="font-size: 15px; color: #232f4b;">Personal Attention</h4>
                                </div>
                                <div class="item" style="margin-right: 35px; margin-bottom: 20px;">
                                    <h2 style="font-size: 38px; color: #DB9E30; font-weight: 800;">UK</h2>
                                    <h4 style="font-size: 15px; color: #232f4b;">Flexible Timings</h4>
                                </div>
                                <div class="item" style="margin-bottom: 20px;">
                                    <h2 style="font-size: 38px; color: #DB9E30; font-weight: 800;">All Ages</h2>
                                    <h4 style="font-size: 15px; color: #232f4b;">Children &amp; Adults</h4>
                                </div>
                            </div>
                            <a href="register.html" class="theme-btn">Book a Free Trial</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of funfact -->

        <!-- start of FAQs Section -->
        <section class="section-padding pf-terms-section" id="faqs" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8 col-md-10 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Frequently Asked Questions</h2>
                            <h3>Common Questions About Our Online Quran Classes</h3>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center" style="margin-top: 30px;">
                    <div class="col-lg-9 col-12">
                        <div class="accordion" id="quranFaqAccordion">
                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead1">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse1" aria-expanded="true" aria-controls="faqCollapse1" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Are Quran classes available for children?
                                    </button>
                                </h2>
                                <div id="faqCollapse1" class="accordion-collapse collapse show" aria-labelledby="faqHead1" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. QuranTeacher.uk offers online Quran learning for children with lessons designed around their age and level. Our tutors are patient, encouraging, and experienced with young learners.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead2">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse2" aria-expanded="false" aria-controls="faqCollapse2" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Are classes available for adults?
                                    </button>
                                </h2>
                                <div id="faqCollapse2" class="accordion-collapse collapse" aria-labelledby="faqHead2" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. Adults can learn Quran online from beginner level onwards. We offer flexible scheduling in the mornings and evenings to fit comfortably around work and family commitments.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead3">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse3" aria-expanded="false" aria-controls="faqCollapse3" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Do I need to travel to attend classes?
                                    </button>
                                </h2>
                                <div id="faqCollapse3" class="accordion-collapse collapse" aria-labelledby="faqHead3" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        No. Classes are conducted online via live interactive video and digital screen-sharing, allowing students to learn from home anywhere across the United Kingdom.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead4">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse4" aria-expanded="false" aria-controls="faqCollapse4" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Can I choose my lesson time?
                                    </button>
                                </h2>
                                <div id="faqCollapse4" class="accordion-collapse collapse" aria-labelledby="faqHead4" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. Lesson schedules can be arranged around the student's availability, including weekday afternoons, evenings, and weekend slots.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead5">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse5" aria-expanded="false" aria-controls="faqCollapse5" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Can beginners join?
                                    </button>
                                </h2>
                                <div id="faqCollapse5" class="accordion-collapse collapse" aria-labelledby="faqHead5" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. Beginners can start from the absolute basics, including Noorani Qaida to master Arabic alphabet pronunciation before progressing to words and Quranic sentences.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead6">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse6" aria-expanded="false" aria-controls="faqCollapse6" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Do you teach Tajweed?
                                    </button>
                                </h2>
                                <div id="faqCollapse6" class="accordion-collapse collapse" aria-labelledby="faqHead6" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. Tajweed lessons help students improve pronunciation and Quran recitation according to established rules of articulation and rhythm.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item mb-3 reveal-on-scroll" style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; background: #fff;">
                                <h2 class="accordion-header" id="faqHead7">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faqCollapse7" aria-expanded="false" aria-controls="faqCollapse7" style="font-weight: 700; color: #232f4b; font-size: 17px; padding: 18px 22px;">
                                        Can I book a trial lesson?
                                    </button>
                                </h2>
                                <div id="faqCollapse7" class="accordion-collapse collapse" aria-labelledby="faqHead7" data-bs-parent="#quranFaqAccordion">
                                    <div class="accordion-body" style="padding: 15px 22px; color: #555; line-height: 1.7; border-top: 1px solid #f1f5f9;">
                                        Yes. Use the registration/contact process on the website to enquire about starting a free trial lesson with no commitment required.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of FAQs -->

        <!-- start of blog (Resources & Guides) -->
        <section class="blog-section section-padding" id="resources">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Quran Learning Resources</h2>
                            <h3>Guides &amp; Advice for Students and Parents</h3>
                        </div>
                    </div>
                </div>
                <div class="blog-wrap">
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="blog-card reveal-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.06); background: #fff; height: 100%;">
                                <div class="image">
                                    <img src="assets/images/blog/1.jpg" alt="How to Start Learning Quran Online" style="width: 100%; height: 220px; object-fit: cover;">
                                </div>
                                <div class="content" style="padding: 25px;">
                                    <span style="font-size: 13px; color: #DB9E30; font-weight: 700; text-transform: uppercase;">Getting Started</span>
                                    <h2 style="font-size: 20px; font-weight: 700; margin: 10px 0 15px 0;"><a href="blog-single.html" style="color: #232f4b;">How to Start Learning Quran Online from Home</a></h2>
                                    <p style="color: #666; font-size: 14px; line-height: 1.6;">A practical step-by-step guide for parents and adult beginners starting their online Quran education journey.</p>
                                    <a href="blog-single.html" class="theme-btn-s2" style="font-size: 13px; padding: 8px 18px; margin-top: 10px;">Read More</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="blog-card reveal-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.06); background: #fff; height: 100%;">
                                <div class="image">
                                    <img src="assets/images/blog/2.jpg" alt="Benefits of Learning Quran with Tajweed" style="width: 100%; height: 220px; object-fit: cover;">
                                </div>
                                <div class="content" style="padding: 25px;">
                                    <span style="font-size: 13px; color: #DB9E30; font-weight: 700; text-transform: uppercase;">Tajweed Rules</span>
                                    <h2 style="font-size: 20px; font-weight: 700; margin: 10px 0 15px 0;"><a href="blog-single.html" style="color: #232f4b;">Benefits of Learning Quran with Tajweed</a></h2>
                                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Discover why proper pronunciation, articulation points (Makharij), and Tajweed rules are vital for recitation.</p>
                                    <a href="blog-single.html" class="theme-btn-s2" style="font-size: 13px; padding: 8px 18px; margin-top: 10px;">Read More</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-12">
                            <div class="blog-card reveal-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.06); background: #fff; height: 100%;">
                                <div class="image">
                                    <img src="assets/images/blog/3.jpg" alt="Parent Support for Quran Learning" style="width: 100%; height: 220px; object-fit: cover;">
                                </div>
                                <div class="content" style="padding: 25px;">
                                    <span style="font-size: 13px; color: #DB9E30; font-weight: 700; text-transform: uppercase;">Parent Guide</span>
                                    <h2 style="font-size: 20px; font-weight: 700; margin: 10px 0 15px 0;"><a href="blog-single.html" style="color: #232f4b;">How Parents Can Support Children's Quran Learning</a></h2>
                                    <p style="color: #666; font-size: 14px; line-height: 1.6;">Simple daily habits and positive encouragement techniques to help children retain Surahs and remain motivated.</p>
                                    <a href="blog-single.html" class="theme-btn-s2" style="font-size: 13px; padding: 8px 18px; margin-top: 10px;">Read More</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- end of blog -->
"""

index_full = COMMON_HEAD.format(
    title="QuranTeacher.uk | Online Quran Classes in the UK",
    description="QuranTeacher.uk provides online Quran classes for children and adults across the UK, including Quran reading, Noorani Qaida, Tajweed, memorisation and Islamic Studies.",
    canonical_path=""
) + get_header('home', is_home=True) + index_body + COMMON_FOOTER

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(index_full)
with open("public/index-2.html", "w", encoding="utf-8") as f:
    f.write(index_full)
with open("public/index-3.html", "w", encoding="utf-8") as f:
    f.write(index_full)
print("  - index.html, index-2.html, index-3.html written")

# -------------------------------------------------------------
# 2. ABOUT.HTML
# -------------------------------------------------------------
about_body = breadcrumb("About QuranTeacher.uk") + """
        <!-- start of wpo-about-section -->
        <section class="wpo-about-section section-padding">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="wpo-about-wrap">
                            <div class="wpo-about-img">
                                <img src="assets/images/about/about-1.jpg" alt="About QuranTeacher.uk" style="border-radius: 12px; width: 100%; object-fit: cover; max-height: 480px; box-shadow: 0 8px 25px rgba(0,0,0,0.08);">
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-12">
                        <div class="wpo-about-text" style="padding-left: 15px;">
                            <div class="wpo-section-title">
                                <span style="color: #DB9E30; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">UK Online Quran Academy</span>
                                <h2 style="font-size: 34px; font-weight: 800; color: #232f4b; margin: 10px 0 20px 0;">Accessible Quran Education from the Comfort of Home</h2>
                            </div>
                            <p style="line-height: 1.7; color: #555; margin-bottom: 15px;">QuranTeacher.uk was established to provide families across the United Kingdom with structured, reliable, and accessible Quranic education. We connect students directly with qualified teachers through one-to-one live online sessions.</p>
                            <p style="line-height: 1.7; color: #555; margin-bottom: 20px;">We understand that busy UK family schedules, school timings, and weather can make commuting to an evening class difficult. With QuranTeacher.uk, your child or you can learn directly from your living room or study on your computer or tablet, with personalised attention from an experienced tutor.</p>
                            
                            <div class="btns" style="margin-top: 30px;">
                                <a href="register.html" class="theme-btn">Book a Free Trial</a>
                                <a href="service.html" class="theme-btn-s2" style="margin-left: 15px;">Explore Courses</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- start of Mission & Values -->
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-md-9 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Our Principles</h2>
                            <h3>What Guides Our Teaching</h3>
                        </div>
                    </div>
                </div>
                <div class="row" style="margin-top: 30px;">
                    <div class="col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; padding: 35px 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 100%;">
                            <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-check-box" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Correct Tajweed &amp; Pronunciation</h4>
                            <p style="color: #666; line-height: 1.6;">We emphasise correct articulation of Arabic letters from day one, ensuring students build good recitation habits that last a lifetime.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; padding: 35px 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 100%;">
                            <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-face-smile" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">Patience &amp; Positive Encouragement</h4>
                            <p style="color: #666; line-height: 1.6;">Our teachers create a supportive, pressure-free atmosphere so that children look forward to their lessons and build real self-confidence.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12 mb-4">
                        <div style="background: #fff; padding: 35px 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 100%;">
                            <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                                <i class="ti-calendar" style="font-size: 24px; color: #DB9E30;"></i>
                            </div>
                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin-bottom: 12px;">UK-Tailored Flexibility</h4>
                            <p style="color: #666; line-height: 1.6;">We coordinate classes around UK school terms, daylight saving changes, and family holidays to maintain consistent progress without burnout.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- start of CTA -->
        <section class="section-padding text-center" style="background: #232f4b; color: #fff;">
            <div class="container">
                <h2 style="font-size: 32px; font-weight: 800; color: #fff; margin-bottom: 15px;">Experience an Online Lesson First Hand</h2>
                <p style="font-size: 17px; color: #cbd5e1; max-width: 650px; margin: 0 auto 30px auto;">Book a free, no-obligation trial lesson and see how our one-to-one teaching can support your Quran learning journey.</p>
                <a href="register.html" class="theme-btn" style="padding: 14px 40px; font-size: 16px;">Book a Free Trial</a>
            </div>
        </section>
"""

about_full = COMMON_HEAD.format(
    title="About Us | QuranTeacher.uk - Online Quran Classes in the UK",
    description="Learn about QuranTeacher.uk, our qualified tutors, and our mission to provide accessible online Quran education for students across the UK.",
    canonical_path="/about"
) + get_header('about') + about_body + COMMON_FOOTER

with open("public/about.html", "w", encoding="utf-8") as f:
    f.write(about_full)
print("  - about.html written")

# -------------------------------------------------------------
# 3. SERVICE.HTML (Quran Classes)
# -------------------------------------------------------------
service_body = breadcrumb("Our Quran Classes") + """
        <!-- start of service section -->
        <section class="service-section section-padding">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Structured Courses</h2>
                            <h3>Online Quran Classes Tailored for Every Learner</h3>
                            <p style="color: #666; font-size: 16px; max-width: 680px; margin: 15px auto 0 auto;">Choose a learning plan that fits your current level and goals. All courses are delivered live online with one-to-one tutor attention.</p>
                        </div>
                    </div>
                </div>

                <div class="service-wrap" style="margin-top: 30px;">
                    <div class="row">
                        <!-- Course 1 -->
                        <div class="col-lg-6 col-12 mb-4" id="quran-reading">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-1.svg" alt="Quran Reading Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Foundation &amp; Fluency</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Quran Reading (Nazra)</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">Designed for learners who want to read the Holy Quran correctly from the basics and gradually improve their fluency and confidence. The tutor listens carefully, corrects errors in real time, and helps the student build a natural rhythm.</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>Reading directly from the Mushaf (Uthmani or Indo-Pak script)</li>
                                    <li>Guidance on stopping rules (Waqf) and verse endings</li>
                                    <li>Gradual improvement of reading speed without losing pronunciation</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>

                        <!-- Course 2 -->
                        <div class="col-lg-6 col-12 mb-4" id="noorani-qaida">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-2.svg" alt="Noorani Qaida Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Beginner Foundation</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Noorani Qaida</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">A structured foundation for beginners of all ages learning Arabic letters, pronunciation, and Quran reading fundamentals. Students learn letter shapes, vowel marks (Fatha, Kasra, Dammah), Sukoon, and rules for joining letters.</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>Individual letter recognition and correct phonetics</li>
                                    <li>Compound letters (Murakkabat) and short/long vowels</li>
                                    <li>Smooth transition from Qaida to reading simple Quranic verses</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>

                        <!-- Course 3 -->
                        <div class="col-lg-6 col-12 mb-4" id="tajweed">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-3.svg" alt="Quran with Tajweed Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Correct Pronunciation</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Quran with Tajweed</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">Learn the rules of Tajweed and improve Quran pronunciation and recitation. Ideal for students who can already read but wish to master correct articulation points (Makharij) and recitation rules.</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>Rules of Noon Sakinah, Tanween, and Meem Sakinah</li>
                                    <li>Makharij (throat, tongue, lips articulation points)</li>
                                    <li>Rules of Madd (prolongation), Ghunnah, Qalqalah, and Ikhfa</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>

                        <!-- Course 4 -->
                        <div class="col-lg-6 col-12 mb-4" id="memorisation">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-4.svg" alt="Quran Memorisation Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Hifz Program</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Quran Memorisation</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">A structured approach to memorising Surahs or embarking on full Hifz. We emphasise daily memorisation (Sabaq), recent revision (Sabqi), and cumulative revision (Manzil) to ensure retention.</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>Daily target setting adapted to the student's capacity</li>
                                    <li>Systematic revision schedule to prevent forgetting</li>
                                    <li>Tajweed compliance during memorisation</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>

                        <!-- Course 5 -->
                        <div class="col-lg-6 col-12 mb-4" id="islamic-studies">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-5.svg" alt="Islamic Studies Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Faith &amp; Practice</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Islamic Studies</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">Learn essential Islamic knowledge in an age-appropriate, easy-to-understand way. Covers fundamental beliefs, five pillars, stories of the Prophets, daily Sunnah Duas, and moral character (Akhlaq).</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>How to perform Wudu and complete Salah (Prayer)</li>
                                    <li>Six Kalimahs and daily supplications (Duas)</li>
                                    <li>Moral manners and Islamic values for growing up in the UK</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>

                        <!-- Course 6 -->
                        <div class="col-lg-6 col-12 mb-4" id="children-adults">
                            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 35px 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); height: 100%;">
                                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                                    <div style="width: 55px; height: 55px; background: rgba(219,158,48,0.12); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 20px;">
                                        <img src="assets/images/service/icon-6.svg" alt="Children and Adults Icon" style="width: 30px; height: 30px;">
                                    </div>
                                    <div>
                                        <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">All Ages</span>
                                        <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 3px 0 0 0;">Classes for Children &amp; Adults</h3>
                                    </div>
                                </div>
                                <p style="color: #555; line-height: 1.7; margin-bottom: 15px;">Friendly online lessons designed to help children learn consistently and confidently, alongside private, flexible sessions for adult learners looking to begin or resume their Quranic studies.</p>
                                <ul style="color: #666; font-size: 14px; margin-bottom: 20px; list-style: disc; padding-left: 20px; line-height: 1.8;">
                                    <li>Children: Engaging 30-minute sessions suited to attention spans</li>
                                    <li>Adults: Discreet, 1-on-1 private classes at flexible evening hours</li>
                                    <li>Qualified male and female teachers available upon request</li>
                                </ul>
                                <a href="register.html" class="theme-btn" style="padding: 9px 24px; font-size: 14px;">Enrol for Free Trial</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Learning Plans / Contact CTA without fake prices -->
                <div style="background: #fbfbfb; border: 2px dashed #DB9E30; border-radius: 16px; padding: 40px; margin-top: 40px; text-align: center;">
                    <h3 style="font-size: 26px; font-weight: 800; color: #232f4b; margin-bottom: 10px;">Choose Your Learning Schedule</h3>
                    <p style="color: #555; font-size: 16px; max-width: 600px; margin: 0 auto 25px auto;">We offer 2, 3, 4, or 5 days per week options, with 30-minute or 45-minute lesson durations. Contact us for personalised schedule details and family discounts.</p>
                    <a href="register.html" class="theme-btn" style="padding: 12px 35px;">Book a Free Trial Lesson</a>
                    <a href="contact.html" class="theme-btn-s2" style="margin-left: 15px; padding: 12px 30px;">Ask a Question</a>
                </div>
            </div>
        </section>
"""

service_full = COMMON_HEAD.format(
    title="Online Quran Classes | QuranTeacher.uk - Courses & Syllabi",
    description="Explore our online Quran courses across the UK: Quran reading, Noorani Qaida, Tajweed rules, Quran memorisation, and Islamic studies.",
    canonical_path="/service"
) + get_header('classes') + service_body + COMMON_FOOTER

with open("public/service.html", "w", encoding="utf-8") as f:
    f.write(service_full)
with open("public/service-s2.html", "w", encoding="utf-8") as f:
    f.write(service_full)
with open("public/service-single.html", "w", encoding="utf-8") as f:
    f.write(service_full)
print("  - service.html, service-s2.html, service-single.html written")

# -------------------------------------------------------------
# 4. CONTACT.HTML
# -------------------------------------------------------------
contact_body = breadcrumb("Contact QuranTeacher.uk") + """
        <!-- start of contact-pg-section -->
        <section class="wpo-contact-pg-section section-padding">
            <div class="container">
                <div class="row">
                    <div class="col-lg-10 offset-lg-1">
                        <div class="row">
                            <div class="col-lg-4 col-md-6 col-12 mb-4">
                                <div style="background: #fff; padding: 30px 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; height: 100%;">
                                    <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto;">
                                        <i class="ti-email" style="font-size: 22px; color: #DB9E30;"></i>
                                    </div>
                                    <h4 style="font-size: 18px; font-weight: 700; color: #232f4b; margin-bottom: 8px;">Email Enquiries</h4>
                                    <p style="color: #666; font-size: 15px; margin: 0;"><a href="mailto:info@quranteacher.uk" style="color: #DB9E30;">info@quranteacher.uk</a></p>
                                    <span style="font-size: 13px; color: #888;">We respond within 24 hours</span>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 col-12 mb-4">
                                <div style="background: #fff; padding: 30px 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; height: 100%;">
                                    <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto;">
                                        <i class="ti-location-pin" style="font-size: 22px; color: #DB9E30;"></i>
                                    </div>
                                    <h4 style="font-size: 18px; font-weight: 700; color: #232f4b; margin-bottom: 8px;">UK Coverage</h4>
                                    <p style="color: #666; font-size: 15px; margin: 0;">Online Across the UK</p>
                                    <span style="font-size: 13px; color: #888;">London, Midlands, North, Scotland, Wales</span>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-12 col-12 mb-4">
                                <div style="background: #fff; padding: 30px 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; height: 100%;">
                                    <div style="width: 50px; height: 50px; background: rgba(219,158,48,0.12); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto;">
                                        <i class="ti-time" style="font-size: 22px; color: #DB9E30;"></i>
                                    </div>
                                    <h4 style="font-size: 18px; font-weight: 700; color: #232f4b; margin-bottom: 8px;">Class Timings</h4>
                                    <p style="color: #666; font-size: 15px; margin: 0;">Mon &ndash; Sun: 8:00 am &ndash; 9:00 pm</p>
                                    <span style="font-size: 13px; color: #888;">UK Time (GMT / BST)</span>
                                </div>
                            </div>
                        </div>

                        <div class="wpo-contact-form" style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); margin-top: 20px;">
                            <div class="section-title">
                                <h2>Send an Enquiry</h2>
                                <h3>Have a Question About Online Quran Classes?</h3>
                            </div>
                            <form id="contactForm" onsubmit="event.preventDefault(); document.getElementById('contactMsgSuccess').style.display='block';">
                                <div class="row">
                                    <div class="col-lg-6 col-12 mb-3">
                                        <label for="cName" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Your Name *</label>
                                        <input type="text" class="form-control" id="cName" name="name" placeholder="Full name" required style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-lg-6 col-12 mb-3">
                                        <label for="cEmail" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Email Address *</label>
                                        <input type="email" class="form-control" id="cEmail" name="email" placeholder="example@domain.co.uk" required style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-lg-6 col-12 mb-3">
                                        <label for="cPhone" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Contact Phone Number</label>
                                        <input type="tel" class="form-control" id="cPhone" name="phone" placeholder="Phone or WhatsApp number" style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-lg-6 col-12 mb-3">
                                        <label for="cCourse" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Course of Interest</label>
                                        <select class="form-control" id="cCourse" name="course" style="padding: 12px 15px; border-radius: 6px;">
                                            <option value="quran-reading">Quran Reading</option>
                                            <option value="noorani-qaida">Noorani Qaida for Beginners</option>
                                            <option value="tajweed">Quran with Tajweed</option>
                                            <option value="memorisation">Quran Memorisation (Hifz)</option>
                                            <option value="islamic-studies">Islamic Studies</option>
                                            <option value="children">Classes for Children</option>
                                            <option value="adults">Classes for Adults</option>
                                        </select>
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="cMessage" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Your Message / Student Age &amp; Preferred Time *</label>
                                        <textarea class="form-control" id="cMessage" name="message" rows="5" placeholder="Tell us about the student's age, previous experience, and preferred lesson days/times..." required style="padding: 12px 15px; border-radius: 6px;"></textarea>
                                    </div>
                                    <div class="col-12">
                                        <button type="submit" class="theme-btn" style="padding: 14px 40px; font-size: 16px;">Send Enquiry</button>
                                        <div id="contactMsgSuccess" style="display: none; margin-top: 20px; padding: 15px; background: #e6fffa; border: 1px solid #38b2ac; border-radius: 6px; color: #234e52; font-weight: 600;">
                                            Thank you for your enquiry. We will get in touch with you shortly to assist with your lesson arrangements.
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

contact_full = COMMON_HEAD.format(
    title="Contact Us | QuranTeacher.uk - Enquire About Online Classes",
    description="Get in touch with QuranTeacher.uk to arrange online Quran lessons for children and adults across the UK.",
    canonical_path="/contact"
) + get_header('contact') + contact_body + COMMON_FOOTER

with open("public/contact.html", "w", encoding="utf-8") as f:
    f.write(contact_full)
print("  - contact.html written")

# -------------------------------------------------------------
# 5. REGISTER.HTML (Book a Free Trial)
# -------------------------------------------------------------
register_body = breadcrumb("Book a Free Trial Lesson") + """
        <!-- start of register section -->
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8 col-md-10 col-12">
                        <div style="background: #fff; padding: 45px 35px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
                            <div class="section-title text-center" style="margin-bottom: 30px;">
                                <span style="color: #DB9E30; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">No Payment Required</span>
                                <h2 style="font-size: 32px; font-weight: 800; color: #232f4b; margin-top: 8px;">Book Your Free Online Trial Lesson</h2>
                                <p style="color: #666; font-size: 15px; margin-top: 10px;">Experience our live 1-on-1 Quran teaching with an experienced teacher. Fill out the short form below to choose your preferred schedule.</p>
                            </div>

                            <form id="trialForm" onsubmit="event.preventDefault(); document.getElementById('trialSuccess').style.display='block';">
                                <div class="row">
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tParentName" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Parent / Student Full Name *</label>
                                        <input type="text" class="form-control" id="tParentName" name="parent_name" placeholder="Full name" required style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tEmail" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Email Address *</label>
                                        <input type="email" class="form-control" id="tEmail" name="email" placeholder="example@email.com" required style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tPhone" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Phone / WhatsApp Number *</label>
                                        <input type="tel" class="form-control" id="tPhone" name="phone" placeholder="UK phone or WhatsApp" required style="padding: 12px 15px; border-radius: 6px;">
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tStudentAge" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Student Age *</label>
                                        <select class="form-control" id="tStudentAge" name="student_age" required style="padding: 12px 15px; border-radius: 6px;">
                                            <option value="">Select age group...</option>
                                            <option value="4-7">Child (4 &ndash; 7 years)</option>
                                            <option value="8-12">Child (8 &ndash; 12 years)</option>
                                            <option value="13-17">Teenager (13 &ndash; 17 years)</option>
                                            <option value="adult">Adult (18+ years)</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tCourse" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Desired Course *</label>
                                        <select class="form-control" id="tCourse" name="course" required style="padding: 12px 15px; border-radius: 6px;">
                                            <option value="noorani-qaida">Noorani Qaida (Beginners)</option>
                                            <option value="quran-reading">Quran Reading</option>
                                            <option value="tajweed">Quran with Tajweed</option>
                                            <option value="hifz">Quran Memorisation (Hifz)</option>
                                            <option value="islamic-studies">Islamic Studies</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 col-12 mb-3">
                                        <label for="tTime" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Preferred Lesson Timing *</label>
                                        <select class="form-control" id="tTime" name="preferred_time" required style="padding: 12px 15px; border-radius: 6px;">
                                            <option value="weekday-afternoon">Weekday Afternoons (4pm &ndash; 6pm UK)</option>
                                            <option value="weekday-evening">Weekday Evenings (6pm &ndash; 9pm UK)</option>
                                            <option value="weekend-morning">Weekend Mornings (9am &ndash; 1pm UK)</option>
                                            <option value="weekend-afternoon">Weekend Afternoons (1pm &ndash; 7pm UK)</option>
                                            <option value="adult-morning">Morning Slot (Adults)</option>
                                        </select>
                                    </div>
                                    <div class="col-12 mb-3">
                                        <label for="tNotes" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Additional Notes / Current Reading Level (Optional)</label>
                                        <textarea class="form-control" id="tNotes" name="notes" rows="3" placeholder="Tell us if the student has studied Arabic letters before, or any specific requirements..." style="padding: 12px 15px; border-radius: 6px;"></textarea>
                                    </div>
                                    <div class="col-12 text-center" style="margin-top: 15px;">
                                        <button type="submit" class="theme-btn" style="padding: 14px 45px; font-size: 16px;">Request Free Trial Lesson</button>
                                        <div id="trialSuccess" style="display: none; margin-top: 25px; padding: 18px; background: #e6fffa; border: 1px solid #38b2ac; border-radius: 8px; color: #234e52; font-weight: 600;">
                                            Thank you for booking a trial lesson! We will review your preferred timing and email you the trial schedule and meeting link.
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

register_full = COMMON_HEAD.format(
    title="Book a Free Trial | QuranTeacher.uk - Online Quran Classes",
    description="Register for a free one-to-one online Quran trial lesson with QuranTeacher.uk. Available for children and adults across the UK.",
    canonical_path="/register"
) + get_header('register') + register_body + COMMON_FOOTER

with open("public/register.html", "w", encoding="utf-8") as f:
    f.write(register_full)
print("  - register.html written")

# -------------------------------------------------------------
# 6. LOGIN.HTML & FORGOT.HTML (Student Portal)
# -------------------------------------------------------------
login_body = breadcrumb("Student Portal Login") + """
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-6 col-md-8 col-12">
                        <div style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
                            <div class="section-title text-center" style="margin-bottom: 25px;">
                                <h2 style="font-size: 28px; font-weight: 800; color: #232f4b;">Student Portal</h2>
                                <p style="color: #666; font-size: 14px; margin-top: 5px;">Sign in to view your class schedule and progress reports.</p>
                            </div>
                            <form onsubmit="event.preventDefault(); document.getElementById('loginNotice').style.display='block';">
                                <div class="mb-3">
                                    <label for="lEmail" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Student / Parent Email</label>
                                    <input type="email" class="form-control" id="lEmail" required placeholder="Enter your registered email" style="padding: 12px 15px; border-radius: 6px;">
                                </div>
                                <div class="mb-3">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                                        <label for="lPass" style="font-weight: 600; color: #232f4b; margin-bottom: 0;">Password</label>
                                        <a href="forgot.html" style="font-size: 13px; color: #DB9E30;">Forgot password?</a>
                                    </div>
                                    <input type="password" class="form-control" id="lPass" required placeholder="Enter your password" style="padding: 12px 15px; border-radius: 6px;">
                                </div>
                                <button type="submit" class="theme-btn" style="width: 100%; padding: 12px; margin-top: 10px;">Sign In</button>
                                <div id="loginNotice" style="display: none; margin-top: 15px; padding: 12px; background: #fefcbf; border: 1px solid #ecc94b; border-radius: 6px; color: #744210; font-size: 14px;">
                                    Student portal credentials are provided upon regular enrolment. If you are a new student, please <a href="register.html" style="color: #744210; font-weight: bold; text-decoration: underline;">book a trial</a> first.
                                </div>
                            </form>
                            <p style="text-align: center; margin-top: 25px; color: #666; font-size: 14px;">New to QuranTeacher.uk? <a href="register.html" style="color: #DB9E30; font-weight: 700;">Book a Free Trial</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

login_full = COMMON_HEAD.format(
    title="Student Portal Sign In | QuranTeacher.uk",
    description="Sign in to your QuranTeacher.uk student portal to view your upcoming lessons, schedules, and teacher notes.",
    canonical_path="/login"
) + get_header('login') + login_body + COMMON_FOOTER

with open("public/login.html", "w", encoding="utf-8") as f:
    f.write(login_full)

forgot_body = breadcrumb("Reset Password") + """
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-6 col-md-8 col-12">
                        <div style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
                            <div class="section-title text-center" style="margin-bottom: 25px;">
                                <h2 style="font-size: 28px; font-weight: 800; color: #232f4b;">Reset Password</h2>
                                <p style="color: #666; font-size: 14px; margin-top: 5px;">Enter your registered email and we'll send you recovery instructions.</p>
                            </div>
                            <form onsubmit="event.preventDefault(); document.getElementById('forgotSuccess').style.display='block';">
                                <div class="mb-3">
                                    <label for="fEmail" style="font-weight: 600; color: #232f4b; margin-bottom: 5px;">Registered Email</label>
                                    <input type="email" class="form-control" id="fEmail" required placeholder="Enter your registered email" style="padding: 12px 15px; border-radius: 6px;">
                                </div>
                                <button type="submit" class="theme-btn" style="width: 100%; padding: 12px; margin-top: 10px;">Send Reset Link</button>
                                <div id="forgotSuccess" style="display: none; margin-top: 15px; padding: 12px; background: #e6fffa; border: 1px solid #38b2ac; border-radius: 6px; color: #234e52; font-size: 14px;">
                                    If an account matches this email, password reset instructions have been sent.
                                </div>
                            </form>
                            <p style="text-align: center; margin-top: 25px; color: #666; font-size: 14px;"><a href="login.html" style="color: #DB9E30; font-weight: 700;">Back to Sign In</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

forgot_full = COMMON_HEAD.format(
    title="Reset Password | QuranTeacher.uk",
    description="Reset your password for the QuranTeacher.uk student portal.",
    canonical_path="/forgot"
) + get_header('login') + forgot_body + COMMON_FOOTER

with open("public/forgot.html", "w", encoding="utf-8") as f:
    f.write(forgot_full)
print("  - login.html, forgot.html written")

# -------------------------------------------------------------
# 7. BLOG.HTML & BLOG-SINGLE.HTML (Resources & Guides)
# -------------------------------------------------------------
blog_articles = [
    {
        "title": "How to Start Learning Quran Online from Home",
        "category": "Getting Started",
        "img": "assets/images/blog/1.jpg",
        "excerpt": "A practical guide for parents and adult beginners in the UK starting their online Quran education journey, from setting up a quiet study area to establishing consistent learning habits."
    },
    {
        "title": "Benefits of Learning Quran with Tajweed",
        "category": "Tajweed Rules",
        "img": "assets/images/blog/2.jpg",
        "excerpt": "Discover why correct articulation points (Makharij) and Tajweed rules are essential for accurate, beautiful recitation and how beginner students can master them step by step."
    },
    {
        "title": "How Parents Can Support Their Children's Quran Learning",
        "category": "Parent Advice",
        "img": "assets/images/blog/3.jpg",
        "excerpt": "Practical daily routines and positive reinforcement strategies that help UK children retain Surahs, practise comfortably, and stay engaged with their Quran teacher."
    },
    {
        "title": "Noorani Qaida for Beginners: What to Expect",
        "category": "Curriculum",
        "img": "assets/images/blog/1.jpg",
        "excerpt": "A comprehensive walkthrough of the Noorani Qaida syllabus, explaining why it remains the most trusted starting point for learning Arabic phonetics and Quranic reading."
    },
    {
        "title": "Building a Consistent Quran Learning Routine in the UK",
        "category": "Student Habits",
        "img": "assets/images/blog/2.jpg",
        "excerpt": "How to balance school homework, extracurricular activities, and Quran classes without burnout using short, consistent 30-minute one-to-one sessions."
    }
]

blog_cards_html = ""
for item in blog_articles:
    blog_cards_html += f"""
                    <div class="col-lg-4 col-md-6 col-12 mb-4">
                        <div class="blog-card reveal-on-scroll" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.06); background: #fff; height: 100%;">
                            <div class="image">
                                <img src="{item['img']}" alt="{item['title']}" style="width: 100%; height: 210px; object-fit: cover;">
                            </div>
                            <div class="content" style="padding: 25px;">
                                <span style="font-size: 13px; color: #DB9E30; font-weight: 700; text-transform: uppercase;">{item['category']}</span>
                                <h2 style="font-size: 19px; font-weight: 700; margin: 10px 0 12px 0;"><a href="blog-single.html" style="color: #232f4b;">{item['title']}</a></h2>
                                <p style="color: #666; font-size: 14px; line-height: 1.6;">{item['excerpt']}</p>
                                <a href="blog-single.html" class="theme-btn-s2" style="font-size: 13px; padding: 8px 18px; margin-top: 10px;">Read Full Guide</a>
                            </div>
                        </div>
                    </div>
"""

blog_body = breadcrumb("Quran Learning Resources") + f"""
        <section class="blog-section section-padding">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-7 col-12">
                        <div class="section-title text-center reveal-on-scroll">
                            <h2>Articles &amp; Guides</h2>
                            <h3>Practical Advice for Students &amp; Parents</h3>
                            <p style="color: #666; font-size: 16px; margin-top: 10px;">Helpful guides on starting online Quran lessons, Tajweed rules, and building consistent daily learning habits.</p>
                        </div>
                    </div>
                </div>
                <div class="row" style="margin-top: 30px;">
                    {blog_cards_html}
                </div>
            </div>
        </section>
"""

blog_full = COMMON_HEAD.format(
    title="Quran Learning Resources & Guides | QuranTeacher.uk",
    description="Helpful guides and advice for UK students and parents on learning Quran online, mastering Tajweed, and building consistent routines.",
    canonical_path="/blog"
) + get_header('resources') + blog_body + COMMON_FOOTER

for fname in ["blog.html", "blog-fullwidth.html", "blog-left-sidebar.html"]:
    with open(f"public/{fname}", "w", encoding="utf-8") as f:
        f.write(blog_full)

blog_single_body = breadcrumb("How to Start Learning Quran Online from Home", trail=[("Home", "index.html"), ("Resources", "blog.html")]) + """
        <section class="wpo-blog-single-section section-padding">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-9 col-12">
                        <div class="wpo-blog-single-wrap" style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
                            <div class="image" style="margin-bottom: 25px;">
                                <img src="assets/images/blog/1.jpg" alt="Online Quran Learning from Home" style="width: 100%; border-radius: 8px; max-height: 420px; object-fit: cover;">
                            </div>
                            <span style="color: #DB9E30; font-weight: 700; font-size: 13px; text-transform: uppercase;">Getting Started &bull; UK Families</span>
                            <h2 style="font-size: 30px; font-weight: 800; color: #232f4b; margin: 10px 0 20px 0;">How to Start Learning Quran Online from the Comfort of Home</h2>
                            
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">Learning the Holy Quran is one of the most rewarding commitments a Muslim family can undertake. For families living in the UK, balancing school hours, after-school clubs, and British weather often makes commuting to a physical centre difficult. Online one-to-one Quran tuition has transformed this experience, making high-quality instruction directly accessible from your home.</p>

                            <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 25px 0 15px 0;">1. Choose a Quiet, Dedicated Learning Space</h3>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">To help students focus, set up a calm area with a desktop computer, laptop, or tablet. A pair of comfortable headphones with a microphone ensures clear audio so the teacher can accurately hear every letter and Tajweed nuance.</p>

                            <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 25px 0 15px 0;">2. Start with a Structured Foundation: Noorani Qaida</h3>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">For younger children and complete beginners, beginning with Noorani Qaida is essential. It trains the student to recognise individual Arabic letters, grasp the vowels (Harakat), and learn how letters join together before attempting full verses.</p>

                            <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 25px 0 15px 0;">3. Prioritise Consistency Over Long Sessions</h3>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">Thirty minutes of focused, one-to-one tuition 3 or 4 days per week is far more effective for children than one long session at the weekend. Regular practice builds memory retention and keeps learning enjoyable.</p>

                            <h3 style="font-size: 22px; font-weight: 700; color: #232f4b; margin: 25px 0 15px 0;">4. Take Advantage of a Free Trial Lesson</h3>
                            <p style="color: #555; line-height: 1.8; font-size: 16px;">Before committing to a schedule, attend a trial lesson. This allows your child to meet their teacher, test the online platform, and assess their starting level in a relaxed, friendly environment.</p>

                            <div style="background: #fafafa; border-left: 4px solid #DB9E30; padding: 25px; border-radius: 4px; margin: 30px 0;">
                                <h4 style="font-size: 18px; font-weight: 700; color: #232f4b; margin-bottom: 8px;">Ready to begin?</h4>
                                <p style="color: #555; margin-bottom: 15px;">Book a free online trial lesson with one of our qualified teachers today.</p>
                                <a href="register.html" class="theme-btn" style="padding: 10px 25px; font-size: 14px;">Book a Free Trial</a>
                            </div>

                            <div class="author-box" style="display: flex; align-items: center; padding: 20px 0; border-top: 1px solid #e2e8f0; margin-top: 30px;">
                                <div style="margin-left: 15px;">
                                    <h5 style="font-size: 16px; font-weight: 700; color: #232f4b; margin-bottom: 2px;">QuranTeacher.uk Academic Team</h5>
                                    <p style="color: #777; font-size: 13px; margin: 0;">Dedicated to authentic online Quran education across the UK.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

blog_single_full = COMMON_HEAD.format(
    title="How to Start Learning Quran Online from Home | QuranTeacher.uk",
    description="A practical guide for parents and adult beginners in the UK starting their online Quran education journey.",
    canonical_path="/blog-single"
) + get_header('resources') + blog_single_body + COMMON_FOOTER

for fname in ["blog-single.html", "blog-single-fullwidth.html", "blog-single-left-sidebar.html"]:
    with open(f"public/{fname}", "w", encoding="utf-8") as f:
        f.write(blog_single_full)

print("  - blog.html, blog-single.html and variations written")

# -------------------------------------------------------------
# 8. PRIVACY.HTML, PRIVACE.HTML, TERMS.HTML, 404.HTML
# -------------------------------------------------------------
privacy_body = breadcrumb("Privacy Policy") + """
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-9 col-12">
                        <div style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); line-height: 1.8; color: #555;">
                            <h2 style="font-size: 28px; font-weight: 800; color: #232f4b; margin-bottom: 20px;">Privacy Policy</h2>
                            <p><strong>Effective Date:</strong> January 1, 2026</p>
                            <p>QuranTeacher.uk is committed to protecting and respecting your privacy in accordance with UK data protection laws, including the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">1. Information We Collect</h4>
                            <p>We only collect information necessary to coordinate lessons and communicate with students and parents. This includes:</p>
                            <ul>
                                <li>Parent or student name, email address, and telephone number</li>
                                <li>Student age and Quran reading level</li>
                                <li>Preferred lesson times and attendance records</li>
                            </ul>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">2. How We Use Your Information</h4>
                            <p>Your information is used strictly to:</p>
                            <ul>
                                <li>Schedule and conduct online Quran lessons</li>
                                <li>Provide student progress updates to parents</li>
                                <li>Respond to questions and customer service enquiries</li>
                            </ul>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">3. Safeguarding &amp; Security</h4>
                            <p>We treat the safeguarding of young learners with the utmost seriousness. All lesson interactions are conducted in a safe, professional online environment. We never sell, rent, or trade your personal details to third parties.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">4. Contact Us</h4>
                            <p>If you have any questions about this Privacy Policy or your data, please contact us at <a href="mailto:info@quranteacher.uk" style="color: #DB9E30;">info@quranteacher.uk</a>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

privacy_full = COMMON_HEAD.format(
    title="Privacy Policy | QuranTeacher.uk",
    description="Privacy Policy for QuranTeacher.uk online Quran tuition services in the United Kingdom.",
    canonical_path="/privacy"
) + get_header('privacy') + privacy_body + COMMON_FOOTER

with open("public/privacy.html", "w", encoding="utf-8") as f:
    f.write(privacy_full)
with open("public/privace.html", "w", encoding="utf-8") as f:
    f.write(privacy_full)

terms_body = breadcrumb("Terms & Conditions") + """
        <section class="section-padding" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-9 col-12">
                        <div style="background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); line-height: 1.8; color: #555;">
                            <h2 style="font-size: 28px; font-weight: 800; color: #232f4b; margin-bottom: 20px;">Terms &amp; Conditions</h2>
                            <p><strong>Effective Date:</strong> January 1, 2026</p>
                            <p>Welcome to QuranTeacher.uk. By booking a trial or enrolling in online Quran tuition with us, you agree to the following terms and conditions.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">1. Online Tuition Services</h4>
                            <p>QuranTeacher.uk provides live one-to-one online Quranic instruction. Lessons are scheduled at agreed UK times between the student/parent and the assigned tutor.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">2. Free Trial Lessons</h4>
                            <p>Free trial lessons are offered with no obligation to continue. They allow parents and students to evaluate our teaching method and assess the student's level.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">3. Attendance &amp; Rescheduling</h4>
                            <p>We request at least 12 hours notice if a student needs to reschedule a class, allowing our teachers to adjust their schedule accordingly.</p>

                            <h4 style="font-size: 20px; font-weight: 700; color: #232f4b; margin: 25px 0 10px 0;">4. Code of Conduct</h4>
                            <p>Both tutors and students are expected to maintain respectful, encouraging, and professional Islamic conduct at all times.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

terms_full = COMMON_HEAD.format(
    title="Terms & Conditions | QuranTeacher.uk",
    description="Terms and conditions for online Quran lessons with QuranTeacher.uk.",
    canonical_path="/terms"
) + get_header('terms') + terms_body + COMMON_FOOTER

with open("public/terms.html", "w", encoding="utf-8") as f:
    f.write(terms_full)

error_404_body = breadcrumb("Page Not Found") + """
        <section class="section-padding text-center" style="background: #fafafa;">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-6 col-md-8 col-12">
                        <div style="background: #fff; padding: 50px 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
                            <h1 style="font-size: 72px; font-weight: 900; color: #DB9E30; margin-bottom: 10px;">404</h1>
                            <h2 style="font-size: 26px; font-weight: 700; color: #232f4b; margin-bottom: 15px;">Page Not Found</h2>
                            <p style="color: #666; font-size: 15px; margin-bottom: 25px;">The page you are looking for may have been moved or does not exist.</p>
                            <a href="index.html" class="theme-btn" style="padding: 12px 35px;">Return to Homepage</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

error_404_full = COMMON_HEAD.format(
    title="Page Not Found | QuranTeacher.uk",
    description="Page not found. Return to QuranTeacher.uk homepage.",
    canonical_path="/404"
) + get_header('404') + error_404_body + COMMON_FOOTER

with open("public/404.html", "w", encoding="utf-8") as f:
    f.write(error_404_full)
print("  - privacy.html, privace.html, terms.html, 404.html written")

print("All pages successfully written!")
